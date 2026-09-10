from pathlib import Path

import pytest
from doublex import Mock, expect_call
from expects import be_false, be_true, equal, expect

from instant_python.metrics.application.config_snapshot_creator import ConfigSnapshotCreator
from instant_python.metrics.domain.config_snapshot import ConfigSnapshot
from instant_python.shared.domain.config_repository import ConfigRepository
from instant_python.shared.infra.persistence.yaml_config_repository import ConfigurationFileNotFound
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


@pytest.mark.unit
class TestConfigSnapshotCreator:
    def setup_method(self) -> None:
        self._repository = Mock(ConfigRepository)
        self._config_snapshot_creator = ConfigSnapshotCreator(repository=self._repository)

    def test_should_create_snapshot_when_config_exists(self) -> None:
        config_path = Path("ipy.yml")
        config = ConfigSchemaMother.any()
        expect_call(self._repository).read(config_path).returns(config)

        snapshot_taken = self._config_snapshot_creator.execute(config_path)

        expect(snapshot_taken.is_unknown()).to(be_false)
        expect(snapshot_taken).to(equal(ConfigSnapshot(**config.for_metrics())))

    def test_should_create_unknown_snapshot_when_config_does_not_exist(self) -> None:
        config_path = Path("ipy.yml")
        expect_call(self._repository).read(config_path).raises(ConfigurationFileNotFound(str(config_path)))

        snapshot_taken = self._config_snapshot_creator.execute(config_path)

        expect(snapshot_taken.is_unknown()).to(be_true)
