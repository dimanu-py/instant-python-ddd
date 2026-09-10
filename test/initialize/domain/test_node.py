from pathlib import Path

import pytest
from doublex import Spy
from doublex_expects import have_been_called, have_been_called_with
from expects import expect

from instant_python.initialize.domain.node import Directory, File
from instant_python.initialize.domain.project_writer import NodeWriter
from test.initialize.domain.mothers.node_mother import FileMother


@pytest.mark.unit
class TestFile:
    _EMPTY_CONTENT = ""
    _SOME_CONTENT = "print('Hello, World!')"
    _SOME_PROJECT_PATH = Path("my_project")
    _SOME_NAME = "sample"
    _SOME_EXTENSION = ".py"

    def setup_method(self) -> None:
        self._file_writer = Spy(NodeWriter)

    def test_should_create_empty_file(self) -> None:
        file = File(name=self._SOME_NAME, extension=self._SOME_EXTENSION, content=self._EMPTY_CONTENT)

        file.create(writer=self._file_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._file_writer.create_file).to(
            have_been_called_with(Path("my_project/sample.py"), self._EMPTY_CONTENT)
        )

    def test_should_create_file_with_content(self) -> None:
        file = File(name=self._SOME_NAME, extension=self._SOME_EXTENSION, content=self._SOME_CONTENT)

        file.create(writer=self._file_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._file_writer.create_file).to(
            have_been_called_with(Path("my_project/sample.py"), self._SOME_CONTENT)
        )


class TestDirectory:
    _PYTHON_MODULE_NAME = "awesome_module"
    _STANDARD_DIRECTORY_NAME = "docs"
    _SOME_PROJECT_PATH = Path("my_project")

    def setup_method(self) -> None:
        self._directory_writer = Spy(NodeWriter)

    def test_should_create_empty_directory(self) -> None:
        directory = Directory(name=self._STANDARD_DIRECTORY_NAME, is_python_module=False, children=[])

        directory.create(writer=self._directory_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._directory_writer.create_directory).to(have_been_called_with(Path("my_project/docs")))
        expect(self._directory_writer.create_file).to_not(have_been_called)

    def test_should_create_python_module(self) -> None:
        directory = Directory(name=self._PYTHON_MODULE_NAME, is_python_module=True, children=[])

        directory.create(writer=self._directory_writer, destination=Path("my_project"))

        expect(self._directory_writer.create_directory).to(have_been_called_with(Path("my_project/awesome_module")))
        expect(self._directory_writer.create_file).to(
            have_been_called_with(Path("my_project/awesome_module/__init__.py"))
        )

    def test_should_create_python_module_with_files_inside(self) -> None:
        files = [FileMother.empty() for _ in range(2)]
        directory = Directory(name=self._PYTHON_MODULE_NAME, is_python_module=True, children=files)

        directory.create(writer=self._directory_writer, destination=self._SOME_PROJECT_PATH)

        expect(self._directory_writer.create_directory).to(have_been_called_with(Path("my_project/awesome_module")))
        expect(self._directory_writer.create_file).to(have_been_called.exactly(3))
