---
description: TGPy runs code when you send it to any chat. It also supports all Python capabilities and has features for convenient usage.
---

# Running Code

## How to use TGPy

Open any chat, type some Python code and send it. It’s that simple.

<TGPy>

```python
2 + 2
```

```
4
```

</TGPy>

<TGPy>

```python
s = 0
for i in range(100):
    s += i
s
```

```
4950
```

</TGPy>

If you edit your message, TGPy will recalculate the result.

When TGPy mistakes your plain-text message for code, type [`cancel`](../reference/code-detection#cancel-evaluation) to
fix that.

::: tip

You can experiment with TGPy in [Saved Messages](tg://resolve?domain=TelegramTips&post=242). Nobody else will see that ;)

:::

## Power of Python

All Python features are available, including **module imports** and **function definitions**. Moreover, you can use
most of Telegram features, such as sending messages. You’ll learn more about them later in the guide.

## Code result

You can explicitly return values in messages:

<TGPy>

```python
x = 2 * 2
return x
```

```
4
```

</TGPy>

Otherwise, all computed values will be returned automatically:

<TGPy>

```python
x = 10
x * 7
x + 20
```

```
[70, 30]
```

</TGPy>

You can also print values. The `print` function is redefined so that the output is added to the message.

<TGPy>

```python
print('Hello World!')
```

```
Hello World!
```

</TGPy>

Exceptions are also shown right in the message.

::: info

Long messages might be truncated because of Telegram limit of 4096 symbols per message.

:::

## More tips

- TGPy saves the defined variables, so you use them in further messages
- The `_` variable contains the result of the previous message
- Edit the message to rerun it
