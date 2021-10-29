from app.run_code.utils import Context

variables = {}

ctx = Context()


def ping():
    return 'Pong!'


variables['ctx'] = ctx
variables['ping'] = ping

# other default variables might be here
