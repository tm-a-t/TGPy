import logging

import aiorun
import yaml
from telethon import TelegramClient, errors
from yaml import YAMLError

from tgpy import Config, app
from tgpy.builtin_functions import add_builtin_functions
from tgpy.console import console
from tgpy.handlers import add_handlers
from tgpy.modules import run_modules, serialize_module
from tgpy.utils import DATA_DIR, MODULES_DIR, SESSION_FILENAME, create_config_dirs

log = logging.getLogger(__name__)


def create_client():
    client = TelegramClient(
        str(SESSION_FILENAME), app.config.api_id, app.config.api_hash
    )
    client.parse_mode = 'html'
    return client


async def start_client():
    await app.client.start(
        phone=lambda: console.input('| Please enter your phone number: '),
        code_callback=lambda: console.input('| Please enter the code you received: '),
        password=lambda: console.input(
            '| Please enter your 2FA password: ', password=True
        ),
    )


async def initial_setup():
    console.print('[bold on bright_cyan] Welcome to TGPy ')
    console.print('Starting setup...')
    console.print()
    console.print('[bold black on white] Step 1 of 2 ')
    console.print(
        '│ TGPy uses Telegram API, so you\'ll need to register your Telegram app.\n'
        '│  [cyan]1.[/] Go to https://my.telegram.org\n'
        '│  [cyan]2.[/] Login with your Telegram account\n'
        '│  [cyan]3.[/] Go to "API development tools"\n'
        '│  [cyan]4.[/] Create your app. Choose any app title and short_title. You can leave other fields empty.\n'
        '│ You will get api_id and api_hash.'
    )
    success = False
    while not success:
        app.config.api_id = console.input('│ Please enter api_id: ')
        app.config.api_hash = console.input('│ ...and api_hash: ')
        try:
            app.client = create_client()
            console.print()
            console.print('[bold black on white] Step 2 of 2 ')
            console.print('│ Now login to Telegram.')
            await app.client.connect()
            await start_client()
            success = True
        except (errors.ApiIdInvalidError, errors.ApiIdPublishedFloodError, ValueError):
            console.print('│ [bold on red]Incorrect api_id/api_hash, try again')
        finally:
            if app.client:
                await app.client.disconnect()
                del app.client
    console.print('│ Login successful!')
    app.config.save()


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


async def _main():
    create_config_dirs()
    migrate_hooks_to_modules()

    app.config = Config.load()
    if not (app.config.api_id and app.config.api_hash):
        await initial_setup()

    log.info('Starting TGPy...')
    app.client = create_client()
    add_handlers()
    add_builtin_functions()
    await start_client()
    log.info('[bold]TGPy is running!', extra={'markup': True})
    await run_modules()
    await app.client.run_until_disconnected()


def main():
    aiorun.run(_main(), stop_on_unhandled_errors=True)
