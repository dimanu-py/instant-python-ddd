from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ErrorMetricsEvent:
    ipy_version: str
    operating_system: str
    command: str
    error_type: str
    error_message: str

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
