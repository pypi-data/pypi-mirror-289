import ast
from collections import defaultdict
from pathlib import Path
from typing import Tuple

from toposort import toposort_flatten


def module_for_path(path: Path) -> str:
    # strip out .py at the end
    module = ".".join(path.parts)
    return module.rsplit(".", 1)[0]


class ImportDependencyVisitor(ast.NodeVisitor):
    def __init__(self, modules):
        self.deps = defaultdict(set)
        self._modules = modules

    def visit_Module(self, node):
        self._current = module_for_path(node.__file__)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module in self._modules:
            self.deps[self._current].add(node.module)
        self.generic_visit(node)

    def visit_Import(self, node):
        names = [n.name for n in node.names]
        for n in names:
            if n in self._modules:
                self.deps[self._current].add(n)
        self.generic_visit(node)


def get_dependencies(trees):
    modules = {module_for_path(node.__file__) for node in trees}
    visitor = ImportDependencyVisitor(modules)
    for t in trees:
        visitor.visit(t)
    for m in modules:
        if m not in visitor.deps:
            visitor.deps[m] = set()
    return visitor.deps


def toposort(trees) -> Tuple:
    deps = get_dependencies(trees)
    tree_dict = {module_for_path(node.__file__): node for node in trees}
    return tuple([tree_dict[t] for t in toposort_flatten(deps, sort=True)])
