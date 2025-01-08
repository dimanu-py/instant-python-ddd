rabbit_mq_connection_template = """
from typing import Callable

import pika
from pika.adapters.blocking_connection import BlockingChannel

from src.contexts.shared.domain.event.exchange_type import ExchangeType
from src.contexts.shared.domain.exceptions.rabbit_mq_connection_not_established_error import (
    RabbitMqConnectionNotEstablishedError,
)
from src.contexts.shared.infra.event.rabbit_mq.rabbit_mq_settings import (
    RabbitMqSettings,
)


class RabbitMqConnection:
    _channel: BlockingChannel | None
    _connection: pika.BlockingConnection | None
    _connection_settings: RabbitMqSettings

    def __init__(self, connection_settings: RabbitMqSettings) -> None:
        self._connection_settings = connection_settings
        self._connection = None
        self._channel = None
        self.open_connection()

    def open_connection(self) -> None:
        credentials = pika.PlainCredentials(
            username=self._connection_settings.user,
            password=self._connection_settings.password,
        )
        self._connection = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host=self._connection_settings.host, credentials=credentials
            )
        )
        self._channel = self._connection.channel()

    def _ensure_channel_exists(self) -> None:
        if self._channel is None:
            raise RabbitMqConnectionNotEstablishedError

    def create_exchange(self, name: str) -> None:
        self._ensure_channel_exists()
        self._channel.exchange_declare(exchange=name, exchange_type=ExchangeType.TOPIC)  # type: ignore

    def publish(self, content: str, exchange: str, routing_key: str) -> None:
        self._ensure_channel_exists()
        self._channel.basic_publish(  # type: ignore
            exchange=exchange,
            routing_key=routing_key,
            body=content,
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )

    def bind_queue_to_exchange(
        self, queue_name: str, exchange_name: str, routing_key: str
    ) -> None:
        self._ensure_channel_exists()
        self._channel.queue_bind(  # type: ignore
            exchange=exchange_name, queue=queue_name, routing_key=routing_key
        )

    def create_queue(self, name: str) -> None:
        self._ensure_channel_exists()
        self._channel.queue_declare(queue=name, durable=True)  # type: ignore

    def consume(self, queue_name: str, callback: Callable) -> None:
        self._ensure_channel_exists()
        self._channel.basic_consume(  # type: ignore
            queue=queue_name, on_message_callback=callback, auto_ack=False
        )
        self._channel.start_consuming()  # type: ignore

    def close_connection(self) -> None:
        self._channel.close()  # type: ignore
""".strip()