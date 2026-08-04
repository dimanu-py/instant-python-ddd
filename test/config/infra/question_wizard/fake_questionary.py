from collections import deque

from instant_python.config.infra.question_wizard.step.questionary import Questionary


class FakeQuestionary(Questionary):
    def __init__(self, answers: list[object], event_log: list[str]) -> None:
        self._answers = deque(answers)
        self._event_log = event_log

    def boolean_question(self, message: str, default: bool = False) -> bool:
        self._event_log.append(message)
        return bool(self._next_answer())

    def free_text_question(self, message: str, default: str | None = None) -> str:
        self._event_log.append(message)
        return str(self._next_answer())

    def single_choice_question(self, message: str, options: list[str], default: str | None = None) -> str:
        self._event_log.append(message)
        return str(self._next_answer())

    def multiselect_question(self, message: str, options: list[str]) -> list[str]:
        self._event_log.append(message)
        answer = self._next_answer()
        return list(answer) if isinstance(answer, list) else []

    def _next_answer(self) -> object:
        return self._answers.popleft()
