from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class UsageMetricsEvent:
    ipy_version: str
    operating_system: str
    command: str
    python_version: str
    dependency_manager: str
    template: str
    built_in_features: list[str]

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
