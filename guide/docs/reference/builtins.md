# TGPy builtins

## Control functions

### `ping()`

Return basic info about your TGPy instance. Use `ping()` to check if TGPy is running.

### `restart()`

Restart TGPy

### `update()`

Download the latest version and restart TGPy

---

## Telethon objects

### `msg`

The current
message [(see Telethon Message reference)](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message)

### `orig`

Original message: the message you reply
to [(see Telethon Message reference)](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message)

TGPy fetches `orig` message only if your code uses `orig` variable (because it requires an additional request to
Telegram API).

### `client`

The Telethon client [(see Telethon Client reference)](https://docs.telethon.dev/en/latest/quick-references/client-reference.html)

---

## Modules

[Read about using modules](/extensibility/modules/)

### `modules`

Object for module managing. `str` value is a list of saved modules

### `modules.add(name: str, code: str = None)`

Add the given code to modules. If `code` isn’t specified, the code from the `orig` message will be added.

### `modules.remove(name: str)`

Remove the module named `name`

---

## Context

[Read about using ctx object](../extensibility/context.md)

### `ctx.msg`

The last message where TGPy started running code

---

## TGPy API object

### `tgpy.add_code_transformer(self, name: str, transformer: Callable[[str], str])`

TODO

### `tgpy.code_transformers`

TODO

### `tgpy.variables`

Dictionary of saved variables

### `tgpy.constants`

Dictionary of constants (`tgpy`, `ctx`, `client`)
