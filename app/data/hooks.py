import logging
import os.path
import traceback
from enum import Enum

import yaml
from pydantic import BaseModel

from app import client
from app.run_code import meval
from app.run_code.variables import variables
from app.run_code.utils import format_traceback
from app.utils import get_base_dir, yaml_multiline_str

DATA_DIR = os.path.join(get_base_dir(), 'data')
HOOKS_DIR = os.path.join(DATA_DIR, 'hooks')
os.makedirs(HOOKS_DIR, exist_ok=True)

logger = logging.getLogger(__name__)


class HookType(str, Enum):
    onstart = 'onstart'


def get_hook_filename(name: str) -> str:
    if os.path.splitext(name)[1] not in ['.yml', '.yaml']:
        name += '.yml'
    return os.path.join(HOOKS_DIR, name)


class Hook(BaseModel):
    name: str
    type: HookType
    once: bool
    save_locals: bool = True
    code: str
    origin: str

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
            client=client,
            msg=None,
            ctx=variables['ctx'],
            print=lambda *args, **kwargs: None,
        )
        if self.save_locals:
            variables.update(new_variables)
        if self.once:
            os.remove(get_hook_filename(self.name))

    @classmethod
    async def run_hooks(cls, type_: HookType):
        for file in os.listdir(HOOKS_DIR):
            if os.path.splitext(file)[1] not in ['.yml', '.yaml']:
                continue
            hook_name = os.path.splitext(os.path.basename(file))[0]
            # noinspection PyBroadException
            try:
                hook = cls.load(hook_name)
            except Exception:
                logger.error(f'Error during loading hook {hook_name}')
                logger.error(traceback.format_exc())
                continue
            if hook.type != type_:
                continue
            # noinspection PyBroadException
            try:
                await hook.run()
            except Exception:
                logger.error(f'Error during running hook {hook_name}')
                logger.error(''.join(format_traceback()))
                continue
