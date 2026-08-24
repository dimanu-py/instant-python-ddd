from typing import override

from instant_python.config.domain.answers_review_formatter import AnswersReviewFormatter


class ConsoleAnswersReviewFormatter(AnswersReviewFormatter):
    _TITLE = "Review Configuration"

    @override
    def print_answers(self, answers: dict) -> None:
        summary = [self._TITLE]
        if answers:
            general_section = answers.get("general") or {}
            summary.append("General")
            for field_title, field_content in general_section.items():
                summary.append(f"  {field_title.title().replace('_', ' ')}: {field_content}")
        print("\n".join(summary))
