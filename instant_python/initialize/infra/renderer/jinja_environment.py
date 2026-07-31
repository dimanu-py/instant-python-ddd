from collections.abc import Callable
from typing import Any, ClassVar

from jinja2 import ChoiceLoader, Environment, FileSystemLoader, PackageLoader

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.supported_templates import SupportedTemplates


class JinjaEnvironment:
    _EMPTY_CONTEXT: ClassVar[dict] = {}
    _BASE_PACKAGE_NAME: ClassVar[str] = "instant_python"
    _PROJECT_STRUCTURE_TEMPLATE_PATH: ClassVar[str] = "templates/project_structure"
    _BOILERPLATE_TEMPLATE_PATH: ClassVar[str] = "templates/boilerplate"

    def __init__(self, user_template_path: str | None = None) -> None:
        self._env = Environment(
            loader=ChoiceLoader(
                [
                    FileSystemLoader(user_template_path if user_template_path else []),
                    PackageLoader(
                        package_name=self._BASE_PACKAGE_NAME, package_path=self._PROJECT_STRUCTURE_TEMPLATE_PATH
                    ),
                    PackageLoader(package_name=self._BASE_PACKAGE_NAME, package_path=self._BOILERPLATE_TEMPLATE_PATH),
                ]
            ),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )
        self.add_filter("is_in", _is_in)
        self.add_filter("compute_base_path", _compute_base_path)
        self.add_filter("has_dependency", _has_dependency)
        self.add_filter("resolve_import_path", _resolve_import_path)

    def render_template(self, name: str, context: dict[str, Any] | None = None) -> str:
        template = self._env.get_template(name)
        return template.render(**(context or self._EMPTY_CONTEXT))

    def add_filter(self, name: str, filter_: Callable) -> None:
        self._env.filters[name] = filter_


class UnknownTemplateError(ApplicationError):
    def __init__(self, template_name: str) -> None:
        super().__init__(message=f"Unknown template type: {template_name}")


def _is_in(values: list[str], container: list) -> bool:
    return any(value in container for value in values)


def _has_dependency(dependencies: list[dict], dependency_name: str) -> bool:
    return any(dep.get("name") == dependency_name for dep in dependencies)


def _compute_base_path(initial_path: str, template_type: str) -> str:
    if template_type == SupportedTemplates.DDD:
        return initial_path

    path_components = initial_path.split(".")
    if template_type == SupportedTemplates.CLEAN:
        return ".".join(path_components[1:])
    elif template_type == SupportedTemplates.STANDARD:
        return ".".join(path_components[2:])
    else:
        raise UnknownTemplateError(template_type)


def _resolve_import_path(initial_path: str, template_type: str) -> str:
    base_path = _compute_base_path(initial_path, template_type)
    return f".{base_path}" if base_path else ""
