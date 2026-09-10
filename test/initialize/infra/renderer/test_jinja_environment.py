import pytest
from expects import be_false, be_none, be_true, equal, expect, have_keys, raise_error
from jinja2 import TemplateNotFound

from instant_python.initialize.infra.renderer.jinja_environment import (
    JinjaEnvironment,
    UnknownTemplateError,
    _compute_base_path,
    _has_dependency,
    _is_in,
    _resolve_import_path,
)
from instant_python.shared.supported_templates import SupportedTemplates
from test.utils import resources_path


@pytest.mark.integration
class TestJinjaEnvironment:
    def setup_method(self) -> None:
        self._jinja_environment = JinjaEnvironment(user_template_path=str(resources_path()))

    def test_should_initialize_environment(self) -> None:
        expect(self._jinja_environment._env).not_to(be_none)

    def test_should_register_custom_filters(self) -> None:
        self._jinja_environment.add_filter("custom_filter", lambda x: x)

        expect(self._jinja_environment._env.filters).to(have_keys("custom_filter"))

    def test_should_compute_current_year_and_add_to_global_env(self) -> None:
        expect(self._jinja_environment._env.globals).to(have_keys("current_year"))

    def test_should_render_template_from_user_templates_folder_when_template_is_found(self) -> None:
        rendered_content = self._jinja_environment.render_template("hello_world.j2", {"name": "World"})

        expect(rendered_content).to(equal("Hello World!"))

    def test_should_render_template_from_default_templates_folder_when_custom_template_is_not_found(self) -> None:
        rendered_content = self._jinja_environment.render_template(
            ".gitignore", {"template": {"built_in_features": []}}
        )

        expect(rendered_content).to_not(be_none)

    def test_should_raise_error_when_template_is_not_found_anywhere(self) -> None:
        expect(lambda: self._jinja_environment.render_template("non_existing_template.j2")).to(
            raise_error(TemplateNotFound)
        )


class TestIsInFilter:
    def test_should_detect_when_a_value_is_inside_the_container(self) -> None:
        values = ["pytest", "coverage"]
        container = ["pytest", "coverage", "black"]

        result = _is_in(values, container)

        expect(result).to(be_true)

    def test_should_detect_when_no_values_are_inside_the_container(self) -> None:
        values = ["flake8", "mypy"]
        container = ["pytest", "coverage", "black"]

        result = _is_in(values, container)

        expect(result).to(be_false)

    def test_should_handle_empty_values_list(self) -> None:
        values = []
        container = ["pytest", "coverage"]

        result = _is_in(values, container)

        expect(result).to(be_false)


class TestHasDependencyFilter:
    def test_should_detect_when_dependency_exists(self) -> None:
        dependencies = [
            {"name": "pytest", "version": "7.0"},
            {"name": "coverage", "version": "6.0"},
        ]

        result = _has_dependency(dependencies, "pytest")

        expect(result).to(be_true)

    def test_should_return_false_when_dependency_does_not_exist(self) -> None:
        dependencies = [
            {"name": "pytest", "version": "7.0"},
            {"name": "coverage", "version": "6.0"},
        ]

        result = _has_dependency(dependencies, "mypy")

        expect(result).to(be_false)

    def test_should_handle_empty_dependencies_list(self) -> None:
        dependencies = []

        result = _has_dependency(dependencies, "pytest")

        expect(result).to(be_false)


class TestComputeBasePathFilter:
    _INITIAL_PATH = "shared.domain"

    def test_should_return_full_path_for_ddd_template(self) -> None:
        initial_path = self._INITIAL_PATH

        import_path = _compute_base_path(initial_path, SupportedTemplates.DDD)

        expect(import_path).to(equal(self._INITIAL_PATH))

    def test_should_remove_first_component_for_clean_architecture(self) -> None:
        import_path = _compute_base_path(self._INITIAL_PATH, SupportedTemplates.CLEAN)

        expect(import_path).to(equal("domain"))

    def test_should_remove_first_two_components_for_standard_template(self) -> None:
        import_path = _compute_base_path(self._INITIAL_PATH, SupportedTemplates.STANDARD)

        expect(import_path).to(equal(""))

    def test_should_raise_error_for_unknown_template_type(self) -> None:
        expect(lambda: _compute_base_path(self._INITIAL_PATH, "unknown_template")).to(raise_error(UnknownTemplateError))


class TestResolveImportPathFilter:
    _INITIAL_PATH = "shared.domain.event.handlers"

    def test_should_resolve_path_when_template_is_ddd(self) -> None:
        template_type = SupportedTemplates.DDD

        result = _resolve_import_path(self._INITIAL_PATH, template_type)

        expect(result).to(equal(f".{self._INITIAL_PATH}"))

    def test_should_resolve_path_when_template_is_clean(self) -> None:
        template_type = SupportedTemplates.CLEAN

        result = _resolve_import_path(self._INITIAL_PATH, template_type)

        expect(result).to(equal(".domain.event.handlers"))

    def test_should_resolve_path_when_template_is_standard(self) -> None:
        template_type = SupportedTemplates.STANDARD

        result = _resolve_import_path(self._INITIAL_PATH, template_type)

        expect(result).to(equal(".event.handlers"))
