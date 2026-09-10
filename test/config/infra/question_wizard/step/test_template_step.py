from typing import ClassVar

import pytest
from expects import contain, expect

from instant_python.config.infra.question_wizard.step.template_step import TemplateStep
from instant_python.shared.supported_templates import SupportedTemplates
from test.config.infra.question_wizard.fake_questionary import FakeQuestionary


@pytest.mark.unit
class TestTemplateStep:
    _EMPTY_BUILT_IN_FEATURES: ClassVar[list[str]] = []
    _SPECIFY_BOUNDED_CONTEXT: ClassVar[list[bool | str]] = [True, "backoffice", "user"]

    def setup_method(self) -> None:
        self._event_log: list[str] = []

    def test_should_skip_built_in_features_for_custom_templates(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[SupportedTemplates.CUSTOM.value],
            event_log=self._event_log,
        )
        step = TemplateStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log).to_not(contain("Do you want to specify your first bounded context?"))
        expect(self._event_log).to_not(contain("Which built-in features do you want to include?"))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_ask_bounded_context_and_aggregate_for_domain_driven_design(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[SupportedTemplates.DDD.value, *self._SPECIFY_BOUNDED_CONTEXT, self._EMPTY_BUILT_IN_FEATURES],
            event_log=self._event_log,
        )
        step = TemplateStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log).to(
            contain(
                "Do you want to specify your first bounded context?",
                "What is the bounded context name?",
                "What is the aggregate name?",
            )
        )
        fake_questionary.should_have_consumed_all_answers()

    def test_should_ask_to_select_built_in_features(self) -> None:
        fake_questionary = FakeQuestionary(
            event_log=self._event_log,
            answers=[SupportedTemplates.STANDARD.value, self._EMPTY_BUILT_IN_FEATURES],
        )
        step = TemplateStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log).to(
            contain(
                "Which built-in features do you want to include?",
            )
        )
        fake_questionary.should_have_consumed_all_answers()
