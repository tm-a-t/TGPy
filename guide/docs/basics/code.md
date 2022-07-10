# Code run

## How to use TGPy

Open any chat, type some Python code and send it. It’s that simple.

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

If you want to keep the original message rather than run the code, send `cancel` after your message.

!!! tip
    
    You can experiment with TGPy in [Saved Messages](tg://resolve?domain=TelegramTips&post=242). Nobody else will see that ;)

## Power of Python

All Python possibilities are available, including **module imports** and **function definitions**. Moreover, you can use most of Telegram features, such as sending messages. You’ll learn more about them later in the guide.

Besides, TGPy provides additional features for simplifying your code.

### Reuse variables

Since defined variables are saved automatically, you can use the variables from previous messages:

```python
phrase = 'TGPy is awesome'

TGPy> None
```

```python
phrase.upper()

TGPy> 'TGPY IS AWESOME'
```

### Code result

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

!!! tip "Tip: How to get the previous calculation result"

    There’s the `_` variable for that:

    ```python
    2 + 2
    
    TGPy> 4
    ```
    
    ```python
    _ * 100
    
    TGPy> 400
    ```

You can also print values. The `print` function is redefined, so that the output is added to messages.

```python
print('Hello World!')

TGPy> Hello World!
```

Exceptions are also shown right in messages.

Long messages might be truncated because of Telegram limit of 4096 symbols per message.
