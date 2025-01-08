domain_event_json_serializer_template = """
import json

from src.contexts.shared.domain.event.domain_event import DomainEvent


class DomainEventJsonSerializer:
    @staticmethod
    def serialize(event: DomainEvent) -> str:
        body = {
            "data": {
                "id": event.id,
                "type": event.name(),
                "attributes": event.to_dict(),
            }
        }
        return json.dumps(body)
""".strip()