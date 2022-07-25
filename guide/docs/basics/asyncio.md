# Asyncio

## Not familiar with asyncio?

To use TGPy features for Telegram (such as sending messages, getting chats, and so on), you should understand Python
asynchronous functions.

Modern Python versions support asynchronous functions. Basically, asynchronous function is a function that runs until
completion while not blocking other code parts.

Let’s say you need to use such function in your TGPy message. To do that, you should place the `await` keyword before:
otherwise, the function won’t run.

```python
result = await some_function()
```

This way the code snippet will be suspended until `some_function()` ends, but **TGPy itself won’t stop**. For instance,
the code from another message may run at the same time.

If you declare some function which uses asynchronous functions, your function must be asynchronous too. For that
use `async def` instead of `def`.

!!! note

    If you wish to learn more about Python `async`/`await`, you may:

    - Read the [explanation of how asyncio works](https://fastapi.tiangolo.com/async/#technical-details) by Tiangolo written for FastAPI
    - Or google anything else about it :)

## Asyncio in TGPy

TGPy allows using top-level `async`/`await` in the code:

```python
import asyncio

await asyncio.sleep(10)
print('Done!')
```

In addition, TGPy automatically awaits all returned values (if needed). Therefore, you may omit top-level `await`:

```python hl_lines="3"
import asyncio

asyncio.sleep(10)
print('Done!')
```
