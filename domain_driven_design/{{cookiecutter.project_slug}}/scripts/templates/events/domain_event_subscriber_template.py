domain_event_subscriber_template = """
from abc import ABC, abstractmethod
from typing import Type

from src.contexts.shared.domain.event.domain_event import DomainEvent


class DomainEventSubscriber[EventType: DomainEvent](ABC):
    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[Type[EventType]]:
        raise NotImplementedError

    @abstractmethod
    def on(self, event: EventType) -> None:
        raise NotImplementedError
""".strip()