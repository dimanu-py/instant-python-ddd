domain_event_json_deserializer_template = """
import json
from typing import Type

from src.contexts.shared.domain.event.domain_event import DomainEvent
from src.contexts.shared.domain.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from src.contexts.shared.domain.exceptions.domain_event_type_not_found import (
    DomainEventTypeNotFound,
)


class DomainEventJsonDeserializer:
    _events_mapping: dict[str, Type[DomainEvent]]

    def __init__(self, subscriber: DomainEventSubscriber[DomainEvent]) -> None:
        self._events_mapping = {
            event.name(): event for event in subscriber.subscribed_to()
        }

    def deserialize(self, body: bytes) -> DomainEvent:
        content = json.loads(body)
        event_class = self._events_mapping.get(content["data"]["type"])

        if not event_class:
            raise DomainEventTypeNotFound(content["data"]["type"])

        return event_class(**content["data"]["attributes"])
""".strip()