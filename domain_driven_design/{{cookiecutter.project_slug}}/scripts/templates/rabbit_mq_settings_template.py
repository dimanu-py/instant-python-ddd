rabbit_mq_settings_template = """
from dataclasses import dataclass


@dataclass(kw_only=True)
class RabbitMqSettings:
    user: str
    password: str
    host: str
""".strip()