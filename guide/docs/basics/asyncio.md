# Asyncio

## Not familiar with asyncio?

If you’re not familiar with Python `async`/`await` keywords, check out the [official guide](https://docs.python.org/3/library/asyncio-task.html) first. You’ll need this to use TGPy functions.

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
