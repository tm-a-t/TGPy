import getpass
import logging

from telethon import TelegramClient

import config

logging.basicConfig(format='{levelname}:    {message}', style='{', level=logging.INFO)

client = TelegramClient('TGPy', config.api_id, config.api_hash)
client.parse_mode = 'html'

from app import handlers
from app.hooks import HookType, Hook


async def main():
    await client.start(config.phone, password=lambda: getpass.getpass('2FA password: '))
    await Hook.run_hooks(HookType.onstart)
    await client.run_until_disconnected()
