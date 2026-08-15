from abc import ABC, abstractmethod


class AnswersReviewFormatter(ABC):
    @abstractmethod
    def print_answers(self, answers: dict) -> None:
        raise NotImplementedError
