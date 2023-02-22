<div align="center" style="width: 50%">

<h3>
<a href="https://tgpy.tmat.me">
<img alt="TGPy Logo" src="guide/docs/assets/TGPy.png" width=280>
</a>
 
Runs Python code snippets<br>within your Telegram messages
</h3>

<h6></h6>
  
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tgpy?style=flat-square)](https://pypi.org/project/tgpy/)
[![PyPI](https://img.shields.io/pypi/v/tgpy?style=flat-square&color=9B59B6)](https://pypi.org/project/tgpy/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tgpy/tgpy?style=flat-square&label=docker&sort=semver&color=9B59B6)](https://hub.docker.com/r/tgpy/tgpy)
[![Open issues](https://img.shields.io/github/issues-raw/tm-a-t/TGPy?style=flat-square)](https://github.com/tm-a-t/TGPy/issues)
[![Docs](https://img.shields.io/website?style=flat-square&label=docs&url=https%3A%2F%2Ftgpy.tmat.me)](https://tgpy.tmat.me/)

</div>

<br>

Here are a few examples of how people use TGPy:

🧮 Run Python as an in-chat calculator

🔍 Search for song lyrics within a chat

🧹 Delete multiple messages with a command

📊 Find out the most active members in a chat

✏️ Instantly convert TeX to Unicode in messages:<br>For example, `x = \alpha^7` becomes `x = α⁷`

## About

TGPy allows you to easily write and execute code snippets directly within your Telegram messages. Combine Telegram features with the full power of Python: Integrate with libraries and APIs. Create functions and TGPy modules to reuse code in the future. Set up code transformers and hooks to create custom commands and tweak Python syntax.

TGPy uses Telegram API through the [Telethon](https://github.com/LonamiWebs/Telethon) library.

## Quick Start

Python 3.10+ required. Install TGPy and connect it to your Telegram account:

```shell
> pip install tgpy
> tgpy
```

You’re ready now. Send Python code to any chat, and it will run. Change your message to change the result. [Read more on installation](http://tgpy.tmat.me/installation/)

## Learn

[🙂 Basics Guide](https://tgpy.tmat.me/basics/code/)

[😎 Extensibility Guide](https://tgpy.tmat.me/extensibility/context/)

[📗 Reference](https://tgpy.tmat.me/reference/builtins/)

[💬 Russian-Speaking Chat](https://t.me/tgpy_flood)


## Demo

https://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4

<br>

![A message processed with TGPy](guide/docs/assets/example.png)
_Finding out the number of premium users in a chat_

## Inspiration

TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. It was designed for running single-use scripts and reusing code flexibly. You can think of TGPy as a userbot for programmers.

## Credits

TGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), a Python library to interact with Telegram API.

Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

## License

This project is licensed under the terms of the MIT license.
