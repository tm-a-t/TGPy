import getpass
import socket

from app.run_code.utils import Context

variables = {}

ctx = Context()


def ping():
    return f'Pong!\n' \
           f'Running on {getpass.getuser()}@{socket.gethostname()}'


variables['ctx'] = ctx
variables['ping'] = ping

# other default variables might be here
