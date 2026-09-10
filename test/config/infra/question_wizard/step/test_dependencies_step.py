from typing import ClassVar

import pytest
from expects import contain, equal, expect
from pytest import CaptureFixture

from instant_python.config.infra.question_wizard.step.dependencies_step import DependenciesStep
from test.config.infra.question_wizard.fake_questionary import FakeQuestionary


@pytest.mark.unit
class TestDependencyStep:
    _A_DEPENDENCY_NAME: ClassVar[str] = "sindripy"
    _A_VERSION: ClassVar[str] = "latest"
    _A_GROUP_NAME: ClassVar[str] = "test"
    _EMPTY_GROUP_NAME: ClassVar[str] = ""
    _EMPTY_DEPENDENCY_NAME: ClassVar[str] = ""

    _WANTS_TO_ADD_INITIAL_DEPENDENCIES: ClassVar[bool] = True
    _WANTS_TO_ADD_ANOTHER_DEPENDENCY: ClassVar[bool] = True
    _DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES: ClassVar[bool] = False

    _A_PRODUCTION_DEPENDENCY_IS_DEV: ClassVar[bool] = False
    _A_DEV_DEPENDENCY_IS_DEV: ClassVar[bool] = True

    _NO_DEPENDENCIES: ClassVar[list[dict[str, str | bool]]] = []
    _A_PRODUCTION_DEPENDENCY: ClassVar[dict[str, str | bool]] = {
        "name": _A_DEPENDENCY_NAME,
        "version": _A_VERSION,
        "is_dev": _A_PRODUCTION_DEPENDENCY_IS_DEV,
        "group": _EMPTY_GROUP_NAME,
    }
    _A_DEV_DEPENDENCY_WITHOUT_GROUP: ClassVar[dict[str, str | bool]] = {
        "name": _A_DEPENDENCY_NAME,
        "version": _A_VERSION,
        "is_dev": _A_DEV_DEPENDENCY_IS_DEV,
        "group": _EMPTY_GROUP_NAME,
    }
    _A_DEV_DEPENDENCY_WITH_GROUP: ClassVar[dict[str, str | bool]] = {
        "name": _A_DEPENDENCY_NAME,
        "version": _A_VERSION,
        "is_dev": _A_DEV_DEPENDENCY_IS_DEV,
        "group": _A_GROUP_NAME,
    }

    def setup_method(self) -> None:
        self._event_log: list[str] = []

    def test_should_skip_dependency_installation_when_user_skips_the_step(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        dependencies = step.run()

        expect(dependencies).to(equal({"dependencies": self._NO_DEPENDENCIES}))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_include_production_dependency(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._WANTS_TO_ADD_INITIAL_DEPENDENCIES]
            + self._answers_for_a_production_dependency()
            + [self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        dependencies = step.run()

        expect(dependencies).to(equal({"dependencies": [self._A_PRODUCTION_DEPENDENCY]}))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_not_include_group_name_in_a_development_dependency_when_not_specified(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._WANTS_TO_ADD_INITIAL_DEPENDENCIES]
            + self._answers_for_a_dev_dependency(self._EMPTY_GROUP_NAME)
            + [self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        dependencies = step.run()

        expect(dependencies).to(equal({"dependencies": [self._A_DEV_DEPENDENCY_WITHOUT_GROUP]}))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_include_specified_group_name_in_a_development_dependency(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._WANTS_TO_ADD_INITIAL_DEPENDENCIES]
            + self._answers_for_a_dev_dependency(self._A_GROUP_NAME)
            + [self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        dependencies = step.run()

        expect(dependencies).to(equal({"dependencies": [self._A_DEV_DEPENDENCY_WITH_GROUP]}))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_prompt_with_the_initial_dependency_message(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log).to(equal(["Do you want to add initial dependencies?"]))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_ask_dependency_name_again_when_first_time_is_empty(self, capsys: CaptureFixture[str]) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._WANTS_TO_ADD_INITIAL_DEPENDENCIES]
            + [self._EMPTY_DEPENDENCY_NAME]
            + self._answers_for_a_production_dependency()
            + [self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log.count("What is the name of the dependency?")).to(equal(2))
        output = capsys.readouterr().out
        expect(output).to(contain("Dependency name cannot be empty. Let's try again."))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_prompt_with_the_another_dependency_message_for_following_dependencies(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._WANTS_TO_ADD_INITIAL_DEPENDENCIES]
            + self._answers_for_a_production_dependency()
            + [self._WANTS_TO_ADD_ANOTHER_DEPENDENCY]
            + self._answers_for_a_production_dependency()
            + [self._DOES_NOT_WANT_TO_ADD_MORE_DEPENDENCIES],
            event_log=self._event_log,
        )
        step = DependenciesStep(questionary=fake_questionary)

        step.run()

        expect(self._event_log).to(contain("Do you want to add initial dependencies?"))
        expect(self._event_log).to(contain("Do you want to add another dependency?"))
        fake_questionary.should_have_consumed_all_answers()

    def _answers_for_a_production_dependency(self) -> list[object]:
        return [self._A_DEPENDENCY_NAME, self._A_VERSION, self._A_PRODUCTION_DEPENDENCY_IS_DEV]

    def _answers_for_a_dev_dependency(self, group_name: str) -> list[object]:
        return [self._A_DEPENDENCY_NAME, self._A_VERSION, self._A_DEV_DEPENDENCY_IS_DEV, group_name]
