from typing import ClassVar

import pytest
from doublex import Spy
from doublex_expects import have_been_called, have_been_called_with
from expects import be_none, equal, expect, have_keys

from instant_python.config.domain.answers_review_formatter import AnswersReviewFormatter
from instant_python.config.infra.question_wizard.questionary_console_wizard import (
    QuestionaryConsoleWizard,
)
from instant_python.shared.domain.general_config import InvalidPythonVersionValue
from instant_python.shared.supported_templates import SupportedTemplates
from test.config.infra.question_wizard.fake_questionary import FakeQuestionary


@pytest.mark.unit
class TestQuestionaryConsoleWizard:
    _HAPPY_PATH_ANSWERS: ClassVar[list[object]] = [
        "example-project",
        "src",
        "Example project description",
        "0.1.0",
        "Jane Doe",
        "MIT",
        "3.13",
        SupportedTemplates.STANDARD.value,
        [],
        True,
        "jane",
        "jane@example.com",
        False,
        True,
    ]
    _ANSWERS_WITH_INVALID_ANSWER: ClassVar[list[object]] = [
        "example-project",
        "src",
        "Example project description",
        "0.1.0",
        "Jane Doe",
        "MIT",
        "3.3",
        SupportedTemplates.STANDARD.value,
        [],
        True,
        "jane",
        "jane@example.com",
        False,
        True,
    ]
    _ANSWERS_WITH_WRONG_SLUG_FORMAT: ClassVar[list[object]] = ["ExampleProject"] + _HAPPY_PATH_ANSWERS[1:]
    _NOT_SAVED_ANSWERS: ClassVar[list[object]] = _HAPPY_PATH_ANSWERS[:-1] + [False]

    expected_question_messages: ClassVar[list[str]] = [
        "What is the project name?",
        "What is the source folder name?",
        "What is the project description?",
        "What is the initial project version?",
        "What is your name?",
        "Which license do you want to use?",
        "Which Python version do you want to use?",
        "Which template do you want to use?",
        "Which built-in features do you want to include?",
        "Do you want to initialize a git repository?",
        "What is your Git user name?",
        "What is your Git email?",
        "Do you want to add initial dependencies?",
        "Do you want to save this project configuration?",
    ]

    def setup_method(self) -> None:
        self._event_log: list[str] = []
        self._answers_formatter = Spy(AnswersReviewFormatter)
        self._fake_questionary = FakeQuestionary(answers=self._HAPPY_PATH_ANSWERS, event_log=self._event_log)
        self._console_wizard = QuestionaryConsoleWizard(
            questionary=self._fake_questionary, review_formatter=self._answers_formatter
        )

    def test_should_ask_all_sections_in_order(self) -> None:
        self._console_wizard.run()

        expect(self._event_log).to(equal([message for message in self.expected_question_messages]))

    def test_should_display_section_heading_before_its_questions(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._console_wizard.run()

        expected_headers = [
            "[1/4] General",
            "[2/4] Template",
            "[3/4] Git",
            "[4/4] Dependencies",
        ]
        printed_headers = capsys.readouterr().out
        expect(printed_headers.splitlines()).to(equal(expected_headers))

    def test_should_show_answers_summary(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._console_wizard.run()

        expect(self._answers_formatter.print_answers).to(have_been_called)

    def test_should_fail_fast_when_config_has_invalid_answers(self) -> None:
        fake_questionary = FakeQuestionary(answers=self._ANSWERS_WITH_INVALID_ANSWER, event_log=self._event_log)
        console_wizard = QuestionaryConsoleWizard(
            questionary=fake_questionary, review_formatter=self._answers_formatter
        )

        with pytest.raises(InvalidPythonVersionValue):
            console_wizard.run()

    def test_should_send_formatted_slug_to_answers_formatter(self) -> None:
        fake_questionary = FakeQuestionary(answers=self._ANSWERS_WITH_WRONG_SLUG_FORMAT, event_log=self._event_log)
        console_wizard = QuestionaryConsoleWizard(
            questionary=fake_questionary, review_formatter=self._answers_formatter
        )

        console_wizard.run()

        expect(self._answers_formatter.print_answers).to(
            have_been_called_with(have_keys(general=have_keys(slug="exampleproject"))).once
        )

    def test_should_return_empty_config_when_user_does_not_save_it(self) -> None:
        fake_questionary = FakeQuestionary(answers=self._NOT_SAVED_ANSWERS, event_log=self._event_log)
        console_wizard = QuestionaryConsoleWizard(
            questionary=fake_questionary, review_formatter=self._answers_formatter
        )

        config = console_wizard.run()

        expect(config).to(be_none)
