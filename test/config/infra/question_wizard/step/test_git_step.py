from typing import ClassVar

import pytest
from expects import equal, expect

from instant_python.config.infra.question_wizard.step.git_step import GitStep
from test.config.infra.question_wizard.fake_questionary import FakeQuestionary


@pytest.mark.unit
class TestGitStep:
    _INITIALIZE_GIT: ClassVar[bool] = True
    _SKIP_GIT_INITIALIZATION: ClassVar[bool] = False
    _A_GIT_USERNAME: ClassVar[str] = "johndoe"
    _A_GIT_EMAIL: ClassVar[str] = "johndoe@git.com"
    _A_GIT_CONFIG: ClassVar[dict[str, str]] = {"username": _A_GIT_USERNAME, "email": _A_GIT_EMAIL}

    def setup_method(self) -> None:
        self._event_log: list[str] = []

    def test_should_skip_asking_for_git_user_configuration(self) -> None:
        fake_questionary = FakeQuestionary(answers=[self._SKIP_GIT_INITIALIZATION], event_log=self._event_log)
        step = GitStep(questionary=fake_questionary)

        git_config = step.run()

        expect(git_config).to(equal({"git": {"initialize": self._SKIP_GIT_INITIALIZATION}}))
        fake_questionary.should_have_consumed_all_answers()

    def test_should_ask_git_username_and_email_when_git_is_selected(self) -> None:
        fake_questionary = FakeQuestionary(
            answers=[self._INITIALIZE_GIT, self._A_GIT_USERNAME, self._A_GIT_EMAIL],
            event_log=self._event_log,
        )
        step = GitStep(questionary=fake_questionary)

        git_config = step.run()

        expect(git_config).to(equal({"git": {"initialize": self._INITIALIZE_GIT, **self._A_GIT_CONFIG}}))
        fake_questionary.should_have_consumed_all_answers()
