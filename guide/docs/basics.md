# Basics

Just send any Python code to any chat - and it'll be evaluated.
```python
2 + 2

TGPy> 4
```

```python
s = 0
for i in range(100):
    s += i
s

TGPy> 4950
```

Change your message to change the result.

If you want to keep the original message, send `cancel` after your message.
[Learn more about code detection](code_detection.md)

## Do anything

All Python possibilities are available, including module imports and function definitions.

TGPy uses [Telethon library](https://github.com/LonamiWebs/Telethon/) to interact with Telegram. You can use 
messages, chats and users in your code. Check out [Telethon documentation](https://docs.telethon.dev/en/latest/).

For example, to programmatically reply to the current message:

```python
msg.reply('Hello!')
```

You can use variables such as `msg` for current message object and `client` for Telethon client object.
[Learn more about TGPy builtins](builtins.md)

Variables defined by you are saved automatically, so you can use them in following messages.

```python
def f():
    return 'TGPy is awesome'

TGPy> None
```

```python
f()

TGPy> 'TGPy is awesome'
```

## Code result

You can explicitly return values in messages:
```python
x = 10 * 10
return x

TGPy> 100
```

Otherwise, all calculated values will be automatically returned:
```python
10 * 10
x = 2
x + 2

TGPy> [100, 4]
```

You can also print values. `print` function is redefined, so the output is added to messages.

```python
print('Hello World!')
return 'ok'

TGPy> 'ok'

Hello World!
```

Exceptions are also shown right in messages.

Long messages might be truncated because of Telegram limit of 4096 symbols per message.

## Asyncio

You can use `async`/`await` in your code. Also, all returned values are automatically awaited (if needed).

```python
import asyncio
asyncio.sleep(30)

TGPy> Running...
```