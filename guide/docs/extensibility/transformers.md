# Transformers & hooks

TGPy API allows you to use TGPy internal features in your messages and modules.

```python
import tgpy.api
```

Transformers and hooks are API features that can control code evaluation.


## Code transformers

With code transformers, you can transform the code before TGPy runs it. This is useful for setting up custom commands, syntax changes, and more.

Transformers are functions that take message text and return some modified text. Whenever you send a message, TGPy tries to apply your code transformers to its text. If the final text is the valid Python code, it runs.

To create a transformer, you should define a function which takes a string and returns a new string — let’s call your function `transformer`. Then you should register it as following:

```python
tgpy.api.add_code_transformer(name, transformer)
```

!!! example

    Say you want to run shell commands by starting your message with `.sh`, for example:

    ```shell title="Your message"
    .sh ls
    ```

    You can implement this feature by saving a code transformer to a module:

    ```python title="Your module"
    import os
    import subprocess
    
    def shell(code):
        proc = subprocess.run([os.getenv("SHELL") or "/bin/sh", "-c", code], encoding="utf-8", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return proc.stdout + (f"\n\nReturn code: {proc.returncode}" if proc.returncode != 0 else "")
    
    def sh_trans(cmd):
        if cmd.lower().startswith(".sh "):
            return f"shell({repr(cmd[4:])})"
        return cmd
    
    tgpy.add_code_transformer("shell", sh_trans)
    ```

    Code by [Ivanq](https://t.me/Ivanq_SandS)


List of your code transformers:

```python
tgpy.api.code_transformers
```
This is the list of tuples `(name, transformer)`. TGPy applies transformers in the same order as they are listed.

You can use this list and change it. Particularly, to delete a code transformer, you should delete it from the list.


## AST transformers

AST transformers are similar to code transformers, but operate with abstract syntax trees instead of text strings.

<div class="tgpy-code-block">

```python
tgpy.api.add_ast_transformer(name, transformer)
```
<hr>
```python
tgpy.api.ast_transformers
```

</div>

First, TGPy applies code transformers. If the transformation result is valid Python code, AST transformers are then applied.


## Exec hooks

Exec hooks are functions that run before the message is parsed and handled. Unlike transformers, they may edit
the message, delete it, and so on.

Exec hooks must have the following signature:

```python
async hook(message: Message, is_edit: bool) -> Message | bool | None
``` 

<p class="code-label"><code>is_edit</code> is True if you have edited the TGPy message</p>

An exec hook may edit the message using Telegram API methods or alter the message in place.

If a hook returns Message object or alters it in place, the object is used instead of the original one during the rest
of handling (including calling other hook functions). If a hook returns True or None, execution completes normally.
If a hook returns False, the rest of hooks are executed and then the handling stops without further message
parsing or evaluating.

Add a hook:

```python
tgpy.api.add_exec_hook(name, hook)
```


## Using transformers and hooks manually

Apply all your code transformers to custom text:

```python
tgpy.api.apply_code_transformers(text)
```

Apply all your AST transformers to a custom AST:

```python
await tgpy.api.apply_ast_transformers(tree)
```

Apply all your exec hooks to a message:

```python
await apply_exec_hooks(message, is_edit)
```

<p class="code-label">Returns False if any of the hooks returned False or a Message object that should be used instead
of the original one otherwise</p>
