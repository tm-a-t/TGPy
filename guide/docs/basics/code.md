# Code run

Just send any Python code to any chat — and it will run.
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

If you want to keep the original message instead, send `cancel` after your message.

!!! tip
    
    You can experiment with TGPy in [Saved Messages](tg://resolve?domain=TelegramTips&post=242). Nobody else will see that ;)


## Power of Python

All Python possibilities are available, including module imports and function definitions.

Moreover, you can use most Telegram features in your code. Try this:

```python
msg.reply('Hello!')
```

This will reply to the current message with „Hello!“

## Variables

Since defined variables are saved automatically, you can use them in following messages:

```python
phrase = 'TGPy is awesome'

TGPy> None
```

```python
phrase.upper()

TGPy> 'TGPY IS AWESOME'
```

## Code result

You can explicitly return values in messages:
```python
x = 2 * 2
return x

TGPy> 4
```

Otherwise, all calculated values will be automatically returned:
```python
x = 10
x * 7
x + 20

TGPy> [70, 30]
```

??? tip "Tip: How to get the previous calculation result"

    There’s the `_` variable for that:

    ```python
    2 + 2
    
    TGPy> 4
    ```
    
    ```python
    _ * 100
    
    TGPy> 400
    ```

You can also print values. `print` function is redefined, thus the output is added to messages.

```python
print('Hello World!')

TGPy> Hello World!
```

Exceptions are also shown right in messages.

Long messages might be truncated because of Telegram limit of 4096 symbols per message.
