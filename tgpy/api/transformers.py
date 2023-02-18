import ast
import logging
from typing import Awaitable, Callable, Generic, Iterator, Literal, TypeVar

from telethon.tl.custom import Message

from tgpy.api.utils import try_await

logger = logging.getLogger(__name__)

# code -> code
CodeTransformerRet = str
CodeTransformerFunc = Callable[
    [str], CodeTransformerRet | Awaitable[CodeTransformerRet]
]
# ast -> ast
AstTransformerRet = ast.AST
AstTransformerFunc = Callable[
    [ast.AST], AstTransformerRet | Awaitable[AstTransformerRet]
]
# message, is_edit -> code
ExecHookRet = Message | bool | None
ExecHookFunc = Callable[[Message, bool], ExecHookRet | Awaitable[ExecHookRet]]

TF = TypeVar('TF')


class _TransformerStore(Generic[TF]):
    def __init__(self):
        self._by_name = {}
        self._names = []

    def __iter__(self) -> Iterator[tuple[str, TF]]:
        for name in self._names:
            yield name, self._by_name[name]

    def __repr__(self):
        return f'TransformerStore({dict(self)!r})'

    def __len__(self):
        return len(self._names)

    def __getitem__(self, item: str | int) -> tuple[str, TF]:
        if isinstance(item, int):
            return self._names[item], self._by_name[self._names[item]]
        elif isinstance(item, str):
            return self._by_name[item]
        else:
            raise TypeError(f'Expected str or int, got {type(item)}')

    def __setitem__(self, key: str | int, value: TF | tuple[str, TF]):
        if isinstance(key, int) and isinstance(value, tuple):
            old_name = self._names[key]
            self._names[key] = value[0]
            del self._by_name[old_name]
            self._by_name[value[0]] = value[1]
        elif isinstance(key, str) and callable(value):
            if key not in self._by_name:
                self._names.append(key)
            self._by_name[key] = value
        else:
            raise TypeError(
                f'only `obj[str] = func` and `obj[int] = (str, func)` syntaxes are supported'
            )

    def add(self, name: str, func: TF):
        self._names.append(name)
        self._by_name[name] = func

    def append(self, val: tuple[str, TF]):
        return self.add(*val)

    def remove(self, key: str | int):
        if isinstance(key, str):
            del self._by_name[key]
            self._names.remove(key)
        elif isinstance(key, int):
            del self._by_name[self._names[key]]
            del self._names[key]
        else:
            raise TypeError(f'Expected str or int, got {type(key)}')

    def __delitem__(self, key: str | int):
        self.remove(key)


class CodeTransformerStore(_TransformerStore[CodeTransformerFunc]):
    async def apply(self, code: str) -> str:
        for _, transformer in reversed(self):
            try:
                code = await try_await(transformer, code)
            except Exception:
                logger.exception(
                    f'Error while applying code transformer {transformer}',
                    exc_info=True,
                )
                raise
        return code


class AstTransformerStore(_TransformerStore[AstTransformerFunc]):
    async def apply(self, tree: ast.AST) -> ast.AST:
        for _, transformer in reversed(self):
            try:
                tree = await try_await(transformer, tree)
            except Exception:
                logger.exception(
                    f'Error while applying AST transformer {transformer}',
                    exc_info=True,
                )
                raise
        return tree


class ExecHookStore(_TransformerStore[ExecHookFunc]):
    async def apply(
        self, message: Message, *, is_edit: bool
    ) -> Message | Literal[False]:
        res = True
        for _, hook in self:
            try:
                hook_ret = await try_await(hook, message, is_edit)
                if isinstance(hook_ret, Message):
                    message = hook_ret
                elif hook_ret is False:
                    res = False
            except Exception:
                logger.exception(
                    f'Error while running exec hook {hook}',
                    exc_info=True,
                )
                raise
        if res:
            return message
        return False


code_transformers = CodeTransformerStore()
ast_transformers = AstTransformerStore()
exec_hooks = ExecHookStore()

__all__ = [
    'CodeTransformerFunc',
    'AstTransformerFunc',
    'ExecHookFunc',
    'code_transformers',
    'ast_transformers',
    'exec_hooks',
]
