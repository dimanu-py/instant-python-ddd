from pathlib import Path

from instant_python.initialize.domain.env_manager import EnvManager
from instant_python.initialize.domain.project_formatter import ProjectFormatter
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_writer import ProjectWriter
from instant_python.initialize.domain.version_control_configurer import VersionControlConfigurer
from instant_python.shared.domain.config_schema import ConfigSchema


class ProjectInitializer:
    def __init__(
        self,
        renderer: ProjectRenderer,
        writer: ProjectWriter,
        env_manager: EnvManager,
        version_control_configurer: VersionControlConfigurer,
        formatter: ProjectFormatter,
    ) -> None:
        self._project_renderer = renderer
        self._writer = writer
        self._env_manager = env_manager
        self._version_control_configurer = version_control_configurer
        self._formatter = formatter

    def execute(self, config: ConfigSchema, destination_project_folder: Path) -> None:
        self._create_project_at_destination_folder(config, destination_project_folder)
        self._setup_development_environment(config)
        if config.version_control_has_to_be_initialized:
            self._setup_version_control_system(config)
        self._format_final_project()

    def _format_final_project(self) -> None:
        self._formatter.format()

    def _setup_version_control_system(self, config: ConfigSchema) -> None:
        self._version_control_configurer.setup(config.git)

    def _setup_development_environment(self, config: ConfigSchema) -> None:
        self._env_manager.setup(
            python_version=config.python_version,
            dependencies=config.dependencies,
        )

    def _create_project_at_destination_folder(self, config: ConfigSchema, destination_project_folder: Path) -> None:
        project_structure = self._project_renderer.render(context_config=config)
        self._writer.write(project_structure=project_structure, destination=destination_project_folder)
