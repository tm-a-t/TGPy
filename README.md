<div align="center">
<a href="https://tgpy.tmat.me">
<img alt="TGPy Logo" src="guide/docs/assets/TGPy.png" style="width: 70%">
</a>
  
### **Supercharge Telegram with Python**
  
[![PyPI](https://img.shields.io/pypi/v/tgpy?style=flat-square)](https://pypi.org/project/tgpy/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tgpy/tgpy?style=flat-square&label=docker&sort=semver)](https://hub.docker.com/r/tgpy/tgpy)
[![Open issues](https://img.shields.io/github/issues-raw/tm-a-t/TGPy?style=flat-square)](https://github.com/tm-a-t/TGPy/issues)
[![Docs](https://img.shields.io/website?style=flat-square&label=docs&url=https%3A%2F%2Ftgpy.tmat.me)](https://tgpy.tmat.me/)
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/tgpy) -->
</div>
  
<br>
<br>

Write Python code and run it right inside your Telegram messages. For example:

- Use it as an in-chat calculator.
- Search for song lyrics within a chat.
- Delete multiple messages with a command.
- Find out the most active members in a chat.
- Instantly convert TeX to Unicode in your messages: for example, `x = \alpha^7` becomes `x = α⁷`.

> TGPy uses Telegram API through [the Telethon library.](https://github.com/LonamiWebs/Telethon)

## Quick Start

Python 3.9+ required. Install TGPy and connect it to your Telegram account:

```shell
> pip install tgpy
> tgpy
```

You’re ready now. Send Python code to any chat, and it will run. Change your message to change the result. [Details on installation](http://tgpy.tmat.me/installation/)

## Learn

[🙂 Basics Guide](https://tgpy.tmat.me/basics/code/)

[😎 Extensibility Guide](https://tgpy.tmat.me/extensibility/context/)

[📗 Reference](https://tgpy.tmat.me/reference/builtins/)

[💬 Russian Chat](https://t.me/tgpy_flood)

## Demo

![A message processed with TGPy](guide/docs/assets/example.png)
_Finding out the number of premium users in a chat_

<br>

https://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4

## Inspiration

TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. This leads both to convenience of single-use scripts and reusage flexibility.

## Credits

TGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), which allows to integrate Telegram features in Python code.

Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

## License

This project is licensed under the terms of the MIT license.
