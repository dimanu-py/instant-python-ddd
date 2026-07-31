import shutil
from pathlib import Path

import yaml

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.domain.config_repository import ConfigRepository
from instant_python.shared.domain.config_schema import ConfigSchema


class YamlConfigRepository(ConfigRepository):
    def write(self, config: ConfigSchema) -> None:
        destination_path = config.config_file_path
        with destination_path.open("w") as file:
            yaml.dump(config.to_primitives(), file)

    def read(self, path: Path) -> ConfigSchema:
        try:
            with path.open("r") as file:
                raw_config = yaml.safe_load(file)
                return ConfigSchema.from_primitives(content=raw_config, custom_config_path=path)
        except FileNotFoundError as error:
            raise ConfigurationFileNotFound(str(path)) from error

    def move(self, config: ConfigSchema, base_directory: Path) -> None:
        final_destination = config.calculate_config_destination_path(
            base_directory=base_directory,
        )
        ipy_config_project_folder = final_destination.parent / "ipy.yml"
        shutil.move(config.config_file_path, ipy_config_project_folder)


class ConfigurationFileNotFound(ApplicationError):
    def __init__(self, path: str) -> None:
        super().__init__(
            message=f"Configuration file not found at '{path}'. To create a project, you first"
            f" need a configuration file. Please, run 'ipy config' command to create one.\n"
            f"If you have the configuration file in another location, use the '-c' flag.",
        )
