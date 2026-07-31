from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.shared.domain.config_repository import ConfigRepository
from instant_python.shared.domain.config_schema import ConfigSchema


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, repository: ConfigRepository) -> None:
        self._question_wizard = question_wizard
        self._repository = repository

    def execute(self) -> None:
        answers = self._ask_project_configuration_to_user()
        config = self._create_configuration_based_on_answers(answers)
        self._save_configuration(config)

    def _create_configuration_based_on_answers(self, answers: dict) -> ConfigSchema:
        return ConfigSchema.from_primitives(answers)

    def _save_configuration(self, config: ConfigSchema) -> None:
        self._repository.write(config)

    def _ask_project_configuration_to_user(self) -> dict:
        return self._question_wizard.run()
