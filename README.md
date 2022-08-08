# TGPy

_Run Python code right in your Telegram messages_

![PyPI](https://img.shields.io/pypi/v/tgpy)
![Docker Image Version (latest semver)](https://img.shields.io/docker/v/tgpy/tgpy?label=docker&sort=semver)
![Open issues](https://img.shields.io/github/issues-raw/tm-a-t/TGPy)
![Docs](https://img.shields.io/website?label=docs&url=https%3A%2F%2Ftgpy.tmat.me)
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/tgpy) -->

TGPy is a tool for running Python expressions and Telegram API scripts, built on top of [Telethon](https://github.com/LonamiWebs/Telethon).

- Do Python calculations in dialogs
- Use code to send messages, save files, analyze chats and more
- Set up functions to automate your Telegram actions

## Getting started

Python 3.9+ required. Install TGPy and connect it to your Telegram account:

```shell
> pip install tgpy
> tgpy
```

You’re ready now. Send Python code to any chat, and it will run. Change your message to change the result.

Details on installation: http://tgpy.tmat.me/installation/

https://user-images.githubusercontent.com/38432588/181266550-c4640ff1-71f2-4868-ab83-6ea3690c01b6.mp4

## New TGPy docs

**[Basics Guide:](http://tgpy.tmat.me/basics/code/)** All you need to know to start using TGPy.

**[Extensibility Guide:](http://tgpy.tmat.me/extensibility/context/)** Special features for advanced usage.

**[Reference:](http://tgpy.tmat.me/reference/builtins/)** List of TGPy objects and settings.

## Inspiration

TGPy is inspired by [FTG](https://gitlab.com/friendly-telegram/friendly-telegram) and similar userbots. However, the key concept is different: TGPy is totally based on usage of code in Telegram rather than plugging extra modules. This leads both to convenience of single-use scripts and reusage flexibility.

## Credits

TGPy is built on [Telethon](https://github.com/LonamiWebs/Telethon), which allows to integrate Telegram features in Python code.

Basic code transformation (such as auto-return of values) is based on [meval](https://github.com/penn5/meval).

## License

This project is licensed under the terms of the MIT license.
