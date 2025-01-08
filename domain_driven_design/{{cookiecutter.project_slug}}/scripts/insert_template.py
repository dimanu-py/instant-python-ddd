#!/usr/bin/env python
import sys
from pathlib import Path

from scripts.templates.aggregate_root_template import aggregate_root_template
from scripts.templates.exceptions.incorrect_value_error_template import incorrect_value_type_error_template
from scripts.templates.exceptions.required_value_error_template import required_value_error_template
from scripts.templates.exceptions.invalid_negative_value_error_template import invalid_negative_value_error_template
from scripts.templates.value_objects.string_value_object_template import string_value_object_template
from scripts.templates.value_objects.uuid_template import uuid_template
from scripts.templates.value_objects.value_object_template import value_object_template
from scripts.templates.value_objects.int_value_object_template import int_value_object_template
from scripts.templates.events.domain_event_template import domain_event_template
from scripts.templates.events.domain_event_subscriber_template import domain_event_subscriber_template
from scripts.templates.events.event_bus_template import event_bus_template
from scripts.templates.events.exchange_type_template import exchange_type_template
from scripts.templates.events.rabbit_mq_configurer_template import rabbit_mq_configurer_template
from scripts.templates.events.rabbit_mq_connection_template import rabbit_mq_connection_template
from scripts.templates.events.rabbit_mq_consumer_template import rabbit_mq_consumer_template
from scripts.templates.events.rabbit_mq_event_bus_template import rabbit_mq_event_bus_template
from scripts.templates.events.rabbit_mq_queue_formatter_template import rabbit_mq_queue_formatter_template
from scripts.templates.events.rabbit_mq_settings_template import rabbit_mq_settings_template
from scripts.templates.events.domain_event_json_deserializer_template import domain_event_json_deserializer_template
from scripts.templates.events.domain_event_json_serializer_template import domain_event_json_serializer_template


TEMPLATES = {
	"value_object": value_object_template,
	"string_value_object": string_value_object_template,
	"int_value_object": int_value_object_template,
	"uuid": uuid_template,
	"incorrect_value": incorrect_value_type_error_template,
	"required_value": required_value_error_template,
	"invalid_negative_value": invalid_negative_value_error_template,
	"domain_event": domain_event_template,
	"domain_event_subscriber": domain_event_subscriber_template,
	"event_bus": event_bus_template,
	"exchange_type": exchange_type_template,
	"aggregate_root": aggregate_root_template,
	"rabbit_mq_configurer": rabbit_mq_configurer_template,
	"rabbit_mq_connection": rabbit_mq_connection_template,
	"rabbit_mq_consumer": rabbit_mq_consumer_template,
	"rabbit_mq_event_bus": rabbit_mq_event_bus_template,
	"rabbit_mq_queue_formatter": rabbit_mq_queue_formatter_template,
	"rabbit_mq_settings": rabbit_mq_settings_template,
	"domain_event_json_deserializer": domain_event_json_deserializer_template,
	"domain_event_json_serializer": domain_event_json_serializer_template,
}


def main() -> None:
	list_available_templates()
	template_name = input("Enter the name of the template you want to insert: ")
	ensure_template_exists(template_name)

	user_path = input("Enter the path where template should be created: ")
	folder_path = generate_folder_path(Path(user_path))
	write_content_at(folder_path, template_name)


def list_available_templates() -> None:
    print(f"Available templates: {', '.join(TEMPLATES.keys())}")


def ensure_template_exists(template_name: str) -> None:
	if template_name not in TEMPLATES:
		print(f"Error: Template '{template_name}' not found.")
		list_available_templates()
		sys.exit(1)


def write_content_at(folder_path: Path, template_name: str) -> None:
	file_name = f"{template_name.replace('_template', '')}.py"
	file_path = folder_path / file_name

	with open(file_path, "w") as file:
		file.write(TEMPLATES[template_name])
	print(f"Template {template_name} created at {file_path}")


def generate_folder_path(user_path: Path) -> Path:
	project_root = Path(__file__).resolve().parents[1]
	folder_path =  project_root / user_path
	folder_path.mkdir(parents=True, exist_ok=True)
	print(f"Folder created at: {folder_path}")
	return folder_path


if __name__ == "__main__":
	main()
