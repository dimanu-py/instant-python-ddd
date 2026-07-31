from pathlib import Path

import yaml
from jinja2 import TemplateNotFound

from instant_python.initialize.domain.node import NodeType
from instant_python.initialize.domain.project_renderer import ProjectRenderer
from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.shared.domain.config_schema import ConfigSchema
from instant_python.shared.supported_templates import SupportedTemplates


class JinjaProjectRenderer(ProjectRenderer):
    _MAIN_STRUCTURE_TEMPLATE_FILE = "main_structure.yml"

    def __init__(self, env: JinjaEnvironment) -> None:
        self._env = env

    def render(self, context_config: ConfigSchema) -> ProjectStructure:
        template_name = self._get_project_main_structure_template(context_config)
        basic_project_structure = self._render_project_structure_with_jinja(context_config, template_name)
        project_structure_with_files_content = self._add_template_content_to_files(
            context_config, basic_project_structure
        )
        return ProjectStructure.from_raw_structure(structure=project_structure_with_files_content)

    def _render_project_structure_with_jinja(self, context_config: ConfigSchema, template_name: str) -> list[dict]:
        raw_project_structure = self._env.render_template(name=template_name, context=context_config.to_primitives())
        return yaml.safe_load(raw_project_structure)

    def _get_project_main_structure_template(self, config: ConfigSchema) -> str:
        return str(Path(config.calculate_project_structure_template_name()) / self._MAIN_STRUCTURE_TEMPLATE_FILE)

    def _add_template_content_to_files(self, context_config: ConfigSchema, project_structure: list[dict]) -> list[dict]:
        for node in project_structure:
            self._populate_file_content(context_config, node)
        return project_structure

    def _populate_file_content(self, context_config: ConfigSchema, node: dict) -> None:
        if node.get("type") == NodeType.FILE:
            try:
                template_name = node.get("template") or f"{node['name']}{node['extension']}"
                file_content = self._env.render_template(
                    name=template_name,
                    context={
                        **context_config.to_primitives(),
                        "template_types": SupportedTemplates,
                    },
                )
            except (TemplateNotFound, KeyError):
                print(f"Warning: Template not found for file {node.get('name')}, leaving content empty.")
                file_content = None
            node["content"] = file_content

        for child in node.get("children", []):
            self._populate_file_content(context_config, child)
