domain_event_template = """
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict


@dataclass(frozen=True, kw_only=True)
class DomainEvent(ABC):
    id: str

    @classmethod
    @abstractmethod
    def name(cls) -> str:
        raise NotImplementedError

    def to_dict(self) -> dict:
        return asdict(self)
""".strip()