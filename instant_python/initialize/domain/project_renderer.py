from abc import ABC, abstractmethod

from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.shared.domain.config_schema import ConfigSchema


class ProjectRenderer(ABC):
    @abstractmethod
    def render(self, context_config: ConfigSchema) -> ProjectStructure:
        raise NotImplementedError
