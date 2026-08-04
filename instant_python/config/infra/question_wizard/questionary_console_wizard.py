from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.config.infra.question_wizard.step.dependencies_step import DependenciesStep
from instant_python.config.infra.question_wizard.step.general_step import GeneralStep
from instant_python.config.infra.question_wizard.step.git_step import GitStep
from instant_python.config.infra.question_wizard.step.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Steps
from instant_python.config.infra.question_wizard.step.template_step import TemplateStep


class QuestionaryConsoleWizard(QuestionWizard):
    def __init__(self, questionary: Questionary) -> None:
        self._steps = Steps(
            GeneralStep(questionary=questionary),
            TemplateStep(questionary=questionary),
            GitStep(questionary=questionary),
            DependenciesStep(questionary=questionary),
        )
        self._answers = {}

    def run(self) -> dict:
        for position, step in enumerate(self._steps, start=1):
            self._show_section_heading(position, step.title)
            answer = step.run()
            self._answers.update(answer)

        return self._answers

    def _show_section_heading(self, position: int, section_title: str) -> None:
        print(f"[{position}/{len(self._steps)}] {section_title}")
