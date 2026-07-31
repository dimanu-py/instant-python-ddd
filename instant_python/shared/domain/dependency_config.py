from dataclasses import asdict, dataclass, field

from instant_python.shared.application_error import ApplicationError


@dataclass
class DependencyConfig:
    name: str
    version: str
    is_dev: bool = field(default=False)
    group: str = field(default_factory=str)

    def __post_init__(self) -> None:
        self.version = str(self.version)
        self._ensure_dependency_is_dev_if_group_is_set()

    def to_primitives(self) -> dict[str, str | bool]:
        return asdict(self)

    def get_installation_flag(self) -> tuple[str, ...]:
        if self.group:
            return (f"--group {self.group}",)
        elif self.is_dev:
            return ("--dev",)
        return ()

    def get_specification(self) -> str:
        if self.version == "latest":
            return self.name
        return f"{self.name}=={self.version}"

    def _ensure_dependency_is_dev_if_group_is_set(self) -> None:
        if self.group and not self.is_dev:
            raise NotDevDependencyIncludedInGroup(self.name, self.group)


class NotDevDependencyIncludedInGroup(ApplicationError):
    def __init__(self, dependency_name: str, dependency_group: str) -> None:
        super().__init__(
            message=f"Dependency '{dependency_name}' has been included in group '{dependency_group}' but it is not a development dependency. Please ensure that only development dependencies are included in groups."
        )
