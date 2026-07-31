import random

from instant_python.initialize.domain.node import Directory, File, Node, NodeType
from instant_python.initialize.domain.project_structure import ProjectStructure
from test.initialize.domain.mothers.node_mother import DirectoryMother, FileMother


class ProjectStructureMother:
    _MIN_NODES = 1
    _MAX_NODES = 5
    _MAX_DEPTH = 3

    @classmethod
    def empty(cls) -> ProjectStructure:
        return ProjectStructure(nodes=[])

    @classmethod
    def any(cls) -> ProjectStructure:
        num_nodes = random.randint(cls._MIN_NODES, cls._MAX_NODES)
        nodes = [cls._create_random_node(depth=0) for _ in range(num_nodes)]
        return ProjectStructure(nodes=nodes)

    @classmethod
    def with_one_directory(cls, name: str, is_python_module: bool) -> ProjectStructure:
        return ProjectStructure(nodes=[DirectoryMother.without_children(name, is_python_module)])

    @classmethod
    def with_one_python_file(cls, name: str) -> ProjectStructure:
        return ProjectStructure(nodes=[FileMother.empty(name)])

    @classmethod
    def _create_random_node(cls, depth: int) -> Node:
        node_types = [NodeType.FILE, NodeType.DIRECTORY]

        if depth >= cls._MAX_DEPTH:
            node_type = NodeType.FILE
        else:
            node_type = random.choice(node_types)

        if node_type == NodeType.FILE:
            return cls._create_file_node()
        else:
            return cls._create_directory_node(depth)

    @classmethod
    def _create_file_node(cls) -> File:
        return FileMother.empty()

    @classmethod
    def _create_directory_node(cls, depth: int) -> Directory:
        num_children = random.randint(0, cls._MAX_NODES)
        children = [cls._create_random_node(depth + 1) for _ in range(num_children)]
        return DirectoryMother.with_children(children)
