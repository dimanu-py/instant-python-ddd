from typing import override

from instant_python.config.domain.answers_review_formatter import AnswersReviewFormatter


class ConsoleAnswersReviewFormatter(AnswersReviewFormatter):
    @override
    def print_answers(self, answers: dict) -> None:
        raise NotImplementedError
