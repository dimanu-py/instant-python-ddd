from collections.abc import Iterator

from instant_python.initialize.domain.node import Directory, File, Node, NodeType
from instant_python.shared.application_error import ApplicationError


class ProjectStructure:
    def __init__(self, nodes: list[Node]) -> None:
        self._nodes = nodes

    @classmethod
    def from_raw_structure(cls, structure: list[dict]) -> "ProjectStructure":
        nodes = cls._build_project_structure(structure)
        cls._ensure_pyproject_file_is_present(nodes)
        return cls(nodes=nodes)

    def flatten(self) -> Iterator[Node]:
        for node in self._nodes:
            yield node
            if isinstance(node, Directory):
                yield from self._flatten_directory(node)

    @classmethod
    def _build_project_structure(cls, nodes: list[dict]) -> list[Node]:
        return [cls._build_node(node) for node in nodes]

    @classmethod
    def _build_node(cls, node: dict) -> Node:
        node_type = node["type"]
        name = node["name"]

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [cls._build_node(child) for child in children]
            return Directory(name=name, is_python_module=is_python_module, children=directory_children)
        elif node_type == NodeType.FILE:
            extension = node.get("extension", "")
            content = node.get("content", None)
            return File(name=name, extension=extension, content=content)
        else:
            raise UnknownNodeTypeError(node_type)

    @classmethod
    def _ensure_pyproject_file_is_present(cls, nodes: list[Node]) -> None:
        for node in nodes:
            if isinstance(node, File) and node.is_pyproject_toml():
                return
        raise MissingPyprojectTomlError()

    def __iter__(self) -> Iterator[Node]:
        return iter(self._nodes)

    def __len__(self) -> int:
        return len(self._nodes)

    def _flatten_directory(self, directory: Directory) -> Iterator[Node]:
        for child in directory:
            yield child
            if isinstance(child, Directory):
                yield from self._flatten_directory(child)


class UnknownNodeTypeError(ApplicationError):
    def __init__(self, node_type: str) -> None:
        super().__init__(message=f"Unknown node type: {node_type}")


class MissingPyprojectTomlError(ApplicationError):
    def __init__(self) -> None:
        super().__init__(
            message="Missing pyproject.toml file in project structure. Add the following "
            "to your project structure definition:\n"
            "- name: pyproject\n"
            "  type: file\n"
            "  extension: .toml"
        )
