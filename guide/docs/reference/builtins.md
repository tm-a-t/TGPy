# TGPy builtins

## Control functions

| Function          | Description                                                                           |
| ----------------- | ------------------------------------------------------------------------------------- |
| `#!python ping()`          | Return basic info about your TGPy instance. Use `ping()` to check if TGPy is running. |
| `#!python restart()`       | Restart TGPy.                                                                         |
| `#!python update()`        | Download the latest version of TGPy, update, and restart the instance.                |

## Telethon objects

| Object   | Description                                                                                                                                                       |
|--------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `#!python client` | The Telethon client. [See Telethon Client reference](https://docs.telethon.dev/en/latest/quick-references/client-reference.html)                                 |
| `#!python msg`    | The current message. [See Telethon Message reference](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message)                        |
| `#!python orig`   | Original message: the message you replied to. [See Telethon Message reference](https://docs.telethon.dev/en/latest/quick-references/objects-reference.html#message) |

!!! note

    TGPy fetches `orig` message only if your code uses the `orig` variable. That’s because it requires an additional
    request to Telegram API.

## Modules

[Read on modules](/extensibility/modules/)

| Object | Description |
| --- | --- |
| `#!python modules` | Object for module management. `str(modules)` lists saved modules. |
| `#!python modules.add(name: str, code: str)` | Add the given code as a module. If `code` isn’t specified, the code from the `orig` message will be added. |
| `#!python modules.remove(name: str)` | Remove the module named `name`. |

## Context

[Read on the `ctx` object](../extensibility/context.md)

| Object | Description |
| --- | --- |
| `#!python ctx.msg` | The message containing the code TGPy is evaluating at the moment |

## TGPy API object

| Object | Description |
| --- | --- |
| `#!python tgpy.add_code_transformer(name: str, transformer: Callable[[str], str])` | _To be documented_ |
| `#!python tgpy.code_transformers` | _To be documented_ |
| `#!python tgpy.variables` | Dictionary of saved variables |
| `#!python tgpy.constants` | Dictionary of constants<br>(`tgpy`, `ctx`, `client`) |
