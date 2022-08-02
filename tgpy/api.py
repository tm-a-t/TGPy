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


api = API()
