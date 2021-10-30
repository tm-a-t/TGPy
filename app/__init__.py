import logging

from telethon import TelegramClient

import config

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]', level=logging.INFO)

client = TelegramClient('TGPy', config.api_id, config.api_hash)
client.parse_mode = 'html'

from app import handlers
from app.data.hooks import HookType, Hook


async def main():
    await client.start(config.phone, password=lambda: input('2FA password: '))
    await Hook.run_hooks(HookType.onstart)
    await client.run_until_disconnected()
