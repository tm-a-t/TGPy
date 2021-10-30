# Code detection

## Why auto-detection?

TGPy is designed for running code snippets sequentially and frequently. Bot-like commands 
(such as `/run print('Hello World')`) would break the workflow. 

That's why TGPy automatically detects your messages with syntactically correct Python code and evaluates it.

It turns out that regular text messages aren't often identified as code. TGPy ignores too simple expressions.

Although, optional disabling of auto-detection might be added in the future.

## Simple expressions

Simple names and constants are ignored. If you want to get some variable value, use `return variable`.

In future updates some other simple expressions will be ignored, too.

## Cancel evaluation

Change the message with evaluated code to the original with the `cancel` command.

`cancel` edits back your latest TGPy message in current chat (if it's in 10 latest messages).

`cancel` can be also used in reply to a specific TGPy message.

## Prevent evaluation

If you write `//` in the beginning in your message, the code will be not evaluated. The `//` prefix will be deleted.
