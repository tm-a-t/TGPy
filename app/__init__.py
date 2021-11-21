import getpass
import logging

from telethon import TelegramClient

import config
from app.utils import DATA_DIR, migrate_from_old_versions

logging.basicConfig(format='{levelname}:    {message}', style='{', level=logging.INFO)

migrate_from_old_versions()
client = TelegramClient(str(DATA_DIR / 'TGPy'), config.api_id, config.api_hash)

from app import handlers
from app.hooks import HookType, Hook


async def main():
    await client.start(config.phone, password=lambda: getpass.getpass('2FA password: '))
    await Hook.run_hooks(HookType.onstart)
    await client.run_until_disconnected()
