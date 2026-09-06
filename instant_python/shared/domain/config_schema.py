from dataclasses import dataclass, field
from pathlib import Path
from typing import TypedDict

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.domain.dependency_config import (
    DependencyConfig,
)
from instant_python.shared.domain.general_config import (
    GeneralConfig,
)
from instant_python.shared.domain.git_config import GitConfig
from instant_python.shared.domain.template_config import (
    TemplateConfig,
)
from instant_python.shared.supported_templates import SupportedTemplates

_GENERAL = "general"
_DEPENDENCIES = "dependencies"
_TEMPLATE = "template"
_GIT = "git"
_REQUIRED_CONFIG_KEYS = [_GENERAL, _DEPENDENCIES, _TEMPLATE, _GIT]

# Dropped rather than rejected so config files saved by older versions still load.
_LEGACY_GENERAL_KEYS = {"year"}


@dataclass
class ConfigSchema:
    general: GeneralConfig
    dependencies: list[DependencyConfig]
    template: TemplateConfig
    git: GitConfig
    config_file_path: Path = field(default_factory=lambda: ConfigSchema._DEFAULT_CONFIG_PATH)

    _DEFAULT_CONFIG_PATH: Path = Path.cwd() / "ipy.yml"

    @classmethod
    def from_primitives(cls, content: dict[str, dict | list], custom_config_path: Path | None = None) -> "ConfigSchema":
        cls._ensure_config_is_not_empty(content)
        cls._ensure_all_required_sections_are_present(content)
        general_content = {k: v for k, v in content[_GENERAL].items() if k not in _LEGACY_GENERAL_KEYS}
        return cls(
            general=GeneralConfig(**general_content),
            dependencies=[DependencyConfig(**dep) for dep in content[_DEPENDENCIES]] if content[_DEPENDENCIES] else [],
            template=TemplateConfig(**content[_TEMPLATE]),
            git=GitConfig(**content[_GIT]),
            config_file_path=custom_config_path if custom_config_path else cls._DEFAULT_CONFIG_PATH,
        )

    @classmethod
    def _ensure_config_is_not_empty(cls, content: dict[str, dict | list]) -> None:
        if not content:
            raise EmptyConfigurationNotAllowed

    @classmethod
    def _ensure_all_required_sections_are_present(cls, content: dict[str, dict | list]):
        missing_keys = [key for key in _REQUIRED_CONFIG_KEYS if key not in content]
        if missing_keys:
            raise ConfigKeyNotPresent(missing_keys, _REQUIRED_CONFIG_KEYS)

    def calculate_config_destination_path(self, base_directory: Path) -> Path:
        return base_directory / self.project_folder_name / self.config_file_path.name

    def calculate_project_structure_template_name(self) -> str:
        if self.template_type == SupportedTemplates.CUSTOM:
            return ""
        return self.template_type

    def to_primitives(self) -> "ConfigSchemaPrimitives":
        return ConfigSchemaPrimitives(
            general=self.general.to_primitives(),
            dependencies=[dependency.to_primitives() for dependency in self.dependencies],
            template=self.template.to_primitives(),
            git=self.git.to_primitives(),
        )

    def for_metrics(self) -> dict[str, str | list[str]]:
        return {
            "python_version": self.python_version,
            "dependency_manager": self.dependency_manager,
            "template": self.template_type,
            "built_in_features": self.template.built_in_features,
        }

    @property
    def template_type(self) -> str:
        return self.template.name

    @property
    def project_folder_name(self) -> str:
        return self.general.slug

    @property
    def dependency_manager(self) -> str:
        return self.general.dependency_manager

    @property
    def python_version(self) -> str:
        return self.general.python_version

    @property
    def version_control_has_to_be_initialized(self) -> bool:
        return self.git.initialize


class ConfigSchemaPrimitives(TypedDict):
    general: dict[str, str]
    dependencies: list[dict[str, str | bool]]
    template: dict[str, str | list[str]]
    git: dict[str, str | bool]


class ConfigKeyNotPresent(ApplicationError):
    def __init__(self, missing_keys: list[str], required_keys: list[str]) -> None:
        super().__init__(
            message=f"The following required keys are missing from the config file: {', '.join(missing_keys)}. Required keys are: {', '.join(required_keys)}."
        )


class EmptyConfigurationNotAllowed(ApplicationError):
    def __init__(self) -> None:
        super().__init__(message="Configuration file cannot be empty.")
