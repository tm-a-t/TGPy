# forked from https://pypi.org/project/meval/

import ast
import inspect
from collections import deque
from copy import deepcopy
from importlib.abc import SourceLoader
from importlib.util import module_from_spec, spec_from_loader
from types import CodeType
from typing import Any, Iterator

from tgpy.api.parse_code import ParseResult


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


async def _meval(
    parsed: ParseResult, filename: str, saved_variables: dict, **kwargs
) -> (dict, Any):
    kwargs.update(saved_variables)

    root = deepcopy(parsed.tree)
    ret_name = '_ret'
    ok = False
    while True:
        if ret_name in kwargs.keys():
            ret_name = '_' + ret_name
            continue
        for node in ast.walk(root):
            if isinstance(node, ast.Name) and node.id == ret_name:
                ret_name = '_' + ret_name
                break
            ok = True
        if ok:
            break

    code = root.body
    if not code:
        return {}, None

    # _ret = []
    ret_decl = ast.Assign(
        targets=[ast.Name(id=ret_name, ctx=ast.Store())],
        value=ast.List(elts=[], ctx=ast.Load()),
    )
    ast.fix_missing_locations(ret_decl)
    code.insert(0, ret_decl)

    # __import__('builtins').locals()
    get_locals = ast.Call(
        func=ast.Attribute(
            value=ast.Call(
                func=ast.Name(id='__import__', ctx=ast.Load()),
                args=[ast.Constant(value='builtins')],
                keywords=[],
            ),
            attr='locals',
            ctx=ast.Load(),
        ),
        args=[],
        keywords=[],
    )

    if not any(isinstance(node, ast.Return) for node in shallow_walk(root)):
        for i in range(len(code)):
            if (
                not isinstance(code[i], ast.Expr)
                or i != len(code) - 1
                and isinstance(code[i].value, ast.Call)
            ):
                continue

            # replace ... with _ret.append(...)
            code[i] = ast.copy_location(
                ast.Expr(
                    ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id=ret_name, ctx=ast.Load()),
                            attr='append',
                            ctx=ast.Load(),
                        ),
                        args=[code[i].value],
                        keywords=[],
                    )
                ),
                code[-1],
            )
    else:
        for node in shallow_walk(root):
            if not isinstance(node, ast.Return):
                continue

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

    # return (__import__('builtins').locals(), _ret)
    code.append(
        ast.copy_location(
            ast.Return(
                value=ast.Tuple(
                    elts=[get_locals, ast.Name(id=ret_name, ctx=ast.Load())],
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
    comp = compile(mod, filename, 'exec')
    loader = MevalLoader(parsed.original, comp, filename)
    py_module = module_from_spec(spec_from_loader(filename, loader, origin=filename))
    loader.exec_module(py_module)

    new_locs, ret = await getattr(py_module, 'tmp')(**kwargs)
    for loc in list(new_locs):
        if (loc in kwargs or loc == ret_name) and loc not in saved_variables:
            new_locs.pop(loc)

    ret = [await el if inspect.isawaitable(el) else el for el in ret]
    ret = [el for el in ret if el is not None]

    if len(ret) == 1:
        ret = ret[0]
    elif not ret:
        ret = None

    new_locs['_'] = ret
    return new_locs, ret
