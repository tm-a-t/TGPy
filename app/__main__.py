import aiorun

from app import main, client

aiorun.run(main(), loop=client.loop, stop_on_unhandled_errors=True)
