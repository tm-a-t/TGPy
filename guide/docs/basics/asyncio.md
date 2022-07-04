# Asyncio

## Not familiar with asyncio?

If you don’t know how to work with Python `async`/`await` keywords, check out the [official guide](https://docs.python.org/3/library/asyncio-task.html) first. You’ll need this to use TGPy functions.

## Asyncio in TGPy

You can use top-level `async`/`await` in the code:

```python
import asyncio

await asyncio.sleep(10)
print('Done!')
```


In addition, TGPy automatically awaits all returned values (if needed). Therefore, this will work as well:

```python
import asyncio

asyncio.sleep(10)
print('Done!')
```
