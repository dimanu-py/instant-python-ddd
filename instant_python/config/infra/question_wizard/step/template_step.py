
from instant_python.config.infra.question_wizard.step.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Step
from instant_python.shared.supported_built_in_features import SupportedBuiltInFeatures
from instant_python.shared.supported_templates import SupportedTemplates


class TemplateStep(Step):
    _KEY = "template"

    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
        self._answers = {}

    def run(self) -> dict[str, dict[str, str | list[str]]]:
        name = self._choose_template_name_from_options()

        if name == SupportedTemplates.DDD and self._user_wants_to_specify_bounded_context():
            self._ask_bounded_context_name()
            self._ask_aggregate_name()

        if name != SupportedTemplates.CUSTOM:
            self._select_built_in_features()

        return {self._KEY: self._answers}

    def _choose_template_name_from_options(self) -> str:
        answer = self._questionary.single_choice_question(
            message="Select a template",
            options=SupportedTemplates.get_supported_templates(),
        )
        self._answers["name"] = answer
        return answer

    def _user_wants_to_specify_bounded_context(self) -> None:
        answer = self._questionary.boolean_question(
            message="Do you want to specify your first bounded context?",
            default=True,
        )
        self._answers["specify_bounded_context"] = answer

    def _ask_bounded_context_name(self) -> str:
        answer = self._questionary.free_text_question(
            message="Enter the bounded context name",
            default="backoffice",
        )
        self._answers["bounded_context"] = answer
        return answer

    def _ask_aggregate_name(self) -> None:
        answer = self._questionary.free_text_question(
            message="Enter the aggregate name",
            default="user",
        )
        self._answers["aggregate_name"] = answer

    def _select_built_in_features(self) -> None:
        answer = self._questionary.multiselect_question(
            message="Select the built-in features you want to include",
            options=SupportedBuiltInFeatures.get_supported_built_in_features(),
        )
        self._answers["built_in_features"] = answer
