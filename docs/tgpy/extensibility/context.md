---
description: You can use TGPy Context object to refer to the active TGPy message, disable showing the output, or check if the code is running from a module.
---

# Context Data

The `ctx` object stores some information about the context of running the code.

## Current message

The `msg` object always refers to the message where it was used. For
instance, if you use `msg` inside a function, it will refer to the message that defined this function — even if later
you call it from another message. However, sometimes you need to define reusable functions that use the current
message.

Let’s say we want to define a `cat()` function which sends a cat picture to the chat where you use it. Somehow the
function must use the current chat. You can pass `msg` as an argument, but then it won’t be handy enough for you to call
the function. Instead, you may want to use `ctx.msg` variable.

`ctx.msg` always contains your TGPy message where the current code is running. With it, you can define `cat()` function
as follows:

```python
async def cat():
    cat_url = 'https://cataas.com/cat'  # URL for a cat image
    await ctx.msg.respond(file=cat_url)
```

## Original message

To get the message which `ctx.msg` replies to, use:

```python
original = await ctx.msg.get_reply_message()
```
 
::: info 
The shortcut `ctx.orig` is planned but not implemented yet.
:::

## Set manual output

Sometimes you want the code from a message to edit the message itself. However, after running the code TGPy
basically changes the message back to the code and the output.

To prevent TGPy editing the message, you should set:

```python
ctx.is_manual_output = True
```

## Other

`ctx.is_module` is True if the code runs from a module.
