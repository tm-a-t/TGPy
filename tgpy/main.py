import aiorun
import logging
from telethon import TelegramClient, errors

from tgpy import app, Config
from tgpy.console import console
from tgpy.handlers import add_handlers
from tgpy.hooks import HookType, Hook
from tgpy.utils import migrate_from_old_versions, SESSION_FILENAME

log = logging.getLogger(__name__)


def create_client():
    client = TelegramClient(str(SESSION_FILENAME), app.config.api_id, app.config.api_hash)
    client.parse_mode = 'html'
    return client


async def start_client():
    await app.client.start(
        phone=lambda: console.input('| Please enter your phone number: '),
        code_callback=lambda: console.input('| Please enter the code you received: '),
        password=lambda: console.input('| Please enter your 2FA password: ', password=True),
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
    console.print('│ Login successful!')
    app.config.save()


async def run_client():
    log.info('Starting TGPy...')
    await start_client()
    log.info('[bold]TGPy is running!', extra={'markup': True})
    await Hook.run_hooks(HookType.onstart)
    await app.client.run_until_disconnected()


async def _main():
    migrate_from_old_versions()

    app.config = Config.load()
    if not (app.config.api_id and app.config.api_hash):
        await initial_setup()
    else:
        app.client = create_client()

    add_handlers()
    await run_client()


def main():
    aiorun.run(_main(), stop_on_unhandled_errors=True)
