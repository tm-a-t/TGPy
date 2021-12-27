import logging
from typing import Any, Callable


class API:
    code_transformers: list[tuple[str, Callable[[str], str]]]
    variables: dict[str, Any]
    constants: dict[str, Any]

    def __init__(self):
        self.variables = {}
        self.constants = {}
        self.code_transformers = []

    def add_code_transformer(self, name: str, transformer: Callable[[str], str]):
        self.code_transformers.append((name, transformer))

    def _apply_code_transformers(self, code: str) -> str:
        for _, transformer in self.code_transformers:
            try:
                code = transformer(code)
            except Exception:
                logger = logging.getLogger(__name__)
                logger.exception(
                    f'Error while applying code transformer {transformer}',
                    exc_info=True,
                )
                raise
        return code


api = API()
