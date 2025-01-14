event_bus_template = """
from abc import ABC, abstractmethod

from src.contexts.shared.domain.event.domain_event import DomainEvent


class EventBus(ABC):
    @abstractmethod
    def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError
""".strip()