exchange_type_template = """
from enum import StrEnum


class ExchangeType(StrEnum):
    TOPIC = "topic"
    DIRECT = "direct"
    FANOUT = "fanout"
""".strip()