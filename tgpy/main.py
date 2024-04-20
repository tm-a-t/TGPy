import asyncio
import functools
import logging
import os.path
import platform
import subprocess
import sys

import aiorun
import yaml
from rich.console import Console, Theme
from telethon import TelegramClient, errors
from yaml import YAMLError

from tgpy import app
from tgpy._handlers import add_handlers
from tgpy.api import DATA_DIR, MODULES_DIR, WORKDIR, config
from tgpy.modules import run_modules, serialize_module
from tgpy.utils import SESSION_FILENAME, create_config_dirs

logger = logging.getLogger(__name__)

theme = Theme(inherit=False)
console = Console(theme=theme)


async def ainput(prompt: str, password: bool = False):
    def wrapper(prompt, password):
        return console.input(prompt, password=password)

    return await asyncio.get_event_loop().run_in_executor(
        None, wrapper, prompt, password
    )


def create_client():
    device_model = None
    if sys.platform == 'linux':
        if os.path.isfile('/sys/devices/virtual/dmi/id/product_name'):
            with open('/sys/devices/virtual/dmi/id/product_name') as f:
                device_model = f.read().strip()
    elif sys.platform == 'darwin':
        device_model = (
            subprocess.check_output('sysctl -n hw.model'.split(' ')).decode().strip()
        )
    elif sys.platform == 'win32':
        device_model = ' '.join(
            subprocess.check_output('wmic computersystem get manufacturer,model')
            .decode()
            .replace('Manufacturer', '')
            .replace('Model', '')
            .split()
        )

    client = TelegramClient(
        str(SESSION_FILENAME),
        config.get('core.api_id'),
        config.get('core.api_hash'),
        device_model=device_model,
        system_version=platform.platform(),
        lang_code='en',
        system_lang_code='en-US',
        proxy=config.get('core.proxy', None),
    )
    client.parse_mode = 'html'
    return client


async def start_client():
    await app.client.start(
        phone=functools.partial(ainput, '| Please enter your phone number: '),
        code_callback=functools.partial(
            ainput, '| Please enter the code you received: '
        ),
        password=functools.partial(
            ainput, '| Please enter your 2FA password: ', password=True
        ),
    )


async def initial_setup():
    console.print('[bold #ffffff on #16a085] Welcome to TGPy ')
    console.print('Starting setup...')
    console.print()
    console.print('[bold #7f8c8d on #ffffff] Step 1 of 2 ')
    console.print(
        '│ TGPy uses Telegram API, so you\'ll need to register your Telegram app.\n'
        '│  [#1abc9c]1.[/] Go to https://my.telegram.org\n'
        '│  [#1abc9c]2.[/] Login with your Telegram account\n'
        '│  [#1abc9c]3.[/] Go to "API development tools"\n'
        '│  [#1abc9c]4.[/] Create your app. Choose any app title and short_title. You can leave other fields empty.\n'
        '│ You will get api_id and api_hash.'
    )
    success = False
    while not success:
        config.set('core.api_id', int(await ainput('│ Please enter api_id: ')))
        config.set('core.api_hash', await ainput('│ ...and api_hash: '))
        try:
            app.client = create_client()
            console.print()
            console.print('[bold #7f8c8d on #ffffff] Step 2 of 2 ')
            console.print('│ Now login to Telegram.')
            await app.client.connect()
            await start_client()
            success = True
        except (errors.ApiIdInvalidError, errors.ApiIdPublishedFloodError, ValueError):
            console.print(
                '│ [bold #ffffff on #ed1515]Incorrect api_id/api_hash, try again'
            )
        finally:
            if app.client:
                await app.client.disconnect()
                del app.client
    console.print('│ Login successful!')


def migrate_hooks_to_modules():
    old_modules_dir = DATA_DIR / 'hooks'
    if not old_modules_dir.exists():
        return
    for mod_file in old_modules_dir.iterdir():
        # noinspection PyBroadException
        try:
            if mod_file.suffix not in ['.yml', '.yaml']:
                continue
            try:
                with open(mod_file) as f:
                    module = yaml.safe_load(f)

                if 'type' in module:
                    del module['type']
                if 'datetime' in module:
                    module['priority'] = int(module['datetime'].timestamp())
                    del module['datetime']

                new_mod_file = mod_file.with_suffix('.py')
                with open(new_mod_file, 'w') as f:
                    f.write(serialize_module(module))
                mod_file.unlink()
                mod_file = new_mod_file
            except YAMLError:
                continue
        except Exception:
            pass
        finally:
            mod_file.rename(MODULES_DIR / mod_file.name)
    old_modules_dir.rmdir()


def migrate_config():
    if old_api_id := config.get('api_id'):
        config.set('core.api_id', int(old_api_id))
        config.unset('api_id')
    if old_api_hash := config.get('api_hash'):
        config.set('core.api_hash', old_api_hash)
        config.unset('api_hash')


async def _async_main():
    create_config_dirs()
    os.chdir(WORKDIR)
    migrate_hooks_to_modules()

    config.load()
    migrate_config()
    if not (config.get('core.api_id') and config.get('core.api_hash')):
        await initial_setup()

    logger.info('Starting TGPy...')
    app.client = create_client()
    add_handlers()
    await start_client()
    logger.info('TGPy is running!')
    await run_modules()
    await app.client.run_until_disconnected()


async def async_main():
    try:
        await _async_main()
    except Exception:
        logger.exception('TGPy failed to start')
        asyncio.get_event_loop().stop()


def main():
    aiorun.run(async_main())
