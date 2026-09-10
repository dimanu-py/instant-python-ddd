import json
import tempfile
from pathlib import Path

import pytest
from approvaltests import verify

from instant_python.initialize.infra.writer.file_system_project_writer import FileSystemProjectWriter
from test.initialize.domain.mothers.project_structure_mother import ProjectStructureMother


@pytest.mark.integration
class TestFileSystemProjectWriter:
    def test_should_create_standard_directory_in_file_system(self) -> None:
        project_structure = ProjectStructureMother.with_one_directory(name="standard_directory", is_python_module=False)
        writer = FileSystemProjectWriter()

        with tempfile.TemporaryDirectory() as project_dir:
            project_location_path = Path(project_dir)
            writer.write(project_structure, project_location_path)
            created_structure = self._read_folder_structure(project_location_path)

        verify(json.dumps(created_structure, indent=2))

    def test_should_create_python_module_in_file_system(self) -> None:
        project_structure = ProjectStructureMother.with_one_directory(name="awesome_module", is_python_module=True)
        writer = FileSystemProjectWriter()

        with tempfile.TemporaryDirectory() as project_dir:
            project_location_path = Path(project_dir)
            writer.write(project_structure, project_location_path)
            created_structure = self._read_folder_structure(project_location_path)

        verify(json.dumps(created_structure, indent=2))

    def test_should_create_file_in_file_system(self) -> None:
        project_structure = ProjectStructureMother.with_one_python_file(name="python_file")
        writer = FileSystemProjectWriter()

        with tempfile.TemporaryDirectory() as project_dir:
            project_location_path = Path(project_dir)
            writer.write(project_structure, project_location_path)
            created_structure = self._read_folder_structure(project_location_path)

        verify(json.dumps(created_structure, indent=2))

    def _read_folder_structure(self, path: Path) -> dict:
        structure = {}

        if not path.exists():
            return structure

        for child in sorted(path.iterdir(), key=lambda p: p.name):
            if child.is_dir():
                structure[f"{child.name}/"] = self._read_folder_structure(child)
            else:
                structure[child.name] = child.read_text()

        return structure
