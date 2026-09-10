import random
from typing import ClassVar

from instant_python.shared.domain.general_config import (
    GeneralConfig,
)
from test.random_generator import RandomGenerator


class GeneralConfigMother:
    _SUPPORTED_PYTHON_VERSIONS: ClassVar[list[str]] = ["3.10", "3.11", "3.12", "3.13"]
    _SUPPORTED_LICENSES: ClassVar[list[str]] = ["MIT", "Apache", "GPL"]

    @classmethod
    def any(cls) -> GeneralConfig:
        return GeneralConfig(
            slug=RandomGenerator.word(),
            source_name=RandomGenerator.word(),
            description=RandomGenerator.description(),
            version=RandomGenerator.version(),
            author=RandomGenerator.name(),
            license=random.choice(cls._SUPPORTED_LICENSES),
            python_version=random.choice(cls._SUPPORTED_PYTHON_VERSIONS),
            dependency_manager="uv",
        )

    @classmethod
    def with_parameter(cls, **custom_options) -> GeneralConfig:
        defaults = cls.any().to_primitives()
        defaults.update(custom_options)
        return GeneralConfig(**defaults)

    @classmethod
    def default_dependency_manager(cls) -> GeneralConfig:
        return GeneralConfig(
            slug=RandomGenerator.word(),
            source_name=RandomGenerator.word(),
            description=RandomGenerator.description(),
            version=RandomGenerator.version(),
            author=RandomGenerator.name(),
            license=random.choice(cls._SUPPORTED_LICENSES),
            python_version=random.choice(cls._SUPPORTED_PYTHON_VERSIONS),
        )
