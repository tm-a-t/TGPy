"""
name: star_imports
origin: tgpy://builtin_module/star_imports
priority: 300
"""

import ast

import tgpy.api


def unwrap_star_import(module_name: str) -> list[str]:
    # https://stackoverflow.com/a/41991139
    module = __import__(module_name, fromlist=['*'])
    if hasattr(module, '__all__'):
        names = module.__all__
    else:
        names = [name for name in dir(module) if not name.startswith('_')]
    return names


class StarImportsTransformer(ast.NodeTransformer):
    def visit_ImportFrom(self, node: ast.ImportFrom):
        node = self.generic_visit(node)
        if node.names[0].name == '*':
            try:
                # this has a downside of delaying the start
                # of message evaluation if the import takes a long time
                names = unwrap_star_import(node.module)
                node.names = [ast.alias(name) for name in names]
            except ImportError:
                pass
        return node


tgpy.api.ast_transformers.add('star_imports', StarImportsTransformer)

__all__ = []
