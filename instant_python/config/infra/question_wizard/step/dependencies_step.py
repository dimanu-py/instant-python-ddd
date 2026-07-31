
from instant_python.config.infra.question_wizard.step.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Step


class DependenciesStep(Step):
    _KEY = "dependencies"

    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)
        self._dependencies = []

    def run(self) -> dict[str, list[dict[str, str | bool]]]:
        while True:
            if not self._user_wants_to_install_dependencies():
                break

            name = self._ask_dependency_name()
            if not name:
                print("Dependency name cannot be empty. Let's try again.")
                continue
            version = self._ask_dependency_version()
            is_for_development = self._ask_if_dependency_is_for_development_purpose(name)
            group_name = self._ask_dev_dependency_group_name() if is_for_development else ""

            self._dependencies.append(
                {
                    "name": name,
                    "version": version,
                    "is_dev": is_for_development,
                    "group": group_name,
                }
            )

        return {self._KEY: self._dependencies}

    def _ask_dev_dependency_group_name(self) -> str:
        return self._questionary.free_text_question(
            message="Specify the name of the group where to install the dependency (leave empty if not applicable)",
            default="",
        )

    def _ask_if_dependency_is_for_development_purpose(self, name: str) -> bool:
        return self._questionary.boolean_question(
            message=f"Do you want to install {name} as a dev dependency?",
            default=False,
        )

    def _ask_dependency_version(self) -> str:
        return self._questionary.free_text_question(
            message="Enter the version of the dependency you want to install",
            default="latest",
        )

    def _ask_dependency_name(self) -> str:
        return self._questionary.free_text_question(
            message="Enter the name of the dependency you want to install",
        )

    def _user_wants_to_install_dependencies(self) -> bool:
        return self._questionary.boolean_question(
            message="Do you want to install dependencies?",
        )
