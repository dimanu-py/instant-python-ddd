import pytest
from expects import be_empty, be_false, be_none, be_true, expect

from instant_python.initialize.domain.node import File
from instant_python.initialize.infra.renderer.jinja_environment import JinjaEnvironment
from instant_python.initialize.infra.renderer.jinja_project_renderer import JinjaProjectRenderer
from instant_python.shared.supported_templates import SupportedTemplates
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother
from test.utils import resources_path


@pytest.mark.unit
class TestJinjaProjectRenderer:
    def test_should_render_standard_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.STANDARD.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        expect(project_structure).to_not(be_none)
        expect(project_structure).to_not(be_empty)

    def test_should_include_file_template_content_in_project_structure(self) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.STANDARD.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        first_file = next((node for node in project_structure.flatten() if isinstance(node, File)), None)
        expect(first_file).to_not(be_none)
        expect(first_file.is_empty()).to(be_false)

    def test_should_include_file_template_content_in_custom_project_when_name_and_extension_match_default_template(
        self,
    ) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.CUSTOM.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        first_file = next((node for node in project_structure.flatten() if isinstance(node, File)), None)
        expect(first_file).to_not(be_none)
        expect(first_file.is_empty()).to(be_false)

    def test_should_leave_file_template_content_empty_in_custom_project_when_name_and_extension_does_not_match_default_template(
        self,
    ) -> None:
        config = ConfigSchemaMother.with_template(template=SupportedTemplates.CUSTOM.value)
        renderer = JinjaProjectRenderer(env=JinjaEnvironment(str(resources_path())))

        project_structure = renderer.render(context_config=config)

        unmatched_file = next(
            (node for node in project_structure.flatten() if isinstance(node, File) and node._name == "unmatched_file"),
            None,
        )
        expect(unmatched_file).to_not(be_none)
        expect(unmatched_file.is_empty()).to(be_true)
