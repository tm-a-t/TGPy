---
description: Reference on built-in functions and objects.
---

# Builtins

## Control functions

| Function    | Description                                                                           |
|-------------|---------------------------------------------------------------------------------------|
| `ping()`    | Return basic info about your TGPy instance. Use `ping()` to check if TGPy is running. |
| `restart()` | Restart TGPy.                                                                         |
| `update()`  | Download the latest version of TGPy, update, and restart the instance.                |

## Telethon objects

| Object   | Description                                                                                                                                                         |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `client` | The Telethon client. [See Telethon Client reference](https://docs.telethon.dev/en/stable/quick-references/client-reference.html)                                    |
| `msg`    | The current message. [See Telethon Message reference](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html#message)                          |
| `orig`   | Original message: the message you replied to. [See Telethon Message reference](https://docs.telethon.dev/en/stable/quick-references/objects-reference.html#message) |

::: info
TGPy fetches `orig` message only if your code uses the `orig` variable. That’s because it requires an additional
request to Telegram API.
:::

## Modules

[Read on modules](../extensibility/modules)

| Object                              | Description                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| `modules`                           | Object for [module management](../extensibility/modules#manage-modules).                                   |
| `modules.add(name: str, code: str)` | Add the given code as a module. If `code` isn’t specified, the code from the `orig` message will be added. |
| `modules.remove(name: str)`         | Remove the module named `name`.                                                                            |

## Context

[Read on the `ctx` object](../extensibility/context.md)

| Object                 | Description                                                                              |
|------------------------|------------------------------------------------------------------------------------------|
| `ctx.msg`              | The message where the code is running.                                                   |
| `ctx.is_module`        | `True` if the code is running from a module.                                             |
| `ctx.is_manual_output` | Can be set to True to prevent the last message edit by TGPy so you can edit it yourself. |
