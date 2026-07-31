from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import ClassVar

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
    dependency_manager: str
    year: int = field(default=datetime.now(tz=timezone.utc).year)

    _SUPPORTED_DEPENDENCY_MANAGERS: ClassVar[list[str]] = SupportedManagers.get_supported_managers()
    _SUPPORTED_PYTHON_VERSIONS: ClassVar[list[str]] = SupportedPythonVersions.get_supported_versions()
    _SUPPORTED_LICENSES: ClassVar[list[str]] = SupportedLicenses.get_supported_licenses()

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self.python_version = str(self.python_version)
        self._remove_white_spaces_from_slug_if_present()
        self._ensure_license_is_supported()
        self._ensure_python_version_is_supported()
        self._ensure_dependency_manager_is_supported()

    def _remove_white_spaces_from_slug_if_present(self) -> None:
        if " " in self.slug:
            self.slug = self.slug.replace(" ", "")

    def _ensure_license_is_supported(self) -> None:
        if self.license not in self._SUPPORTED_LICENSES:
            raise InvalidLicenseValue(self.license, self._SUPPORTED_LICENSES)

    def _ensure_python_version_is_supported(self) -> None:
        if self.python_version not in self._SUPPORTED_PYTHON_VERSIONS:
            raise InvalidPythonVersionValue(self.python_version, self._SUPPORTED_PYTHON_VERSIONS)

    def _ensure_dependency_manager_is_supported(self) -> None:
        if self.dependency_manager not in self._SUPPORTED_DEPENDENCY_MANAGERS:
            raise InvalidDependencyManagerValue(self.dependency_manager, self._SUPPORTED_DEPENDENCY_MANAGERS)

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)


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
