# MetricsMiddleware Refactor

## Purpose

Decouple `MetricsMiddleware` from hardcoded dependencies, fix the config path extraction bug, and raise its test coverage above 90% while keeping telemetry as a cross-cutting concern outside business logic.

## Behavior

`MetricsMiddleware` wraps the CLI group and runs after each command invocation. It collects a snapshot of the project configuration and delegates both the success and error paths to `UsageMetricsSender`, keeping telemetry outside business logic.

On a successful command, the middleware creates a config snapshot from the resolved configuration path and sends success metrics — but only when the snapshot contains real data. On a failed command, it sends error metrics regardless of the config state.

The middleware receives its collaborators (`ConfigSnapshotCreator` and `UsageMetricsSender`) through the constructor. They are wired at application startup through the `cls=` parameter of `InstantPythonTyper`, using a `lambda` or a factory function.

The configuration path used for the snapshot comes from the user-supplied `--config`/`-c` option when present; otherwise the default `ipy.yml` is used.

Metrics sending stays fire-and-forget: it runs on a daemon thread with a 5-second timeout so the CLI command is not delayed.

## Contract

- **Inputs**:
  - The `MetricsMiddleware` constructor receives `ConfigSnapshotCreator` and `UsageMetricsSender`.
  - The CLI invocation, including the optional `--config <path>` / `-c <path>` option.
  - The project config snapshot produced from the resolved configuration path.
- **Outputs**:
  - A success metrics event sent through `UsageMetricsSender` when the config snapshot has real data.
  - An error metrics event sent through `UsageMetricsSender` on command failure, always.
  - No change to CLI output, exit codes, or latency (the metrics thread timeout stays at 5 seconds).

## Edge Cases

- Successful command with an unknown config snapshot: success metrics are skipped; the command outcome is unaffected.
- Failed command with an unknown config snapshot: error metrics are still sent.
- `--config custom.yml` passed: the config snapshot is created from `custom.yml`.
- `-c custom.yml` passed: the config snapshot is created from `custom.yml`.
- No `--config`/`-c` option passed: the config snapshot is created from the default `ipy.yml`.
- The metrics thread times out or fails: the CLI command is not delayed or broken, because sending is fire-and-forget on a daemon thread.

## Decisions

- **Dependencies are injected through the constructor.**
  - Rationale: the current implementation hardcodes `ConfigSnapshotCreator` and `UsageMetricsSender`, violating Dependency Inversion and leaving the middleware untestable in isolation (48% coverage).
  - Alternative: keep the hardcoded dependencies. Rejected because it prevents isolated testing and keeps coverage at 48%.
- **Dependencies are wired in `cli.py` through the `cls=` parameter of `InstantPythonTyper`.**
  - Rationale: Typer's `cls=` accepts a class or a callable, so dependencies can be passed without changing how the middleware is registered; a factory function keeps `cli.py` clean.
  - Alternative: instantiate the dependencies inline where the app is created. Rejected in favor of explicit constructor injection wired in one place.
- **Success metrics are gated on a real config snapshot; error metrics are always sent.**
  - Rationale: reporting success with "unknown" config data produces misleading telemetry, while errors are valuable even when the config could not be read.
  - Alternative: send success metrics with unknown snapshots. Rejected because it pollutes the metrics with fabricated data.
- **The config path extraction bug is fixed as part of this effort.**
  - Rationale: it is technically independent, but the middleware is the only consumer of the extraction logic, so fixing it now avoids a separate iteration.
  - Alternative: fix it in a later iteration. Rejected because it would leave known-broken behavior in the only path that uses it.
- **Metrics sending remains fire-and-forget on a daemon thread with a 5-second timeout.**
  - Rationale: telemetry must not add latency to the CLI command.
  - Alternative: send metrics synchronously. Rejected because it delays the command.

## Open Questions

- Should `MetricsMiddleware` stop extending `TyperGroup`? Click provides alternative hooks like `@app.result_callback` or wrapping at the `InstantPythonTyper` level. Dropping the inheritance would make the middleware purely compositional. However, the `invoke()` override is the simplest hook — `result_callback` only fires on success, and there is no built-in error callback equivalent.

## Requirements

### Config snapshot

- R1: WHEN a CLI command finishes successfully AND the config snapshot contains real data, the system SHALL send success metrics through `UsageMetricsSender`.
- R2: WHEN a CLI command finishes successfully AND the config snapshot is unknown, the system SHALL NOT send success metrics.
- R3: WHEN a CLI command fails, the system SHALL send error metrics through `UsageMetricsSender`.
- R4: WHEN a CLI command fails AND the config snapshot is unknown, the system SHALL still send error metrics.

### Config path extraction

- R5: WHEN the user passes `--config <path>`, the system SHALL create the config snapshot from `<path>`.
- R6: WHEN the user passes `-c <path>`, the system SHALL create the config snapshot from `<path>`.
- R7: WHEN the user passes no `--config`/`-c` option, the system SHALL create the config snapshot from the default `ipy.yml`.

### Dependency injection

- R8: The system SHALL construct `MetricsMiddleware` with `ConfigSnapshotCreator` and `UsageMetricsSender` injected through the constructor.
- R9: The system SHALL wire the injected dependencies at application startup through the `cls=` parameter of `InstantPythonTyper`.

### Behavior preservation

- R10: The system SHALL NOT change existing CLI behavior or output.
- R11: The system SHALL keep metrics sending fire-and-forget on a daemon thread.
- R12: The system SHALL keep the metrics sending thread timeout at 5 seconds.
- R13: The `MetricsMiddleware` module SHALL have test coverage above 90%.

## Related Features

- `docs/specs/technical-debt-review.md` — documents DT-1 (hardcoded dependencies), DT-2 (config path bug), and partially DT-9 (missing tests), which this spec addresses.
- `docs/specs/0002-new-tool-management-system.md` — requirement R30 extends the metrics payload built around `ConfigSchema.for_metrics()`.
