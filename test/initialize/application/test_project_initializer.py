from pathlib import Path

import pytest
from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.initialize.application.project_initializer import ProjectInitializer
from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.domain.project_formatter import ProjectFormatter
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_writer import ProjectWriter
from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer
from test.initialize.domain.mothers.project_structure_mother import ProjectStructureMother
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


@pytest.mark.unit
class TestProjectInitializer:
    def setup_method(self) -> None:
        self._renderer = Mock(ProjectRenderer)
        self._writer = Mock(ProjectWriter)
        self._env_manager = Mock(EnvManager)
        self._version_control_configurer = Mock(VersionControlConfigurer)
        self._formatter = Mock(ProjectFormatter)
        self._project_initializer = ProjectInitializer(
            renderer=self._renderer,
            writer=self._writer,
            env_manager=self._env_manager,
            version_control_configurer=self._version_control_configurer,
            formatter=self._formatter,
        )

    def test_should_initialize_project_with_git_repository(self) -> None:
        config = ConfigSchemaMother.any()
        project_structure = ProjectStructureMother.any()
        destination_folder = Path.cwd()

        expect_call(self._renderer).render(config).returns(project_structure)
        expect_call(self._writer).write(project_structure, destination_folder).returns(None)
        expect_call(self._env_manager).setup(config.python_version, config.dependencies).returns(None)
        expect_call(self._version_control_configurer).setup(config.git).returns(None)
        expect_call(self._formatter).format().returns(None)

        self._project_initializer.execute(config=config, destination_project_folder=destination_folder)

        expect(self._renderer).to(have_been_satisfied)
        expect(self._writer).to(have_been_satisfied)
        expect(self._env_manager).to(have_been_satisfied)
        expect(self._version_control_configurer).to(have_been_satisfied)
        expect(self._formatter).to(have_been_satisfied)

    def test_should_initialize_project_without_git_repository(self) -> None:
        config = ConfigSchemaMother.without_git()
        project_structure = ProjectStructureMother.any()
        destination_folder = Path.cwd()

        expect_call(self._renderer).render(config).returns(project_structure)
        expect_call(self._writer).write(project_structure, destination_folder).returns(None)
        expect_call(self._env_manager).setup(config.python_version, config.dependencies).returns(None)
        expect_call(self._formatter).format().returns(None)

        self._project_initializer.execute(config=config, destination_project_folder=destination_folder)

        expect(self._renderer).to(have_been_satisfied)
        expect(self._writer).to(have_been_satisfied)
        expect(self._env_manager).to(have_been_satisfied)
        expect(self._version_control_configurer).to(have_been_satisfied)
        expect(self._formatter).to(have_been_satisfied)
