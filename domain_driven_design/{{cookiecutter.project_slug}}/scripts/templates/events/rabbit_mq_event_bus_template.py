rabbit_mq_event_bus_template = """
from src.contexts.shared.domain.event.domain_event import DomainEvent
from src.contexts.shared.domain.event.event_bus import EventBus
from src.contexts.shared.infra.event.domain_event_json_serializer import (
    DomainEventJsonSerializer,
)
from src.contexts.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)


class RabbitMqEventBus(EventBus):
    def __init__(self, client: RabbitMqConnection, exchange_name: str) -> None:
        self._client = client
        self._exchange_name = exchange_name
        self._event_serializer = DomainEventJsonSerializer()

    def publish(self, events: list[DomainEvent]) -> None:
        for event in events:
            self._client.publish(
                content=self._serialize_event(event),
                exchange=self._exchange_name,
                routing_key=event.name(),
            )

    def _serialize_event(self, event: DomainEvent) -> str:
        return self._event_serializer.serialize(event)
""".strip()