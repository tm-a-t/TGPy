---
description: Through TGPy API module you can use internal features such as internal config object and functions to parse and run code.
---

# Other API features

TGPy API allows you to use TGPy internal features in your messages and modules.

```python
import tgpy.api
```

## Config

`tgpy.api.config` provides you simple key-value store for any data.
The data, as well as some TGPy settings, is saved to <code>[tgpy/](../installation.md#data-storage)config.yml</code>.

```python
tgpy.api.config.get(key: str, default: JSON = None) -> JSON
```

```python
tgpy.api.config.set(key: str, value: JSON)
```

```python
tgpy.api.config.unset(key: str)
```

```python
tgpy.api.config.save()
```

Useful when modifying objects acquired via the <code>get</code> method
{.code-label}

## Code processing

You can use the following functions to parse and run code.

### Parse code

```python
async parse_code(text: str) -> ParseResult(is_code: bool, original: str, transformed: str, tree: AST | None)
```

Checks if the given text is code and gives AST and other info
{.code-label}

### Parse a message

```python
parse_tgpy_message(message: Message) -> MessageParseResult(is_tgpy_message: bool, code: str | None, result: str | None)
```

Splits Telethon message object into TGPy code and result (if present)
{.code-label}

### Run code

```python
async tgpy_eval(code: str, message: Message = None, *, filename: str = None) -> EvalResult(result: Any, output: str)
```

Runs code and gets the result and the output
{.code-label}
