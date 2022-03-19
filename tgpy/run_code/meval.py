import ast
import inspect
from collections import deque
from importlib.abc import SourceLoader
from importlib.util import module_from_spec, spec_from_loader
from types import CodeType
from typing import Any, Iterator

from tgpy import app


def shallow_walk(node) -> Iterator:
    # Like ast.walk, but ignoring function definitions:
    # Recursively yield all descendant nodes except for function definitions in the tree starting at node
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        queue.extend(ast.iter_child_nodes(node))
        yield node


class MevalLoader(SourceLoader):
    source: bytes
    code: CodeType
    filename: str

    def __init__(self, source: str, code: CodeType, filename: str):
        self.source = source.encode('utf-8')
        self.code = code
        self.filename = filename

    def is_package(self, _):
        return False

    def get_filename(self, _):
        return self.filename

    def get_data(self, _):
        return self.source

    def get_code(self, _):
        return self.code


async def meval(
    str_code: str, origin: str, globs: dict, saved_variables: dict, **kwargs
) -> (dict, Any):
    kwargs.update(saved_variables)

    # noinspection PyProtectedMember
    str_code = app.api._apply_code_transformers(str_code)
    root = ast.parse(str_code, '', 'exec')

    code = root.body
    if not code:
        return {}, None

    # save `Expression` body (`Call`) so it can be used in return statements
    get_locals = ast.parse("__import__('builtins').locals()", '', 'eval').body

    code_has_return = False
    for node in shallow_walk(root):
        if not isinstance(node, ast.Return):
            continue
        code_has_return = True

        # replace return ... with return (__import__('builtins').locals(), [...])
        node.value = ast.Tuple(
            elts=[
                get_locals,
                ast.List(
                    elts=[node.value or ast.Constant(value='None')], ctx=ast.Load()
                ),
            ],
            ctx=ast.Load(),
        )
    if not code_has_return and isinstance(code[-1], ast.Expr):
        # replace last_line with return (__import__('builtins').locals(), last_line)
        code[-1] = ast.copy_location(
            ast.Return(
                value=ast.Tuple(
                    elts=[get_locals, code[-1].value or ast.Constant(value=None)],
                    ctx=ast.Load(),
                )
            ),
            code[-1],
        )

    # return (__import__('builtins').locals(), None)
    code.append(
        ast.copy_location(
            ast.Return(
                value=ast.Tuple(
                    elts=[get_locals, ast.Constant(value=None)],
                    ctx=ast.Load(),
                )
            ),
            code[-1],
        )
    )

    args = []
    for a in list(map(lambda x: ast.arg(x, None), kwargs.keys())):
        ast.fix_missing_locations(a)
        args += [a]
    args = ast.arguments(
        args=[],
        vararg=None,
        kwonlyargs=args,
        kwarg=None,
        defaults=[],
        kw_defaults=[None for i in range(len(args))],
    )
    args.posonlyargs = []
    fun = ast.AsyncFunctionDef(
        name='tmp', args=args, body=code, decorator_list=[], returns=None
    )
    ast.fix_missing_locations(fun)
    mod = ast.Module(body=[fun], type_ignores=[])

    # print(ast.unparse(mod))
    comp = compile(mod, origin, 'exec')
    loader = MevalLoader(str_code, comp, origin)
    py_module = module_from_spec(spec_from_loader(origin, loader, origin=origin))
    loader.exec_module(py_module)

    new_locs, ret = await getattr(py_module, 'tmp')(**kwargs)
    for loc in list(new_locs):
        if (
            loc in globs or loc in kwargs
        ) and loc not in saved_variables:
            new_locs.pop(loc)

    new_locs['_'] = ret
    return new_locs, ret
