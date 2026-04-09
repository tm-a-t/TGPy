---
description: Automatic code detection is a unique TGPy design feature. In case of a false positive, you can escape code. You can also save a hook that disables auto-detection forever.
---

# Code detection

## Cancel evaluation

Sometimes TGPy processes a message when you don’t mean it. In this case TGPy usually shows a value or an error.

Send `cancel` to the chat to edit back your latest TGPy message (only if it’s one of the 10 latest in the chat).

You can also use `cancel` in reply to a specific TGPy message.


## Prevent evaluation

If you begin your message with `//`, the code won’t run. TGPy will delete the `//` prefix.


## Why use auto-detection?

We designed TGPy for writing code snippets quickly and sequentially. Bot-like commands, 
such as `/run print('Hello World')`, would break the workflow. That's why we made TGPy automatically detect
your messages with syntactically correct Python code.

It turns out that regular text messages are identified as code pretty rarely. In fact, TGPy ignores too simple
expressions.


::: details Ignored expressions
TL;DR: TGPy ignores some simple expressions, which could be email addresses, URLs or several comma- or hyphen-separated words
(as described in [issue 4](https://github.com/tm-a-t/TGPy/issues/4))

In this section, an **unknown** variable is one not present in `locals` — that is, one that was not saved in previous
messages and which is not built into TGPy (as `ctx`, `orig`, `msg` and `print` are). Unknown variables' attributes are
also considered unknown.

**Ignored** expressions are the expressions from the list below:

* Constants like `1` or `"abcd"` and unknown variables 
* Binary operations on unknown variables (recursively, i.e., `a - b -c` is also ignored in case `a`, `b`, or `c` are unknown)
* Unary operations on constants or unknown variables
* Tuples of ignored expressions
* Multiple ignored expressions (i.e. separated by `;` or newline)
:::

## Disable auto-detection

If you want to disable auto-detection, you can save the following [hook](../extensibility/transformers#exec-hooks) 
as a [module](../extensibility/modules).

```python
import re
import tgpy.api

CODE_RGX = re.compile(r'\.py[ \n]')  # regex for the messages that you want to run

def hook(msg, is_edit):
    if is_edit:
        return True
    if not CODE_RGX.match(msg.raw_text):
        return False
    msg.raw_text = CODE_RGX.sub('', msg.raw_text, count=1)
    return msg

tgpy.api.add_exec_hook('no_autodetect', hook)

__all__ = []
```