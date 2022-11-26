import dataclasses
import logging
import random
import re
import string
import traceback
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from textwrap import dedent, indent
from typing import Iterator, Optional, Union

import yaml
from yaml import YAMLError

from tgpy import app
from tgpy.run_code import meval
from tgpy.run_code.utils import format_traceback
from tgpy.utils import MODULES_DIR, filename_prefix

logger = logging.getLogger(__name__)


def get_module_filename(name: Union[str, Path]) -> Path:
    name = Path(name)
    if name.suffix != '.py':
        name = name.with_suffix('.py')
    return MODULES_DIR / name


def delete_module_file(name: Union[str, Path]):
    get_module_filename(name).unlink()


def get_module_names() -> Iterator[str]:
    for file in MODULES_DIR.iterdir():
        if file.suffix != '.py':
            continue
        yield file.stem


def get_sorted_modules() -> 'list[Module]':
    modules = []

    for mod_name in get_module_names():
        # noinspection PyBroadException
        try:
            module = Module.load(mod_name)
        except Exception:
            logger.error(f'Error during loading module {mod_name!r}')
            logger.error(traceback.format_exc())
            continue
        modules.append(module)

    modules.sort(key=lambda mod: mod.priority)
    return modules


async def run_modules():
    for module in get_sorted_modules():
        # noinspection PyBroadException
        try:
            await module.run()
        except Exception:
            logger.error(f'Error during running module {module.name!r}')
            logger.error(''.join(format_traceback()))
            continue


DOCSTRING_RGX = re.compile(r'^\s*(?:\'\'\'(.*?)\'\'\'|"""(.*?)""")', re.DOTALL)
MODULE_TEMPLATE = '''
"""
{metadata}
"""
{code}
'''.strip()


def serialize_module(module: Union['Module', dict]) -> str:
    if isinstance(module, Module):
        module_dict = dataclasses.asdict(module)
    else:
        module_dict = module
    module_code = DOCSTRING_RGX.sub('', module_dict.pop('code')).strip()
    module_str_metadata = yaml.safe_dump(module_dict).strip()
    return MODULE_TEMPLATE.format(
        metadata=indent(module_str_metadata, ' ' * 4),
        code=f'{module_code}\n',
    )


def deserialize_module(data: str, name: Optional[str] = None) -> 'Module':
    name = name or f'<unknown module {"".join(random.choices(string.digits, k=8))}>'
    docstring_match = DOCSTRING_RGX.search(data)
    fallback_metadata = {
        'name': name,
        'origin': f'{filename_prefix}module/{name}',
        'priority': datetime.now().timestamp(),
    }
    if docstring_match:
        module_str_metadata = dedent(
            docstring_match.group(1) or docstring_match.group(2)
        ).strip()
        try:
            module_dict = yaml.safe_load(module_str_metadata)
        except YAMLError:
            logger.error(
                f'Error loading metadata of module {name!r}, stripping metadata'
            )
            module_dict = fallback_metadata
    else:
        module_dict = fallback_metadata
        logger.warning(f'No metadata found in module {name!r}')
    # to support debugging properly, module code is the whole file
    module_dict['code'] = data
    module = Module(**module_dict)
    return module


@dataclass
class Module:
    name: str
    code: str
    origin: str
    priority: int
    once: bool = False
    save_locals: bool = True

    @classmethod
    def load(cls, mod_name: str) -> 'Module':
        filename = get_module_filename(mod_name)
        with open(filename, 'r') as f:
            module = deserialize_module(f.read(), mod_name)
        if module.name != mod_name:
            raise ValueError(
                f'Invalid module name. Expected: {mod_name!r}, found: {module.name!r}'
            )
        return module

    def save(self):
        filename = get_module_filename(self.name)

        with open(filename, 'w') as f:
            f.write(serialize_module(self))

    async def run(self):
        new_variables, result = await meval(
            self.code,
            self.origin,
            globals(),
            app.api.variables,
            msg=None,
            print=lambda *args, **kwargs: None,
            **app.api.constants,
        )
        if self.save_locals:
            app.api.variables.update(new_variables)
        if self.once:
            delete_module_file(self.name)
