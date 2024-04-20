"""
    name: constants
    origin: tgpy://builtin_module/constants
    priority: 100
"""

import tgpy.api
from tgpy import app

tgpy.api.constants['ctx'] = app.ctx
tgpy.api.constants['client'] = app.client
tgpy.api.constants['exc'] = None

__all__ = []
