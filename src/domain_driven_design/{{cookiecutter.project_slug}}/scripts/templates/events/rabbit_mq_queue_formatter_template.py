rabbit_mq_queue_formatter_template = """
import re

from src.contexts.shared.domain.event.domain_event import DomainEvent
from src.contexts.shared.domain.event.domain_event_subscriber import (
    DomainEventSubscriber,
)


class RabbitMqQueueFormatter:
    _bounded_context: str
    CAMEL_CASE_TO_SNAKE_CASE_PATTERN = r"(?<!^)(?=[A-Z])"

    def __init__(self, bounded_context: str) -> None:
        self._bounded_context = bounded_context

    def format(self, subscriber: DomainEventSubscriber[DomainEvent]) -> str:
        unformatted_subscriber_name = subscriber.__class__.__name__
        formatted_subscriber_name = re.sub(
            self.CAMEL_CASE_TO_SNAKE_CASE_PATTERN, "_", unformatted_subscriber_name
        ).lower()
        return f"{self._bounded_context}.{formatted_subscriber_name}"
""".strip()