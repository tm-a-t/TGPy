# Code detection

## Why use auto-detection?

TGPy is designed for running code snippets sequentially and frequently. Bot-like commands 
(such as `/run print('Hello World')`) would break the workflow. 

That's why TGPy automatically detects your messages with syntactically correct Python code and evaluates it.

It turns out that regular text messages aren't often identified as code. TGPy ignores too simple expressions.

Although, optional disabling of auto-detection might be added in the future.

## What is ignored?

TL;DR: Some simple expressions, which could be email addresses, URLs or several comma- or hyphen-separated words
(as described in [issue 4](https://github.com/tm-a-t/TGPy/issues/4))

??? note "More details"
    In this section, an **unknown** variable is one not present in `locals` — that is, which were not saved in previous messages and which are not built in TGPy (as `ctx`, `orig`, `msg` and `print` are)
    Unknown variables' attributes are also considered unknown
    
    **Ignored** expressions are expressions in the list below:

    * Constants like `1` or `"abcd"` and unknown variables 
    * Binary operations on unknown variables (recursively, i.e., `a - b -c` is also ignored in case `a`, `b`, `c` are unknown)
    * Unary operations on constants or unknown variables
    * Tuples of ignored expressions
    * Multiple ignored expressions (i.e. separated by `;` or newline)****


## Cancel evaluation

You can change the message with evaluated code to the original with the `cancel` command.

`cancel` edits back your latest TGPy message in current chat (if it's in 10 latest messages).

`cancel` can be also used in reply to a specific TGPy message.

## Prevent evaluation

If you write `//` in the beginning in your message, the code won't be evaluated. The `//` prefix will be deleted.
