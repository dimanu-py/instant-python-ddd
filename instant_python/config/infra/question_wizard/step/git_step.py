from instant_python.config.infra.question_wizard.step.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Step


class GitStep(Step):
    _KEY = "git"

    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
        self._answers = {}

    @property
    def title(self) -> str:
        return "Git"

    def run(self) -> dict[str, dict[str, str | bool]]:
        if not self._user_wants_initialize_git_repository():
            return {self._KEY: self._answers}

        self._ask_git_username()
        self._ask_git_email()

        return {self._KEY: self._answers}

    def _ask_git_email(self) -> None:
        answer = self._questionary.free_text_question(
            message="What is your Git email?",
        )
        self._answers["email"] = answer

    def _ask_git_username(self) -> None:
        answer = self._questionary.free_text_question(
            message="What is your Git user name?",
        )
        self._answers["username"] = answer

    def _user_wants_initialize_git_repository(self) -> bool:
        answer = self._questionary.boolean_question(
            message="Do you want to initialize a git repository?",
            default=True,
        )
        self._answers["initialize"] = answer
        return answer
