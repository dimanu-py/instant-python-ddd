from typing import ClassVar

from instant_python.initialize.domain.node import Directory, File, Node
from test.random_generator import RandomGenerator


class FileMother:
    _EMPTY_CONTENT = ""
    _PYTHON_EXTENSION = ".py"

    @classmethod
    def empty(cls, name: str | None = None) -> File:
        return File(
            name=name if name else RandomGenerator.word(),
            extension=cls._PYTHON_EXTENSION,
            content=cls._EMPTY_CONTENT,
        )


class DirectoryMother:
    _PYTHON_MODULE = True
    _EMPTY: ClassVar[list] = []

    @classmethod
    def without_children(cls, name: str | None = None, is_python_module: bool | None = None) -> Directory:
        return Directory(
            name=name if name else RandomGenerator.word(),
            is_python_module=is_python_module if is_python_module is not None else cls._PYTHON_MODULE,
            children=cls._EMPTY,
        )

    @classmethod
    def with_children(cls, children: list[Node]) -> Directory:
        return Directory(
            name=RandomGenerator.word(),
            is_python_module=cls._PYTHON_MODULE,
            children=children,
        )
