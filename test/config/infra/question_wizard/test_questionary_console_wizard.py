from typing import ClassVar
from unittest.mock import patch

import pytest
from expects import equal, expect

from instant_python.config.infra.question_wizard.questionary_console_wizard import QuestionaryConsoleWizard
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
        "Enter the name of the project (CANNOT CONTAIN SPACES)",
        "Enter the name of the source folder",
        "Enter the project description",
        "Enter the project initial version",
        "Enter your name",
        "Select a license",
        "Enter the python version",
        "Select a dependency manager",
        "Select a template",
        "Select the built-in features you want to include",
        "Do you want to initialize a git repository?",
        "Type your git user name",
        "Type your git email",
        "Do you want to install dependencies?",
    ]

    def setup_method(self) -> None:
        self._event_log: list[str] = []

    def test_should_ask_all_sections_in_order(self) -> None:
        fake_questionary = FakeQuestionary(answers=self.happy_path_answers, event_log=self._event_log)

        QuestionaryConsoleWizard(questionary=fake_questionary).run()

        expect(self._event_log).to(equal([message for message in self.expected_question_messages]))

    def test_should_display_section_heading_before_its_questions(self) -> None:
        fake_questionary = FakeQuestionary(answers=self.happy_path_answers, event_log=self._event_log)

        def record_heading(*args: object) -> None:
            self._event_log.append("heading: " + " ".join(str(argument) for argument in args))

        with patch("builtins.print", side_effect=record_heading):
            QuestionaryConsoleWizard(questionary=fake_questionary).run()

        expect(self._event_log).to(equal(self._expected_events_with_section_headings()))

    def _expected_events_with_section_headings(self) -> list[str]:
        events: list[str] = []
        sections = [
            ("[1/4] General", self.expected_question_messages[0:8]),
            ("[2/4] Template", self.expected_question_messages[8:10]),
            ("[3/4] Git", self.expected_question_messages[10:13]),
            ("[4/4] Dependencies", self.expected_question_messages[13:14]),
        ]
        for heading, questions in sections:
            events.append(f"heading: {heading}")
            events.extend(f"question: {question}" for question in questions)
        return events
