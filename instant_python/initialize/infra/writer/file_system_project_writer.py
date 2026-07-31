from pathlib import Path

from instant_python.initialize.domain.project_structure import ProjectStructure
from instant_python.initialize.domain.project_writer import NodeWriter, ProjectWriter


class FileSystemNodeWriter(NodeWriter):
    def create_directory(self, path: Path) -> None:
        path.mkdir(parents=True, exist_ok=True)

    def create_file(self, path: Path, content: str | None = None) -> None:
        path.touch(exist_ok=True)
        if content is not None:
            path.write_text(content)


class FileSystemProjectWriter(ProjectWriter):
    def __init__(self) -> None:
        self._node_writer = FileSystemNodeWriter()

    def write(self, project_structure: ProjectStructure, destination: Path) -> None:
        for node in project_structure:
            node.create(writer=self._node_writer, destination=destination)
