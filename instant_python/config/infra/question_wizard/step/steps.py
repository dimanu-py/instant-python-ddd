from abc import ABC, abstractmethod
from collections.abc import Iterator

from instant_python.config.infra.question_wizard.step.questionary import Questionary


class Step(ABC):
    def __init__(self, questionary: Questionary) -> None:
        self._questionary = questionary

    @property
    @abstractmethod
    def title(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> dict[str, dict]:
        raise NotImplementedError


class Steps:
    def __init__(self, *step: Step) -> None:
        self._steps = list(step)

    def __iter__(self) -> Iterator[Step]:
        return iter(self._steps)

    def __len__(self) -> int:
        return len(self._steps)
