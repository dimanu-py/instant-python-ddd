rabbit_mq_consumer_template = """
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from src.contexts.shared.domain.event.domain_event import DomainEvent
from src.contexts.shared.domain.event.domain_event_subscriber import (
    DomainEventSubscriber,
)
from src.contexts.shared.infra.event.domain_event_json_deserializer import (
    DomainEventJsonDeserializer,
)
from src.contexts.shared.infra.event.rabbit_mq.rabbit_mq_connection import (
    RabbitMqConnection,
)
from src.contexts.shared.infra.event.rabbit_mq.rabbit_mq_queue_formatter import (
    RabbitMqQueueFormatter,
)


class RabbitMqConsumer:
    _queue_formatter: RabbitMqQueueFormatter
    _subscriber: DomainEventSubscriber[DomainEvent]
    _client: RabbitMqConnection

    def __init__(
        self,
        client: RabbitMqConnection,
        subscriber: DomainEventSubscriber[DomainEvent],
        queue_formatter: RabbitMqQueueFormatter,
    ) -> None:
        self._queue_formatter = queue_formatter
        self._subscriber = subscriber
        self._client = client
        self._event_deserializer = DomainEventJsonDeserializer(subscriber=subscriber)

    def _on_call(
        self,
        channel: BlockingChannel,
        method: Basic.Deliver,
        properties: BasicProperties,
        body: bytes,
    ) -> None:
        event = self._deserialize_event(body)
        self._subscriber.on(event)
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self) -> None:
        self._client.consume(
            queue_name=self._queue_formatter.format(self._subscriber),
            callback=self._on_call,
        )

    def stop_consuming(self) -> None:
        self._client.close_connection()

    def _deserialize_event(self, body: bytes) -> DomainEvent:
        return self._event_deserializer.deserialize(body)
""".strip()