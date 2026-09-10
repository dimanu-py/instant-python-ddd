from pathlib import Path

import typer

from instant_python.initialize.application.project_initializer import ProjectInitializer
from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from instant_python.initialize.infra.env_manager.uv_env_manager import UvEnvManager
from instant_python.initialize.infra.formatter.ruff_project_formatter import RuffProjectFormatter
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
from instant_python.initialize.infra.version_control.git_configurer import GitConfigurer
from instant_python.initialize.infra.writer.file_system_project_writer import FileSystemProjectWriter
from instant_python.shared.infra.persistence.yaml_config_repository import YamlConfigRepository

app = typer.Typer()


@app.command("init", help="Create a new project")
def create_new_project(
    config_file: str = typer.Option(
        "ipy.yml", "--config", "-c", help="Path to yml configuration file. Default: ipy.yml"
    ),
    custom_templates_path: str | None = typer.Option(
        None, "--templates", "-t", help="Path to custom templates folder."
    ),
) -> None:
    repository = YamlConfigRepository()
    config = repository.read(path=Path(config_file))

    current_working_directory = Path.cwd()
    console = SystemConsole(working_directory=str(current_working_directory / config.project_folder_name))
    project_initializer = ProjectInitializer(
        renderer=JinjaProjectRenderer(env=JinjaEnvironment(user_template_path=custom_templates_path)),
        writer=FileSystemProjectWriter(),
        env_manager=UvEnvManager(console=console),
        version_control_configurer=GitConfigurer(console=console),
        formatter=RuffProjectFormatter(console=console),
    )

    project_initializer.execute(
        config=config,
        destination_project_folder=current_working_directory / config.project_folder_name,
    )
    repository.move(config=config, base_directory=current_working_directory)


if __name__ == "__main__":
    app()
