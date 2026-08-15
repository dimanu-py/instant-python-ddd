from typing import ClassVar

import pytest
from doublex import Spy
from doublex_expects import have_been_called
from expects import equal, expect

from instant_python.config.domain.answers_review_formatter import AnswersReviewFormatter
from instant_python.config.infra.question_wizard.questionary_console_wizard import (
    QuestionaryConsoleWizard,
)
from instant_python.shared.supported_templates import SupportedTemplates
from test.config.infra.question_wizard.fake_questionary import FakeQuestionary


@pytest.mark.unit
class TestQuestionaryConsoleWizard:
    happy_path_answers: ClassVar[list[object]] = [
        "example-project",
        "src",
        "Example project description",
        "0.1.0",
        "Jane Doe",
        "MIT",
        "3.13",
        "uv",
        SupportedTemplates.STANDARD.value,
        [],
        True,
        "jane",
        "jane@example.com",
        False,
    ]

    expected_question_messages: ClassVar[list[str]] = [
        "What is the project name?",
        "What is the source folder name?",
        "What is the project description?",
        "What is the initial project version?",
        "What is your name?",
        "Which license do you want to use?",
        "Which Python version do you want to use?",
        "Which dependency manager do you want to use?",
        "Which template do you want to use?",
        "Which built-in features do you want to include?",
        "Do you want to initialize a git repository?",
        "What is your Git user name?",
        "What is your Git email?",
        "Do you want to add initial dependencies?",
    ]

    def setup_method(self) -> None:
        self._event_log: list[str] = []
        self._fake_questionary = FakeQuestionary(answers=self.happy_path_answers, event_log=self._event_log)

    def test_should_ask_all_sections_in_order(self) -> None:
        console_wizard = QuestionaryConsoleWizard(questionary=self._fake_questionary)

        console_wizard.run()

        expect(self._event_log).to(equal([message for message in self.expected_question_messages]))

    def test_should_display_section_heading_before_its_questions(self, capsys: pytest.CaptureFixture[str]) -> None:
        console_wizard = QuestionaryConsoleWizard(questionary=self._fake_questionary)

        console_wizard.run()

        expected_headers = [
            "[1/4] General",
            "[2/4] Template",
            "[3/4] Git",
            "[4/4] Dependencies",
        ]
        printed_headers = capsys.readouterr().out
        expect(printed_headers.splitlines()).to(equal(expected_headers))

    def test_should_show_answers_summary(self, capsys: pytest.CaptureFixture[str]) -> None:
        answers_formatter = Spy(AnswersReviewFormatter)
        console_wizard = QuestionaryConsoleWizard(
            questionary=self._fake_questionary, review_formatter=answers_formatter
        )

        console_wizard.run()

        expect(answers_formatter.print_answers).to(have_been_called)
