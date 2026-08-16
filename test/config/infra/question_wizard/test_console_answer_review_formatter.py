import pytest
from expects import equal, expect

from instant_python.config.infra.question_wizard.console_answers_review_formatter import ConsoleAnswersReviewFormatter


class TestConsoleAnswerReviewFormatter:
    def setup_method(self) -> None:
        self._formatter = ConsoleAnswersReviewFormatter()

    def test_should_show_review_header(self, capsys: pytest.CaptureFixture[str]) -> None:
        self._formatter.print_answers({})

        printed_summary = capsys.readouterr().out
        expect(printed_summary).to(equal("Review Configuration\n"))

    def test_should_show_general_summary(self) -> None: ...

    def test_should_show_template_summary_without_built_in_features(self) -> None: ...

    def test_should_show_template_summary_with_built_in_features(self) -> None: ...

    def test_should_show_template_summary_with_bounded_context(self) -> None: ...

    def test_should_show_git_summary_not_initialized(self) -> None: ...

    def test_should_show_git_summary_initialized_with_username_and_email(self) -> None: ...

    def test_should_show_empty_dependencies_summary(self) -> None: ...

    def test_should_show_dependencies_summary_with_version_format(self) -> None: ...
