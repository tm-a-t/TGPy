import datetime as dt
import logging
import traceback
from enum import Enum
from pathlib import Path
from typing import Union

import yaml
from pydantic import BaseModel

from tgpy import app
from tgpy.run_code import meval
from tgpy.run_code.utils import format_traceback
from tgpy.run_code.variables import variables
from tgpy.utils import yaml_multiline_str, HOOKS_DIR

logger = logging.getLogger(__name__)


class HookType(str, Enum):
    onstart = 'onstart'


def get_hook_filename(name: Union[str, Path]) -> Path:
    name = Path(name)
    if name.suffix not in ['.yml', '.yaml']:
        name = name.with_suffix('.yml')
    return HOOKS_DIR / name


def delete_hook_file(name: Union[str, Path]):
    get_hook_filename(name).unlink()


def get_sorted_hooks(type_=None):
    hooks = []

    for file in HOOKS_DIR.iterdir():
        if file.suffix not in ['.yml', '.yaml']:
            continue
        hook_name = file.stem

        # noinspection PyBroadException
        try:
            hook = Hook.load(hook_name)
        except Exception:
            logger.error(f'Error during loading hook {hook_name!r}')
            logger.error(traceback.format_exc())
            continue
        if type_ is None or hook.type == type_:
            hooks.append(hook)

    hooks.sort(key=lambda hook: hook.datetime)
    return hooks


class Hook(BaseModel):
    name: str
    type: HookType
    once: bool
    save_locals: bool = True
    code: str
    origin: str
    datetime: dt.datetime

    @classmethod
    def load(cls, hook_name: str) -> 'Hook':
        filename = get_hook_filename(hook_name)
        with open(filename) as f:
            hook = Hook.parse_obj(yaml.safe_load(f))
        if hook.name != hook_name:
            raise ValueError(f'Invalid hook name. Expected: {hook_name!r}, found: {hook.name}')
        return hook

    def save(self):
        filename = get_hook_filename(self.name)
        data = self.dict()
        data['code'] = yaml_multiline_str(data['code'])

        with open(filename, 'w') as f:
            f.write(yaml.safe_dump(data))

    async def run(self):
        new_variables, result = await meval(
            self.code,
            self.origin,
            globals(),
            variables,
            client=app.client,
            msg=None,
            ctx=variables['ctx'],
            print=lambda *args, **kwargs: None,
        )
        if self.save_locals:
            variables.update(new_variables)
        if self.once:
            delete_hook_file(self.name)

    @classmethod
    async def run_hooks(cls, type_: HookType):
        for hook in get_sorted_hooks(type_):
            # noinspection PyBroadException
            try:
                await hook.run()
            except Exception:
                logger.error(f'Error during running hook {hook.name!r}')
                logger.error(''.join(format_traceback()))
                continue
