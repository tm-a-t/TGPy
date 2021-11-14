import getpass
import logging

import aiorun
from telethon import TelegramClient

from app.app_config import load_config

logging.basicConfig(format='{levelname}:    {message}', style='{', level=logging.INFO)


class App:
    config = None
    client = None


app = App()

from app.handlers import set_handlers
from app.hooks import HookType, Hook


async def run_client():
    await app.client.start(app.config.phone, password=lambda: getpass.getpass('2FA password: '))
    await Hook.run_hooks(HookType.onstart)
    await app.client.run_until_disconnected()


def main():
    app.config = load_config()

    app.client = TelegramClient('TGPy', app.config.api_id, app.config.api_hash)
    app.client.parse_mode = 'html'

    set_handlers()

    aiorun.run(run_client(), loop=app.client.loop, stop_on_unhandled_errors=True)
