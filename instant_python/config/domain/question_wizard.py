from abc import ABC, abstractmethod

from instant_python.shared.domain.config_schema import ConfigSchema


class QuestionWizard(ABC):
    @abstractmethod
    def run(self) -> ConfigSchema | None:
        raise NotImplementedError
