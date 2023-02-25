"""
    name: compat
    origin: tgpy://builtin_module/compat
    priority: 800
"""

import sys

import tgpy.api
from tgpy._core import message_design


class MessageDesignCompatStub:
    @staticmethod
    def get_code(message):
        return tgpy.api.parse_tgpy_message(message).code

    @staticmethod
    def parse_message(message):
        return tgpy.api.parse_tgpy_message(message)

    @staticmethod
    async def edit_message(*args, **kwargs):
        return await message_design.edit_message(*args, **kwargs)


# noinspection PyTypeChecker
sys.modules['tgpy.message_design'] = MessageDesignCompatStub()


class RunCodeCompatStub:
    @staticmethod
    def apply_code_transformers(code):
        return tgpy.api.code_transformers.apply(code)


# noinspection PyTypeChecker
sys.modules['tgpy.run_code'] = RunCodeCompatStub()


class TGPyAPICompatStub:
    @staticmethod
    def add_code_transformer(name, transformer):
        tgpy.api.code_transformers.add(name, transformer)

    @property
    def constants(self):
        return tgpy.api.constants

    @property
    def variables(self):
        return tgpy.api.variables


tgpy.api.variables['tgpy'] = TGPyAPICompatStub()

__all__ = []
