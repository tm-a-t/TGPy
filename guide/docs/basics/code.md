---
description: TGPy runs code when you send it to any chat. It also supports all Python capabilities and has features for convenient usage.
---

# Running code

## How to use TGPy

Open any chat, type some Python code and send it. It’s that simple.

<div class="tgpy-code-block">
```python
2 + 2
```
<hr>
```
4
```
</div>

<div class="tgpy-code-block">
```python
s = 0
for i in range(100):
    s += i
s
```
<hr>
```
4950
```
</div>

If you edit your message, TGPy will recalculate the result.

When TGPy mistakes your plain-text message for code, type [`cancel`](/reference/code_detection/#cancel-evaluation) to
fix that.

!!! tip

    You can experiment with TGPy in [Saved Messages](tg://resolve?domain=TelegramTips&post=242). Nobody else will see that ;)

## Power of Python

All Python features are available, including **module imports** and **function definitions**. Moreover, you can use
most of Telegram features, such as sending messages. You’ll learn more about them later in the guide.

## Code result

You can explicitly return values in messages:

<div class="tgpy-code-block">
```python
x = 2 * 2
return x
```
<hr>
```
4
```
</div>

Otherwise, all computed values will be returned automatically:

<div class="tgpy-code-block">
```python
x = 10
x * 7
x + 20
```
<hr>
```
[70, 30]
```
</div>

You can also print values. The `print` function is redefined, so that the output is added to the message.

<div class="tgpy-code-block">
```python
print('Hello World!')
```
<hr>
```
Hello World!
```
</div>

Exceptions are also shown right in the message.

!!! note

    Long messages might be truncated because of Telegram limit of 4096 symbols per message.

## More tips

- TGPy saves the defined variables, so you use them in further messages
- The `_` variable contains the result of the previous message
- Edit the message to rerun it
