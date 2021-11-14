import logging

import aiorun
from telethon import TelegramClient

from app.app_config import load_config
from app.console import console
from rich.logging import RichHandler


logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt="[%X]", handlers=[RichHandler()])
log = logging.getLogger('rich')


class App:
    config = None
    client = None


app = App()

from app.handlers import set_handlers
from app.hooks import HookType, Hook


async def run_client():
    log.info('Starting TGPy...')
    await app.client.start(app.config.phone, password=lambda: console.input('2FA password: ', password=True))
    log.info('[bold]TGPy is running!', extra={'markup': True})
    await Hook.run_hooks(HookType.onstart)
    await app.client.run_until_disconnected()


def main():
    app.config = load_config()

    app.client = TelegramClient('TGPy', app.config.api_id, app.config.api_hash)
    app.client.parse_mode = 'html'

    set_handlers()

    aiorun.run(run_client(), loop=app.client.loop, stop_on_unhandled_errors=True)
