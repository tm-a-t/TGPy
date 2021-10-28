import logging

from telethon import TelegramClient

import config

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]', level=logging.INFO)

client = TelegramClient('TGPy', config.api_id, config.api_hash)
client.parse_mode = 'html'

from app import handlers


def run():
    client.start(config.phone, password=lambda: input('2FA password: '))
    client.run_until_disconnected()
