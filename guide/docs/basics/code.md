# Code run

## How to use TGPy

Open any chat, type some Python code and send it. It’s that simple.

<div class="tgpy-code-block">
```python
2 + 2
```
<hr>
```
TGPy> 4
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
TGPy> 4950
```
</div>

Edit your message to change the result.

If you want to keep the original message rather than run the code, send `cancel` after your message.

!!! tip

    You can experiment with TGPy in [Saved Messages](tg://resolve?domain=TelegramTips&post=242). Nobody else will see that ;)

## Power of Python

All Python possibilities are available, including **module imports** and **function definitions**. Moreover, you can use
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
TGPy> 4
```
</div>

Otherwise, all calculated values will be automatically returned:

<div class="tgpy-code-block">
```python
x = 10
x * 7
x + 20
```
<hr>
```
TGPy> [70, 30]
```
</div>

You can also print values. The `print` function is redefined, so that the output is added to messages.

<div class="tgpy-code-block">
```python
print('Hello World!')
```
<hr>
```
TGPy> Hello World!
```
</div>

Exceptions are also shown right in messages.

!!! note

    Long messages might be truncated because of Telegram limit of 4096 symbols per message.

## Other tips

- TGPy saves the defined variables, so you use them in further messages 
- Use the `_` variable as the result of the previous message expression
- Edit the message to rerun it
