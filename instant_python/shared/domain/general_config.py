import re
from dataclasses import asdict, dataclass, field

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.supported_licenses import SupportedLicenses
from instant_python.shared.supported_managers import SupportedManagers
from instant_python.shared.supported_python_versions import SupportedPythonVersions


@dataclass
class GeneralConfig:
    slug: str
    source_name: str
    description: str
    version: str
    author: str
    license: str
    python_version: str
    dependency_manager: str = field(default=SupportedManagers.UV)

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self.python_version = str(self.python_version)
        self._remove_invalid_characters_from_slug_and_normalize_hyphens()
        self._ensure_license_is_supported()
        self._ensure_python_version_is_supported()
        self._ensure_dependency_manager_is_supported()

    def _remove_invalid_characters_from_slug_and_normalize_hyphens(self) -> None:
        normalized_slug = re.sub(r"[^a-z0-9]+", "-", self.slug.lower()).strip("-")
        if not normalized_slug:
            raise InvalidSlugValue(self.slug)
        self.slug = normalized_slug

    def _ensure_license_is_supported(self) -> None:
        supported_licenses = SupportedLicenses.get_supported_licenses()
        if self.license not in supported_licenses:
            raise InvalidLicenseValue(self.license, supported_licenses)

    def _ensure_python_version_is_supported(self) -> None:
        supported_python_versions = SupportedPythonVersions.get_supported_versions()
        if self.python_version not in supported_python_versions:
            raise InvalidPythonVersionValue(self.python_version, supported_python_versions)

    def _ensure_dependency_manager_is_supported(self) -> None:
        supported_dependency_managers = SupportedManagers.get_supported_managers()
        if self.dependency_manager == "pdm":
            self.dependency_manager = SupportedManagers.UV
        if self.dependency_manager not in supported_dependency_managers:
            raise InvalidDependencyManagerValue(self.dependency_manager, supported_dependency_managers)

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)


class InvalidSlugValue(ApplicationError):
    def __init__(self, value: str) -> None:
        super().__init__(message=f"Invalid slug: {value}. It must contain at least one letter or digit.")


class InvalidDependencyManagerValue(ApplicationError):
    def __init__(self, value: str, supported_values: list[str]) -> None:
        super().__init__(
            message=f"Invalid dependency manager: {value}. Allowed values are {', '.join(supported_values)}."
        )


class InvalidLicenseValue(ApplicationError):
    def __init__(self, value: str, supported_values: list[str]) -> None:
        super().__init__(message=f"Invalid license: {value}. Allowed values are {', '.join(supported_values)}.")


class InvalidPythonVersionValue(ApplicationError):
    def __init__(self, value: str, supported_values: list[str]) -> None:
        super().__init__(
            message=f"Invalid Python version: {value}. Allowed versions are {', '.join(supported_values)}."
        )
