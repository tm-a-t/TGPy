import logging
import sys
import tokenize
import traceback

from telethon.tl import TLObject

from tgpy import App
from tgpy.run_code import autoawait


def convert_result(result):
    if isinstance(result, TLObject):
        result = result.stringify()

    return result


def format_traceback():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_traceback = exc_traceback.tb_next.tb_next
    return traceback.format_exception(exc_type, exc_value, exc_traceback)


def apply_code_transformers(app: App, code: str) -> str:
    for _, transformer in app.api.code_transformers:
        try:
            code = transformer(code)
        except Exception:
            logger = logging.getLogger(__name__)
            logger.exception(
                f'Error while applying code transformer {transformer}',
                exc_info=True,
            )
            raise
    try:
        code = autoawait.pre_transform(code)
    except tokenize.TokenError:
        pass
    return code
