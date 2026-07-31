import threading
from pathlib import Path
from typing import Any

from click import Context
from typer.core import TyperGroup

from instant_python.metrics.application.config_snapshot_creator import ConfigSnapshotCreator
from instant_python.metrics.application.usage_metrics_sender import UsageMetricsSender
from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.metrics.infra.post_hog_config import PostHogConfig
from instant_python.metrics.infra.post_hog_metrics_reporter import PostHogMetricsReporter
from instant_python.metrics.infra.user_identity_manager import UserIdentityManager
from instant_python.shared.infra.persistence.yaml_config_repository import YamlConfigRepository


class MetricsMiddleware(TyperGroup):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._config_snapshot_creator = ConfigSnapshotCreator(repository=YamlConfigRepository())
        self._metrics_sender = UsageMetricsSender(
            reporter=PostHogMetricsReporter(
                config=PostHogConfig(),
                user_identity_manager=UserIdentityManager(),
            ),
        )

    def invoke(self, ctx: Context) -> Any:
        config_path = self._extract_config_path(ctx)
        config_snapshot = self._take_first_config_snapshot(config_path)
        try:
            self._execute_command(ctx)
        except Exception as exception:
            self._send_error_metrics(ctx, exception)
            raise
        self._send_success_metrics(config_path, config_snapshot, ctx)

    def _send_success_metrics(self, config_path: Path, config_snapshot: ConfigSnapshot, ctx: Context) -> None:
        config_snapshot = self._retake_config_snapshot_if_needed(config_snapshot, config_path)
        if config_snapshot.is_unknown():
            return
        command = self._extract_executed_command(ctx)
        self._send_metrics_data(command, config_snapshot)

    def _send_error_metrics(self, ctx: Context, exception: Exception) -> None:
        command = self._extract_executed_command(ctx)
        self._send_error_data(command, exception)

    def _execute_command(self, ctx: Context) -> None:
        super().invoke(ctx)

    @staticmethod
    def _extract_executed_command(ctx: Context) -> str:
        return ctx.invoked_subcommand

    @staticmethod
    def _extract_config_path(ctx: Context) -> Path:
        if ctx.args and ("--config" in ctx.args or "-c" in ctx.args):
            return (
                Path(ctx.args[ctx.args.index("--config") + 1])
                if "--config" in ctx.args
                else Path(ctx.args[ctx.args.index("-c") + 1])
            )
        return Path("ipy.yml")

    def _take_first_config_snapshot(self, config_path: Path) -> ConfigSnapshot:
        return self._config_snapshot_creator.execute(config_path)

    def _retake_config_snapshot_if_needed(self, config_snapshot: ConfigSnapshot, config_path: Path) -> ConfigSnapshot:
        if config_snapshot.is_unknown():
            return self._config_snapshot_creator.execute(config_path)
        return config_snapshot

    def _send_metrics_data(self, command: str, config_snapshot: ConfigSnapshot) -> None:
        thread = threading.Thread(
            target=self._metrics_sender.execute_on_success,
            args=(command, config_snapshot),
            daemon=True,
        )
        thread.start()
        thread.join(timeout=5.0)

    def _send_error_data(self, command: str, exception: Exception) -> None:
        thread = threading.Thread(
            target=self._metrics_sender.execute_on_failure,
            args=(command, exception),
            daemon=True,
        )
        thread.start()
        thread.join(timeout=5.0)
