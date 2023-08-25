# TGPy

**Runs Python code snippets within your Telegram messages**

[![PyPI - Downloads](https://img.shields.io/pypi/dm/tgpy?style=flat-square)](https://pypi.org/project/tgpy/)
[![PyPI](https://img.shields.io/pypi/v/tgpy?style=flat-square&color=9B59B6)](https://pypi.org/project/tgpy/)
[![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tgpy/tgpy?style=flat-square&label=docker&sort=semver&color=9B59B6)](https://hub.docker.com/r/tgpy/tgpy)
[![Open issues](https://img.shields.io/github/issues-raw/tm-a-t/TGPy?style=flat-square)](https://github.com/tm-a-t/TGPy/issues)
[![Docs](https://img.shields.io/website?style=flat-square&label=docs&url=https%3A%2F%2Ftgpy.tmat.me)](https://tgpy.tmat.me/)

<br>

Guide: https://tgpy.tmat.me/guide

Recipes: https://tgpy.tmat.me/recipes

Discussion: https://t.me/tgpy_flood

<br>

https://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4

<br>


<!-- --8<-- [start:body] -->
<!-- Starting from here, the content is shared between the readme file and the docs homepage -->

## Quick Start

Python 3.10+ required. Install using pipx:

```shell
pipx install tgpy
tgpy
```

or Docker:

```shell
docker pull tgpy/tgpy
docker run -it --rm -v /tgpy_data:/data tgpy/tgpy
```

Then follow instructions to connect your Telegram account. 

More on installation: [https://tgpy.tmat.me/installation](https://tgpy.tmat.me/installation)

Next, learn TGPy basics: [https://tgpy.tmat.me/basics](https://tgpy.tmat.me/basics)

## Use Cases

Here are a few examples of how people use TGPy:

🧮 Run Python as an in-chat calculator

🔍 Search for song lyrics within a chat

🧹 Delete multiple messages with a command

📊 Find out the most active members in a chat

✏️ Instantly convert TeX to Unicode in messages:<br>For example, `x = \alpha^7` becomes `x = α⁷`

## About

TGPy allows you to easily write and execute code snippets directly within your Telegram messages. Combine Telegram
features with the full power of Python: Integrate with libraries and APIs. Create functions and TGPy modules to reuse
code in the future. Set up code transformers and hooks to create custom commands and tweak Python syntax.

TGPy uses Telegram API through the [Telethon](https://github.com/LonamiWebs/Telethon) library.

## Inspiration and Credits

TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key
concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. It was
designed for running single-use scripts and reusing code flexibly. You can think of TGPy as **a userbot for programmers
**.

We built TGPy with [Telethon](https://github.com/LonamiWebs/Telethon), a Python library to interact with Telegram API.
Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

TGPy Docs use [Material for MKDocs](https://squidfunk.github.io/mkdocs-material/) with custom CSS.

## License

This project is licensed under the terms of the MIT license.

<!-- --8<-- [end:body] -->
