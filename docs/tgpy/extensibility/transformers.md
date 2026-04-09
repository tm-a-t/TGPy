---
description: Code transformers, AST transformers, and hooks are advanced TGPy API features that can control code evaluation.
---

# Transformers & hooks

TGPy API allows you to use TGPy internal features in your messages and modules.

```python
import tgpy.api
```

Code transformers, AST transformers, and exec hooks are TGPy API features that can control code evaluation.

Code transformers are most commonly used.

## Code transformers

With code transformers, you can transform the code before TGPy runs it.
This is useful for setting up prefix commands, syntax changes, and more.

Transformers are functions that take message text and return some modified text. Whenever you send a message, TGPy tries
to apply your code transformers to its text. If the final text is the valid Python code, it runs.

To create a transformer, you should define a function which takes a string and returns a new string — let’s call
it `func`. Then you should register it as following:

```python
tgpy.api.code_transformers.add(name, func)
```

::: info EXAMPLE

Say you want to run shell commands by starting your message with `.sh`, for example:

```shell title="Your message"
.sh ls
```

You can implement this feature by saving a code transformer to a module:

```python title="Your module"
import os
import subprocess
import tgpy.api

def shell(code):
    proc = subprocess.run([os.getenv("SHELL") or "/bin/sh", "-c", code], encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.stdout + (f"\n\nReturn code: {proc.returncode}" if proc.returncode != 0 else "")

def sh_trans(cmd):
    if cmd.lower().startswith(".sh "):
        return f"shell({repr(cmd[4:])})"
    return cmd

tgpy.api.code_transformers.add("shell", sh_trans)
```

Code by [@purplesyringa](https://t.me/purplesyringa)

:::

## AST transformers

AST transformers are similar to code transformers, but operate with abstract syntax trees instead of text strings.

Add an AST transformer:

```python
tgpy.api.ast_transformers.add(name, func)
```

First, TGPy applies code transformers. If the transformation result is valid Python code, AST transformers are then
applied.

## Exec hooks

Exec hooks are functions that run before the message is parsed and handled. Unlike transformers, they may edit
the message, delete it, and so on.

Exec hooks must have the following signature:

```python
async hook(message: Message, is_edit: bool) -> Message | bool | None
``` 

`is_edit` is True if you have edited the TGPy message
{.code-label}

An exec hook may edit the message using Telegram API methods or alter the message in place.

If a hook returns Message object or alters it in place, the object is used instead of the original one during the rest
of handling (including calling other hook functions). If a hook returns True or None, execution completes normally.
If a hook returns False, the rest of hooks are executed and then the handling stops without further message
parsing or evaluating.

Add a hook:

```python
tgpy.api.exec_hooks.add(name, func)
```

## Complete flow

![](/assets/tgpy/diagram.png)

## Managing

TGPy stores transformers and exec hooks in `TransformerStore` objects: `tgpy.api.code_transformers`,
`tgpy.api.ast_transformers` and `tgpy.api.exec_hooks`.

Each of them represents a list of tuples `(name, func)` or a dict in the form of `{name: func}`.

While TGPy applies exec hooks in the same order they are listed, transformers are applied in reverse order.
It's done so that the newly added transformers can emit code that uses features of an older transformer.

Some examples:

<TGPy>

```python
tgpy.api.code_transformers
```

```python
TransformerStore({'postfix_await': <function tmp.<locals>.code_trans at 0x7f2db16cd1c0>})
```

</TGPy>

```python
tgpy.api.code_transformers.remove('postfix_await')
del tgpy.api.code_transformers['postfix_await']
tgpy.api.code_transformers['test'] = func
tgpy.api.code_transformers.add('test', func)
tgpy.api.code_transformers.append(('test', func))
for name, func in tgpy.api.code_transformers:
    ...
list(tgpy.api.code_transformers) -> list[tuple[str, function]]
dict(tgpy.api.code_transformers) -> dict[str, function]
```

## Manual usage

Apply all your code transformers to a custom text:

```python
tgpy.api.code_transformers.apply(text)
```

Apply all your AST transformers to a custom AST:

```python
await tgpy.api.ast_transformers.apply(tree)
```

Apply all your exec hooks to a message:

```python
await tgpy.api.exec_hooks.apply(message, is_edit)
```

Returns False if any of the hooks returned False or a Message object that should be used instead
of the original one otherwise
{.code-label}

