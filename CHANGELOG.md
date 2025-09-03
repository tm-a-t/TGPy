# CHANGELOG


## v0.19.1 (2025-09-03)

### Bug Fixes

- **Telethon**: Fix layer update
  ([`4e4ff18`](https://github.com/tm-a-t/TGPy/commit/4e4ff18e17a1c1dcd9a1fd0aee2e5b3c00b5b7db))


## v0.19.0 (2025-09-03)

### Features

- **Telethon**: Layer 214
  ([`d0baf57`](https://github.com/tm-a-t/TGPy/commit/d0baf57829d3ed4312b32add85a8b54acc92aa29))


## v0.18.1 (2025-06-30)

### Bug Fixes

- Enforce utf-8 encoding when loading modules. Fixes #59
  ([#60](https://github.com/tm-a-t/TGPy/pull/60),
  [`399056c`](https://github.com/tm-a-t/TGPy/commit/399056ce3d0ac49c2a60cfb3766e3d466cedd110))

- Use Get-CimInstance when wmic is not present ([#58](https://github.com/tm-a-t/TGPy/pull/58),
  [`0091fe1`](https://github.com/tm-a-t/TGPy/commit/0091fe1d382e1da122f61aa5f072630d5a4050ec))

### Code Style

- Fix incorrect type hint
  ([`7a1bdb6`](https://github.com/tm-a-t/TGPy/commit/7a1bdb65decc4c74b668483eaa4c5a48acfdebd6))

### Continuous Integration

- Use trusted publishing for pypi
  ([`0384d46`](https://github.com/tm-a-t/TGPy/commit/0384d46bd528e24c78d909e3243ff81d05e1e7e7))


## v0.18.0 (2025-05-26)

### Bug Fixes

- Inspect.getsource now works properly. Fixes #55
  ([`24217a7`](https://github.com/tm-a-t/TGPy/commit/24217a7aed79ac7113d83af8a7aad7895c304912))

- Modules docs url
  ([`96663ac`](https://github.com/tm-a-t/TGPy/commit/96663ac822b4d59f14d9846f124f1b8a15125c41))

- Replying cancel to a message from another user no longer produces an error. Fixes #50
  ([`99c8e09`](https://github.com/tm-a-t/TGPy/commit/99c8e09de61605f86670f64773a5391c61cb0891))

### Build System

- Use upstream poetry
  ([`6102229`](https://github.com/tm-a-t/TGPy/commit/6102229676a90974f4fdefbe8477c5b319831be5))

- ci: use poetry dependency groups - build: loosen dependency requirements

- **docker**: Install poetry 2.0 from pypi
  ([`6af4028`](https://github.com/tm-a-t/TGPy/commit/6af40282c5a472f956b68f7ca404999756889403))

### Chores

- Add .vscode and *.iml to .gitignore
  ([`7bfef78`](https://github.com/tm-a-t/TGPy/commit/7bfef78919def6e18e07582e27dc4440704d6bf4))

### Code Style

- **python**: Replace black and isort with ruff
  ([`460afcb`](https://github.com/tm-a-t/TGPy/commit/460afcb7ac745001bac88a65ede7c9ea2256be0f))

Co-authored-by: Gleb Smirnov <glebsmirnov0708@gmail.com>

### Continuous Integration

- **fmt**: Use nix and treefmt for formatting and CI
  ([`b2f19e9`](https://github.com/tm-a-t/TGPy/commit/b2f19e956baca3e66aa467519ab76dd52377115b))

### Documentation

- Fix creation/modification dates
  ([`61f30b9`](https://github.com/tm-a-t/TGPy/commit/61f30b9c6bc734dbb245868f5193ee8d9afb1275))

### Features

- Add fixes for Apple and Android clients to std. Closes #54
  ([`3369104`](https://github.com/tm-a-t/TGPy/commit/3369104cdce8badcdfcf111e06000cc59989c4ef))

- Add star import fix to std
  ([`0fcac58`](https://github.com/tm-a-t/TGPy/commit/0fcac585e148b37514f5a678e2997c64c91998d8))

- Allow ast transformers to be NodeTransformer subclasses
  ([`835600b`](https://github.com/tm-a-t/TGPy/commit/835600bf3e81c260f238b1cfff7b545fd202d251))

- Tgpy.dev 🥺
  ([`cbc35e8`](https://github.com/tm-a-t/TGPy/commit/cbc35e8449e59bbf0bd78b554a22ed8fa3b646f4))

- **Telethon**: Layer 201
  ([`17a19a4`](https://github.com/tm-a-t/TGPy/commit/17a19a488efbbea8389d4403684c3b2f07028894))


## v0.17.1 (2024-12-21)

### Bug Fixes

- **build**: Fix docker build
  ([`8afb6f6`](https://github.com/tm-a-t/TGPy/commit/8afb6f6b0cede378bb8c6d4d3fef7a8c130cd967))


## v0.17.0 (2024-12-21)

### Bug Fixes

- **ci**: Fix semantic release config
  ([`98db29c`](https://github.com/tm-a-t/TGPy/commit/98db29c69054f0dfdaee0c91e5d8bdf27a4759c3))

- **docker**: Fix restart() failing to start tgpy in docker
  ([`5fcd14c`](https://github.com/tm-a-t/TGPy/commit/5fcd14cc33a4c525cbf096443f67ef1e15ac7c84))

### Build System

- **nix**: Make build use rev from nix
  ([`f7dfdde`](https://github.com/tm-a-t/TGPy/commit/f7dfdded228bbdd59728b98d6fb03b960f2fc93a))

- **nix**: Update flake.lock
  ([`aaa7591`](https://github.com/tm-a-t/TGPy/commit/aaa7591e1ab9078d7315507f5317bf97900ed4a5))

- Update nixpkgs in flake.lock - Fix nix evaluation - Update poetry dependencies

### Chores

- Format .nix files
  ([`bac06a8`](https://github.com/tm-a-t/TGPy/commit/bac06a8dc7da0362983809870d83e30539b868d8))

### Features

- Switch to PEP621 compliant pyproject.toml and pyproject.nix
  ([`7c20075`](https://github.com/tm-a-t/TGPy/commit/7c200755d3c90c560a99b5836e663f6453aa941f))

- Rewrite pyproject.toml to be PEP621 compliant - Update flake.nix to use pyproject.nix - Package
  poetry from master, use it in actions


## v0.16.0 (2024-09-26)

### Bug Fixes

- Ctx.is_manual_output is fixed
  ([`2e591f5`](https://github.com/tm-a-t/TGPy/commit/2e591f5ff84dd4434356772005e65474371acd55))

- Parse_tgpy_message no longer returns positive result for `TGPy error>` messages
  ([`818e47d`](https://github.com/tm-a-t/TGPy/commit/818e47dce360240b29e51676633d276480d9b8f8))

- Sending `cancel` in comments and topics now works correctly. Fix `cancel` throwing error when the
  message is not a TGPy message
  ([`1d3ba1a`](https://github.com/tm-a-t/TGPy/commit/1d3ba1ab583f7408f9f2854d22bfcf7fc7e96ae7))

### Code Style

- Reformat [skip ci]
  ([`2b09fb3`](https://github.com/tm-a-t/TGPy/commit/2b09fb378e8054e8379d9695b707ed0d71151d71))

### Documentation

- Describe loading of API secrets from env in guide
  ([`eb2a023`](https://github.com/tm-a-t/TGPy/commit/eb2a0230d4e0096d74781579dc9682f7ed9effd9))

### Features

- Telegram API ID and hash now can be loaded from environment
  ([`9c22347`](https://github.com/tm-a-t/TGPy/commit/9c223473c507257d25a77ecea566d830965d7c8f))


## v0.15.1 (2024-05-06)

### Bug Fixes

- Config is no longer erased when it fails to save. Also, the config is saved synchronously now
  ([`df539a3`](https://github.com/tm-a-t/TGPy/commit/df539a3dd32d73528e9800e2efe7b2099a5aa4a4))

- Restart now works correctly when tgpy is not in PYTHONPATH (e.g. in a container)
  ([`16d3830`](https://github.com/tm-a-t/TGPy/commit/16d383079b1bd48dabad8c7c562e5835f595d915))

- The correct data directory is now used when TGPY_DATA is set to a relative path and restart is
  called
  ([`f483d6c`](https://github.com/tm-a-t/TGPy/commit/f483d6c1e9b0c1bc0f79f0a31f477637d163d696))


## v0.15.0 (2024-04-28)

### Continuous Integration

- Release hotfix
  ([`8572721`](https://github.com/tm-a-t/TGPy/commit/8572721a486f110561201a4b186dc8d8d7abf773))

- **guide**: Add guide dependencies to pyproject.toml, build guide using nix
  ([`8686aa0`](https://github.com/tm-a-t/TGPy/commit/8686aa0c8bec91a1587deac32af5dcb442da8f2c))

### Documentation

- Reset page scale back to normal
  ([`20ec126`](https://github.com/tm-a-t/TGPy/commit/20ec1266f03d9f5d0e87deba93bfdf1d43cb1b5d))

Bigger scale was rather an experimental change and I'm tired of how it looks :)

### Features

- Cd to DATA_DIR/workdir on tgpy start
  ([`f51dc84`](https://github.com/tm-a-t/TGPy/commit/f51dc8477ba116ad9132dd2a65c0f7630415c357))

- Real time progress feedback
  ([`8e85d7a`](https://github.com/tm-a-t/TGPy/commit/8e85d7a585f89c9c1dc0eba498390ad475e7c439))

When stdout.flush() or stderr.flush() is called, the current output will be displayed in the message
  that is being evaluated. The message with be updated at most once per 3 seconds.

- Stop running message execution on `cancel`, add `stop` command to only stop execution without
  blacklisting the message
  ([`547c1c6`](https://github.com/tm-a-t/TGPy/commit/547c1c6d158e113f9ca63c8d0b87eb69a527d6af))

- Truncate exceptions ([#39](https://github.com/tm-a-t/TGPy/pull/39),
  [`739fbbc`](https://github.com/tm-a-t/TGPy/commit/739fbbcdc2f96ed54a10620f87049b0107c14cc6))

- **Telethon**: Layer 179
  ([`010f4ef`](https://github.com/tm-a-t/TGPy/commit/010f4ef4b17b40f46a99119777f216d1ee79debd))

### Refactoring

- Reactions_fix.update_hash is now called in edit_message
  ([`7e9d683`](https://github.com/tm-a-t/TGPy/commit/7e9d6834486819ee5ae6666f174fcdd28d51586f))


## v0.14.1 (2024-03-09)

### Bug Fixes

- Use cryptg-anyos again, because there are no official cp312-aarch64 binaries
  ([`50ca341`](https://github.com/tm-a-t/TGPy/commit/50ca3417c3bd3418bd66a02c52f35e5cf7d83b11))


## v0.14.0 (2024-03-09)

### Bug Fixes

- Tgpy error when editing MessageService, e.g. when deleting all messages in pm or beating your high
  score in games
  ([`5d6fb5e`](https://github.com/tm-a-t/TGPy/commit/5d6fb5e9f0b6556163c90c327a4d2ac6afe62b96))

### Build System

- Build docker image on python 3.12
  ([`eec91a9`](https://github.com/tm-a-t/TGPy/commit/eec91a92699f619c2972d6add13dd717236f9345))

### Features

- **docker**: Run specified commands on container creation. This feature can be used for example to
  persist installed packages between updates
  ([`456f503`](https://github.com/tm-a-t/TGPy/commit/456f5035ef8f0900750acee2a901cfdcea2e28b6))


## v0.13.2 (2023-12-10)

### Bug Fixes

- Update telethon (fix draft constructor), update all dependencies
  ([`a2b6064`](https://github.com/tm-a-t/TGPy/commit/a2b60641af3a0cab9fef08e95e07447b6c61432a))


## v0.13.1 (2023-12-06)

### Bug Fixes

- Use official cryptg (prebuilt wheels for Python 3.12), bump telethon (fixes usage of Draft), set
  minimum python version to 3.10
  ([`9e49739`](https://github.com/tm-a-t/TGPy/commit/9e497391f83dc6b333a6752f221d1221ea3d6cdb))


## v0.13.0 (2023-12-05)

### Features

- Support proxy
  ([`cd6bc90`](https://github.com/tm-a-t/TGPy/commit/cd6bc9086a818c45ee129ace88a0662980ad6c92))


## v0.12.1 (2023-10-28)

### Bug Fixes

- **Telethon**: New layer fix
  ([`8145bd3`](https://github.com/tm-a-t/TGPy/commit/8145bd3c58371e047114e834e2fbdba2de7ec575))


## v0.12.0 (2023-10-28)

### Features

- **Telethon**: Update to layer 166
  ([`a18dc0d`](https://github.com/tm-a-t/TGPy/commit/a18dc0d663362b50dfe7827ebac6ea2971220248))


## v0.11.0 (2023-09-29)

### Features

- **Telethon**: Fixes for the new layer and many more fixes from upstream
  ([`800fcd5`](https://github.com/tm-a-t/TGPy/commit/800fcd5f9799e82ed8a85155afd1c884b22355d3))


## v0.10.0 (2023-09-25)

### Documentation

- Fix transformer example
  ([`8007b25`](https://github.com/tm-a-t/TGPy/commit/8007b2587046550937cc63f7e5cd66f86e928f29))

Fix shell commands example in documentation (#35)

---------

Co-authored-by: Artyom Ivanov <tmat.ivanov@gmail.com>

- Recipes and new homepage
  ([`28e8eba`](https://github.com/tm-a-t/TGPy/commit/28e8ebae6f57642ce2dea7a70d4bd0bcfee94dc0))

- Revert narrowing container
  ([`bb0bff9`](https://github.com/tm-a-t/TGPy/commit/bb0bff98b058041a62f45fed260bf1f42ce32900))

### Features

- **Telethon**: Layer 164
  ([`2d0c186`](https://github.com/tm-a-t/TGPy/commit/2d0c1865fad08c8ee1f511f6749a22ede7374641))


## v0.9.7 (2023-07-23)

### Bug Fixes

- Consistent colors in setup across all terminals
  ([`faa625b`](https://github.com/tm-a-t/TGPy/commit/faa625bd2f4543b08ea7af361c8217cf006303d2))


## v0.9.6 (2023-06-01)

### Bug Fixes

- Strip device model
  ([`a775cc5`](https://github.com/tm-a-t/TGPy/commit/a775cc5a6415e92d023c421578f31bdd57a7a88d))


## v0.9.5 (2023-06-01)

### Bug Fixes

- Try to fix session termination issue by setting device_model and system_version to real values
  from the system
  ([`44e1c3d`](https://github.com/tm-a-t/TGPy/commit/44e1c3d8faf17f52ec289c3b6c69ae44ed75271e))


## v0.9.4 (2023-05-05)

### Bug Fixes

- Initial setup can now be interrupted with ctrl+c
  ([`e6253c7`](https://github.com/tm-a-t/TGPy/commit/e6253c7573f1eed9bbaefe739a967181a9c932e9))

- Initial setup prompts now work properly
  ([`8713dff`](https://github.com/tm-a-t/TGPy/commit/8713dff2f216bdadb9b07269c68f909b6867f681))

### Code Style

- Reformat [skip ci]
  ([`d33b9f4`](https://github.com/tm-a-t/TGPy/commit/d33b9f4ffa404708a50ed7643c0e6265df4f40bc))

### Continuous Integration

- Fix manual release workflow trigger
  ([`f44d8a3`](https://github.com/tm-a-t/TGPy/commit/f44d8a3ed5095bae093bd8b4eb26e55175e904ee))


## v0.9.3 (2023-02-25)

### Bug Fixes

- Deleting message no longer produces an error
  ([`ef317d9`](https://github.com/tm-a-t/TGPy/commit/ef317d98b9e817843eca8f0756147855217ccb3b))


## v0.9.2 (2023-02-25)

### Bug Fixes

- Message editing bug
  ([`3d1d566`](https://github.com/tm-a-t/TGPy/commit/3d1d566864381ea939143fae3fad607e03b5a548))


## v0.9.1 (2023-02-25)

### Bug Fixes

- Update from older versions
  ([`df11e8b`](https://github.com/tm-a-t/TGPy/commit/df11e8b0b8801b7c0e47f29b173964a7b63fa887))

### Chores

- Fix changelog
  ([`87438a4`](https://github.com/tm-a-t/TGPy/commit/87438a4b8a36317b0f36708559f09e3d668cb1ce))


## v0.9.0 (2023-02-25)

### Build System

- Use python-slim image instead of python-alpine
  ([`a34bd20`](https://github.com/tm-a-t/TGPy/commit/a34bd20e5a6bd97042c446faaa1b567669b6b32f))

### Documentation

- Document new features
  ([`f10b340`](https://github.com/tm-a-t/TGPy/commit/f10b340fc21cf5f7c492292621b0703fcad2e6a0))

- Non-flickery buttons on the index page
  ([`a783e1f`](https://github.com/tm-a-t/TGPy/commit/a783e1f0f26ab10796d98191336488f7cfda3c1b))

- Update changelog
  ([`21abcf0`](https://github.com/tm-a-t/TGPy/commit/21abcf04b2d239d3043f8dc31386e226502e1e96))

- Update pages
  ([`1a696e3`](https://github.com/tm-a-t/TGPy/commit/1a696e3c9e523bd0532f7a576aec196d6e6d447a))

- Update pages
  ([`937dc35`](https://github.com/tm-a-t/TGPy/commit/937dc35cd71216c474e2cb7de9056f61c07d1d5e))

- Update readme
  ([`e446344`](https://github.com/tm-a-t/TGPy/commit/e446344302aac9fafc057f9846dec7b9e902115d))

### Features

- Change in-message url to tgpy.tmat.me
  ([`8737ca9`](https://github.com/tm-a-t/TGPy/commit/8737ca92d600e0f57987426fa0ab9ba2fc655183))

- Move tokenize_string and untokenize_to_string to tgpy.api
  ([`7d8c3b2`](https://github.com/tm-a-t/TGPy/commit/7d8c3b2cadb46bd7447f9e908da1b9cadfe012e8))


## v0.8.0 (2023-02-15)

### Bug Fixes

- Don't stop on unhandled errors. They may happen when, for example, a module uses
  asyncio.create_task
  ([`3584f22`](https://github.com/tm-a-t/TGPy/commit/3584f223064902f8238f35715219289b6a16ea13))

### Features

- Wrap sys.stdout instead of print to capture output + properly use contextvars
  ([`7aa2015`](https://github.com/tm-a-t/TGPy/commit/7aa2015215ad621b405c6471add250bf11aa70c2))


## v0.7.0 (2023-02-05)

### Bug Fixes

- Handle entities properly when editing "//" message
  ([`6d989dc`](https://github.com/tm-a-t/TGPy/commit/6d989dc5349e026338857115d93f5c532f760578))

- Specify parse_mode in error handler to support markdown global parse mode
  ([`60cd81b`](https://github.com/tm-a-t/TGPy/commit/60cd81b9ca5cbb85ed72808e6ce3954bee455c3a))

- Use message.raw_text instead of message.text to detect //
  ([`a85b1c8`](https://github.com/tm-a-t/TGPy/commit/a85b1c834135f2b7c251ff8482afbab93f73002e))

### Features

- Update dependencies (layer 152)
  ([`234dc86`](https://github.com/tm-a-t/TGPy/commit/234dc86399c8545b07f55c1cddbcfbabcac2c372))

- Update telethon (new markdown parser, html parser fixes)
  ([`43dd76f`](https://github.com/tm-a-t/TGPy/commit/43dd76f0953e6ba2e77e9b5bc25f2748a36967ee))


## v0.6.2 (2023-01-22)

### Bug Fixes

- Fix IndentationError appearing for some non-code messages
  ([`599c84f`](https://github.com/tm-a-t/TGPy/commit/599c84f9ba4104d678476b07b090c54529246ab9))

- **docker**: Add /venv/bin to path
  ([`00be149`](https://github.com/tm-a-t/TGPy/commit/00be149b4ce827e97bb31b84f39cfa988a68d1ee))

### Documentation

- Update readme intro
  ([`c334669`](https://github.com/tm-a-t/TGPy/commit/c334669fcab8a6fc7a3f8330ae3217de21b97430))


## v0.6.1 (2023-01-06)

### Bug Fixes

- Update command saying "Already up to date" while in fact updating correctly
  ([`9b25fe6`](https://github.com/tm-a-t/TGPy/commit/9b25fe60809cfbb045bd605c0fa78f5ae19d57d0))

### Build System

- Update deps (telethon layer 151 and markup parsing/unparsing fixes)
  ([`d06f47e`](https://github.com/tm-a-t/TGPy/commit/d06f47e40acff01baf062adbffb126bff67ee0b2))

- Update telethon (layer 150)
  ([`b1379fc`](https://github.com/tm-a-t/TGPy/commit/b1379fc2c2ba540afee8ca6b524fb1a3136215ab))

### Chores

- Add workflow_dispatch event to main workflow
  ([`7812289`](https://github.com/tm-a-t/TGPy/commit/7812289775675a8cb5acb7ee3110ed034cb982af))

- Fix version
  ([`c783bfa`](https://github.com/tm-a-t/TGPy/commit/c783bfa6584190ca3ba07ddab14b029e0044a617))

### Code Style

- Reformat [skip ci]
  ([`9d76376`](https://github.com/tm-a-t/TGPy/commit/9d76376af266c536ff0a024adc365388d39849d4))

- Reformat [skip ci]
  ([`a542441`](https://github.com/tm-a-t/TGPy/commit/a542441794fadd5facb5a2b9c579a9583156d826))


## v0.6.0 (2022-11-26)

### Bug Fixes

- Ignore error when running code deletes the message itself
  ([`d022450`](https://github.com/tm-a-t/TGPy/commit/d0224502c5393dc423c9790e88fedc94bbb5afbf))

- Keep 'cancel' message when replying to other user (fixes #21)
  ([`057231d`](https://github.com/tm-a-t/TGPy/commit/057231d7a437d5ab4fca280b130714573904a67e))

### Build System

- Use cryptg-anyos, which provides prebuilt wheels for musllinux
  ([`7d85c71`](https://github.com/tm-a-t/TGPy/commit/7d85c718e46a1ed3896eaeada4fd2e32cab9b1b3))

### Code Style

- Reformat [skip ci]
  ([`bcf54a4`](https://github.com/tm-a-t/TGPy/commit/bcf54a48db3c954c769b8fe04cbb5dfb30354c2b))

- Reformat [skip ci]
  ([`9853be4`](https://github.com/tm-a-t/TGPy/commit/9853be43f77243b7eb483f923c26912456fac8be))

### Documentation

- Update readme
  ([`a321bbf`](https://github.com/tm-a-t/TGPy/commit/a321bbfe474e8ae97132a7f0f4d11c009495c482))

- add links to badges - change introduction

### Features

- Use MessageEntityPre with language set to 'python' to enable syntax highlighting on supported
  clients (e.g. WebZ). Closes #24
  ([`5de6ded`](https://github.com/tm-a-t/TGPy/commit/5de6ded579c237f0221b6223dfd18254a2ebb1cd))

### Refactoring

- Remove pydantic
  ([`6256c89`](https://github.com/tm-a-t/TGPy/commit/6256c894a85254e8dc2409f0961eee43beaa6d93))


## v0.5.1 (2022-08-09)

### Bug Fixes

- Compatibility with python 3.9
  ([`f3c0468`](https://github.com/tm-a-t/TGPy/commit/f3c046847f9d7f549586c829dbec74238f264ed2))

- Restart() now edits message properly
  ([`60afa44`](https://github.com/tm-a-t/TGPy/commit/60afa44e7002fa87a5c0d2adb60c2065e885f1ec))

### Chores

- Fix readme
  ([`769b903`](https://github.com/tm-a-t/TGPy/commit/769b903cb952687b9c198889256636d5fcf6d2a2))

### Continuous Integration

- Build docker image with proper tgpy version
  ([`d0f4969`](https://github.com/tm-a-t/TGPy/commit/d0f4969f5447b47385aab805296195edb8ef7bf7))

- Tag docker images by release versions
  ([`f8710c7`](https://github.com/tm-a-t/TGPy/commit/f8710c77b4f3d40bcdd43a6bc6f954a2ffb10243))


## v0.5.0 (2022-08-08)

### Bug Fixes

- Apply autoawait pre_transform after regular code transformers
  ([`fde6291`](https://github.com/tm-a-t/TGPy/commit/fde62914540d43da01a02e547f2e62516f7cf52e))

- Message markup for utf-16 (closes #10)
  ([`20f48bc`](https://github.com/tm-a-t/TGPy/commit/20f48bc8e08490e85ff68bfe6feb9997eb8cbb29))

- Parsing of modules with triple quotes in code
  ([`485166d`](https://github.com/tm-a-t/TGPy/commit/485166d5c513e196c0db760c468599d3c6ab9581))

- Setting/removing reaction no longer triggers reevaluation
  ([`cf6e64e`](https://github.com/tm-a-t/TGPy/commit/cf6e64e82d1823202941610274a4ff38955c5cf1))

however, when TGPy is restarted you will need to edit old messages twice to reevaluate

- Use custom telethon version without MessageBox as it's very buggy
  ([`9c7738e`](https://github.com/tm-a-t/TGPy/commit/9c7738e40cda69499974ceda711f56ca65782312))

### Build System

- Add guide dist directory to gitignore
  ([`40578e2`](https://github.com/tm-a-t/TGPy/commit/40578e2f2e069e47ca194fa3105e5d0a8b029d02))

- Add venv to .dockerignore
  ([`2f94d3c`](https://github.com/tm-a-t/TGPy/commit/2f94d3cf74648b1c601014509b9c18c3be232a91))

- Dockerize
  ([`f8cb28d`](https://github.com/tm-a-t/TGPy/commit/f8cb28dd54722c047934e41071cc32ddc6f81cdd))

### Code Style

- Reformat [skip ci]
  ([`373ee12`](https://github.com/tm-a-t/TGPy/commit/373ee12cfc7e1faa889dba4999d6f14aad10084d))

- Reformat [skip ci]
  ([`1204457`](https://github.com/tm-a-t/TGPy/commit/120445711a0aa64bf00480e270e4de258c2a0439))

### Continuous Integration

- Build docker image
  ([`9380141`](https://github.com/tm-a-t/TGPy/commit/938014176febd77488170b32026081fa95c5cdd2))

- Trigger main workflow on pyproject.toml and poetry.lock changes
  ([`30c08ce`](https://github.com/tm-a-t/TGPy/commit/30c08ce97659a5f896083777fd20e5f63e79c8df))

### Documentation

- Change readme assets. new video
  ([`d0b3565`](https://github.com/tm-a-t/TGPy/commit/d0b35657f4f98542eb6408fb2c21420e19034f5c))

- Fix some typos here and there in the guides ([#26](https://github.com/tm-a-t/TGPy/pull/26),
  [`9d6c8a8`](https://github.com/tm-a-t/TGPy/commit/9d6c8a83c054eb4e54866f120355c44de88458b2))

- Guide changes
  ([`b000c12`](https://github.com/tm-a-t/TGPy/commit/b000c12cbbbdaad5f2c02452dd6e2f9b9710e840))

- Guide changes
  ([`237a1cd`](https://github.com/tm-a-t/TGPy/commit/237a1cdd69cd5770d995f26305ae0d51d4db5dbd))

- Guide changes
  ([`43a0779`](https://github.com/tm-a-t/TGPy/commit/43a0779c45c0f01fa2c70ff8797332aa0b11a100))

- Guide changes
  ([`f432d30`](https://github.com/tm-a-t/TGPy/commit/f432d30a2a860f2a1969d9d7f9de55d34cdec140))

- Guide changes. many changes.
  ([`74ae524`](https://github.com/tm-a-t/TGPy/commit/74ae524b7fa5f554e02ace092fd9951663c78a95))

- Guide changes:
  ([`767473b`](https://github.com/tm-a-t/TGPy/commit/767473bdfdfebecc4e2998f0cc9b7bf7bdebecf9))

- Guide changes:
  ([`024bce3`](https://github.com/tm-a-t/TGPy/commit/024bce351a4784dc32cef66a7d6c4dcd146d2ffb))

- Guide changes:
  ([`9e7f832`](https://github.com/tm-a-t/TGPy/commit/9e7f832c5be8a0126efc1ae47afbbe6fc8ea9042))

- Guide color palette & guide changes
  ([`6320934`](https://github.com/tm-a-t/TGPy/commit/63209349449efe8ece23c4dcccce7585e24b1bd7))

- Guide text changes
  ([`903963a`](https://github.com/tm-a-t/TGPy/commit/903963a170ff5965c9044643c14b1ce41879cd15))

- Guide theme changes
  ([`33dcbb0`](https://github.com/tm-a-t/TGPy/commit/33dcbb0ae247e17b09d9deb817d3b7ba733d8fb9))

- New video on docs page
  ([`9abf1eb`](https://github.com/tm-a-t/TGPy/commit/9abf1eb9293313e22d68b57c3c1948365a9a7ed9))

- Readme video
  ([`59a2f12`](https://github.com/tm-a-t/TGPy/commit/59a2f121339f146dcb9b509450bdff8f1af36866))

- Readme video fix
  ([`383fe5b`](https://github.com/tm-a-t/TGPy/commit/383fe5bcfa8f9b1274b113ab426e1f08138dfdfd))

- Restructure guide
  ([`8cee429`](https://github.com/tm-a-t/TGPy/commit/8cee42932b69dc8b55098ae747e7c2d99306fa19))

- Update readme
  ([`a23c076`](https://github.com/tm-a-t/TGPy/commit/a23c0765d1f83f0cb41d8297d8218d8078d0a7d4))

- add badges - update project description

- Update readme
  ([`5569ccb`](https://github.com/tm-a-t/TGPy/commit/5569ccbb5fa601ff9b0c8cb4011dce5ea93eab9f))

### Features

- Allow to specify data directory via environment variable TGPY_DATA
  ([`4d769da`](https://github.com/tm-a-t/TGPy/commit/4d769daea76bc1abe86914487f9a80d3ea0eb2fb))

- Better version detection, ping() builtin improvements
  ([`265b83f`](https://github.com/tm-a-t/TGPy/commit/265b83f0c604b96ae740e06a32441b7e001bac1a))

- Distinguish between dev and release version by using IS_DEV_BUILD constant in tgpy/version.py.
  It's set to False only during release build process. - Allow version detection in docker container
  by using COMMIT_HASH constant in tgpy/version.py, which is set during docker build -
  utils.get_version() tries to get version from (in order): __version__ variable, commit hash from
  `git rev-parse`, commit hash from COMMIT_HASH constant - update() builtin now shows friendly
  message when: running in docker, git is not installed, installation method is unknown (not pypi
  package, not docker image, not git)

- Transform x.await into await x
  ([`6117421`](https://github.com/tm-a-t/TGPy/commit/6117421cc7b72c56dace006d2fc569edfe14b734))

- Use the latest telethon from v1.24 branch, update all dependencies
  ([`91894fc`](https://github.com/tm-a-t/TGPy/commit/91894fc6894e5e111baa469c3de372b46e62b049))


## v0.4.1 (2022-01-10)

### Bug Fixes

- **code detection**: Ignore messages like "fix: fix"
  ([`1b73815`](https://github.com/tm-a-t/TGPy/commit/1b73815928fdbdae3eae1202c01b4b53b9906ba4))


## v0.4.0 (2022-01-10)

### Bug Fixes

- Ctx.msg now always points to message from which code is executed
  ([`59acde9`](https://github.com/tm-a-t/TGPy/commit/59acde9ec7baef5ff130d6fb77d74c2981bd15e2))

- Data directory path on Windows
  ([`7d0e283`](https://github.com/tm-a-t/TGPy/commit/7d0e2835b8c2f5b6327b012a5c56035a63433ba9))

- Print now always writes to message from which code is executed
  ([`0e46527`](https://github.com/tm-a-t/TGPy/commit/0e46527446749dd691263069def260ae29453077))

- **code detection**: Ignore messages like "cat (no)" and "fix: fix"
  ([`75bb43e`](https://github.com/tm-a-t/TGPy/commit/75bb43eae71f9e024a3e7f299cd0614c860c2457))

### Code Style

- Reformat [skip ci]
  ([`769c4ca`](https://github.com/tm-a-t/TGPy/commit/769c4ca06f4c9ad1faa9054f1b7b842587234527))

### Continuous Integration

- Add isort
  ([`c03578c`](https://github.com/tm-a-t/TGPy/commit/c03578c1d1b7a463a2e853fe4d892cde3bd5c586))

- Black config in pyproject.toml
  ([`81ff388`](https://github.com/tm-a-t/TGPy/commit/81ff3881178df8e42650ef59e35b29c02a082873))

- Deploy guide to Netlify
  ([`52eb160`](https://github.com/tm-a-t/TGPy/commit/52eb1605951f8c95db90a6ed19021dc438815bc8))

- Don't trigger main workflow when guide workflow changes, fix cache key
  ([`91c7f9c`](https://github.com/tm-a-t/TGPy/commit/91c7f9cca9fbf911254afe436c713ee2934855ed))

- **guide**: Disable commit/pull request comments
  ([`a1c1a81`](https://github.com/tm-a-t/TGPy/commit/a1c1a81d36ce77a892879437c767277ef3a3437a))

- **main**: Fix cache key
  ([`109048e`](https://github.com/tm-a-t/TGPy/commit/109048e1b6fc26cd85a2b619bffaff6ca2f435e2))

- **main**: Format with black
  ([`357c8ca`](https://github.com/tm-a-t/TGPy/commit/357c8caba4082fb9d1192bcb67626c2f95abe74b))

### Documentation

- Installation with pip & other readme changes
  ([`b220b94`](https://github.com/tm-a-t/TGPy/commit/b220b9451a7e882817292ea7ccfe2c4be9739741))

- Readme & guide updates
  ([`59a4036`](https://github.com/tm-a-t/TGPy/commit/59a40360ed3c0c6315f933dc3871c147bcf4bcd2))

- add guide link to readme - 'hooks' are replaced with 'modules' - API page

### Features

- Multiple improvements
  ([`6b9cbda`](https://github.com/tm-a-t/TGPy/commit/6b9cbdaf79b11cd1e5922999f96e9321a2df4051))

- hooks are now modules - new module format (.py file with yaml metadata in docstring) - refactor
  some code - add API for modifying tgpy behaviour accessible via `tgpy` variable - modules.add now
  changes hook if exists, instead of completely overwriting - modules.add now uses
  `tgpy://module/module_name` as origin - modules['name'] can now be used instead of
  Module.load('name') - 'name' in modules can now be used to check if module exists


## v0.3.0 (2021-12-26)

### Features

- **update**: Show when no updates are available
  ([`62145ff`](https://github.com/tm-a-t/TGPy/commit/62145ff10215e25793e49d7a83d350d665946fce))


## v0.2.3 (2021-12-26)

### Bug Fixes

- **update**: Try both regular installation and --user installation
  ([`50ffbe9`](https://github.com/tm-a-t/TGPy/commit/50ffbe94da5f8e061326be492f064c891bb63817))


## v0.2.2 (2021-12-26)

### Bug Fixes

- **update**: Use --user installation when updating
  ([`1902672`](https://github.com/tm-a-t/TGPy/commit/19026724dbe26e29562e580d187575c774125da8))

### Refactoring

- Remove broken migrate_config function
  ([`c8f976c`](https://github.com/tm-a-t/TGPy/commit/c8f976cfb726a35481126c67558dbb5cc95fd38c))


## v0.2.1 (2021-12-26)

### Bug Fixes

- Store data in system config dir instead of module directory
  ([`7d92544`](https://github.com/tm-a-t/TGPy/commit/7d9254425e72640bce07a06205cb0fb692b72250))

- Update from pypi, if installed as package
  ([`a80b78f`](https://github.com/tm-a-t/TGPy/commit/a80b78fccc710b902b5264a738451b52765f49a5))

### Build System

- Remove obsolete requirements.txt [skip ci]
  ([`902e389`](https://github.com/tm-a-t/TGPy/commit/902e389235a5d63f00f47169ff77393682bd483b))

### Chores

- **changelog**: Remove old generated changelog [skip ci]
  ([`e6740e7`](https://github.com/tm-a-t/TGPy/commit/e6740e7978d3f0130db9df91cc7eddd9c2d32859))

### Continuous Integration

- Fixes, [skip release] tag
  ([`5bacb86`](https://github.com/tm-a-t/TGPy/commit/5bacb86f069ad11b7f81dd498668a704a6866fac))

- Remove [skip release] tag, trigger only on changes in tgpy/ or .github/
  ([`27a2b48`](https://github.com/tm-a-t/TGPy/commit/27a2b48290de87cc2e939cd636e54e5635d1d3f3))


## v0.2.0 (2021-12-25)

### Bug Fixes

- 'msg' stands for Message instead of events.NewMessage
  ([`428b08b`](https://github.com/tm-a-t/TGPy/commit/428b08b48131c24274a33329dbed7d3ffd3f6ce8))

- App.run_code.parse_code: attr.attr.attr was a false positive
  ([`5cb7e28`](https://github.com/tm-a-t/TGPy/commit/5cb7e2819a1c4a3e22df5c1a414fe2e04ed1d961))

- Change return value only if it's not inside other function
  ([`553f864`](https://github.com/tm-a-t/TGPy/commit/553f8646fca74ddfdc447ff93d63d628de74898b))

- Check for forward, via and out in all handlers
  ([`d189c08`](https://github.com/tm-a-t/TGPy/commit/d189c0838cddad15a633f489429acafd6b9bdb24))

- Code detection
  ([`b668329`](https://github.com/tm-a-t/TGPy/commit/b6683292239bcd9c66c92c16f98ec301c135ee41))

Include ctx, msg, print and client to locals to improve code detection

- Code like *"constant", *name or *attr.ibute is ignored
  ([`739c80e`](https://github.com/tm-a-t/TGPy/commit/739c80e56c87042e6e1803d51fe5d22d840bc891))

- Convert old config
  ([`10e0285`](https://github.com/tm-a-t/TGPy/commit/10e028596f45fb67fac70f7a23fa34a9003884c0))

- Disable link preview when editing
  ([`703ea27`](https://github.com/tm-a-t/TGPy/commit/703ea273387269c33d01d6307364aecb56af2c37))

- Disable reevaluation of edited messages in broadcast channels
  ([`62c3006`](https://github.com/tm-a-t/TGPy/commit/62c30060b510cd8c149da6507b9e4b5938fecc57))

- Do not stringify TLObjects in iterable eval results
  ([`fdec6d4`](https://github.com/tm-a-t/TGPy/commit/fdec6d47a3fe61080a3c7fc61dabf08705a003bf))

- Don't count -1 as code
  ([`eab27f6`](https://github.com/tm-a-t/TGPy/commit/eab27f60103a0db9ecb76a9c6c7e9e7280edf5c6))

A single expr which is unary operator with constant operand is no longer a code!

- Edit message after restart
  ([`44b5d07`](https://github.com/tm-a-t/TGPy/commit/44b5d0755cb812a6651620a2470384c2a7f2833d))

- Editting message caused error
  ([`b171036`](https://github.com/tm-a-t/TGPy/commit/b171036b2d107469f5bbf5a1226206843815604c))

- Empty return
  ([`cab3635`](https://github.com/tm-a-t/TGPy/commit/cab3635e85b9151aa22211ca887c9ca40318a530))

- False positive code detections (closes #4)
  ([`c8f25d4`](https://github.com/tm-a-t/TGPy/commit/c8f25d4899f51d07cc47de2ddcc0c3c5ec22d0b8))

- Get rid of for ... in range(len(root.body))
  ([`ceff1de`](https://github.com/tm-a-t/TGPy/commit/ceff1de8a43054b6a03b7f9ae114f45a0863de86))

- Make cancel command case-insensitive
  ([`b938ea3`](https://github.com/tm-a-t/TGPy/commit/b938ea3621caca4279e52788ea828cf42d212dd0))

- Make update sync
  ([`73f96a1`](https://github.com/tm-a-t/TGPy/commit/73f96a1e4b1125107ee7ced4d524e12b802b2732))

- Messageemptyerror on '//', closes #13
  ([`a2d8883`](https://github.com/tm-a-t/TGPy/commit/a2d8883768f2ccbf0db915902830d801edcbd7c3))

- Meval.shallow_walk - ignore async function definitions too
  ([`5e5f04e`](https://github.com/tm-a-t/TGPy/commit/5e5f04ebea285da3db688d566be6feb403cb8b72))

- Move session file to data dir
  ([`b7db892`](https://github.com/tm-a-t/TGPy/commit/b7db8929be793e75dd77ca67006e89c56d1cc7c6))

- No link preview in TGPy error notifications
  ([`3af06cd`](https://github.com/tm-a-t/TGPy/commit/3af06cdb625e4db2c8a672cc26e9094771c4ec54))

- Remove buggy ctx.orig
  ([`f5f31ac`](https://github.com/tm-a-t/TGPy/commit/f5f31ac64887a8f6f984f633a87533af2afbdd31))

- Save formatting when prevent evaluation
  ([`1f3b3dd`](https://github.com/tm-a-t/TGPy/commit/1f3b3dd587dc5a4938b58a360479cfbbd8d41b6e))

- Show commit info in ping message and after update
  ([`26c63d4`](https://github.com/tm-a-t/TGPy/commit/26c63d492993784aaa8cca316053be1d040d930b))

- Str instead of repr for Context
  ([`3c51b72`](https://github.com/tm-a-t/TGPy/commit/3c51b7205d60e0f87b63164d13d386efea0e15d6))

- Tgpy will no longer crash if returned coroutine crashes
  ([`a4303f3`](https://github.com/tm-a-t/TGPy/commit/a4303f32b624f7ae77d8f9099178b222b078ae21))

- Tuples of constants are not evaluated
  ([`ecec598`](https://github.com/tm-a-t/TGPy/commit/ecec598eca5be5130a264861938a1db423f6cb21))

- Update
  ([`846c98b`](https://github.com/tm-a-t/TGPy/commit/846c98b9d57bf9ff19bdc39b24025c6d6f607b22))

- Use getpass.getpass to get 2FA password (fixes #7) ([#8](https://github.com/tm-a-t/TGPy/pull/8),
  [`858e721`](https://github.com/tm-a-t/TGPy/commit/858e7212082e9b7061d0219403e144224cf7f573))

- Using orig var after message edit
  ([`7f3108f`](https://github.com/tm-a-t/TGPy/commit/7f3108fc9776330bbe374c1c421ff1cca0162200))

### Build System

- Switch to poetry, reanme package to tgpy, fix readme images
  ([`263bbcc`](https://github.com/tm-a-t/TGPy/commit/263bbcca39b02f38d340262fcd5f34a648a5598c))

### Continuous Integration

- Automatic semantic releases
  ([`2f34246`](https://github.com/tm-a-t/TGPy/commit/2f3424696bbae77004c08f43fe7271355bdfe779))

- Debug VIVOD
  ([`fb90e12`](https://github.com/tm-a-t/TGPy/commit/fb90e12a77f80e1efa6299ee27b138e4c91fe1fa))

- Fix x1
  ([`cde7e27`](https://github.com/tm-a-t/TGPy/commit/cde7e2754a0fb813c2ab764adeb93f1746d0c93c))

- Fix x1874
  ([`378ed92`](https://github.com/tm-a-t/TGPy/commit/378ed92043de25e5f20350e9146e6b287949979d))

- Fix x1875
  ([`d2eeb60`](https://github.com/tm-a-t/TGPy/commit/d2eeb60cfe0be3c7b5850af1e39fd8d03eec7212))

- Fix x1876
  ([`cd3f30a`](https://github.com/tm-a-t/TGPy/commit/cd3f30ad3d6cfd518453086c8259a5fae3a37925))

- Fix x1877
  ([`0a83ec3`](https://github.com/tm-a-t/TGPy/commit/0a83ec368b8e6e095b516af45eb4d74b18f9e296))

- Fix x2
  ([`d53cf91`](https://github.com/tm-a-t/TGPy/commit/d53cf91478b35244548f35ad3cf4c48880bf8980))

- Fix x3
  ([`8858a69`](https://github.com/tm-a-t/TGPy/commit/8858a69a8aab05547570e7280a44ab9212fcfcd5))

- Fix x4
  ([`d6e7852`](https://github.com/tm-a-t/TGPy/commit/d6e7852bd8d3e308c6a937491715d3dc051cbd3c))

- Fix x5
  ([`687a7cd`](https://github.com/tm-a-t/TGPy/commit/687a7cddf3a5e3221a0612dab5e2f81e84090fb5))

- Fix x6
  ([`df75fe8`](https://github.com/tm-a-t/TGPy/commit/df75fe86f8bdc29ad3ba883d932aed5c824d91d7))

- Fix x7
  ([`7663ce1`](https://github.com/tm-a-t/TGPy/commit/7663ce1d6706d1c511b983f237193f9b7533dc8e))

- Fix: deploy guide only from master branch
  ([`6a99cb1`](https://github.com/tm-a-t/TGPy/commit/6a99cb159abf87ee85d88b22925bcaecc60b0026))

- Github................. ne materus
  ([`54153e5`](https://github.com/tm-a-t/TGPy/commit/54153e5929de376e4fe1f69cd4aaf8b820bd49ab))

- Init ([`8c06daf`](https://github.com/tm-a-t/TGPy/commit/8c06daf990e2ce6a6b5bcb3df2707579df36d068))

- Ne nu ya dazhe debug vivod ne can sdelat(
  ([`21a0074`](https://github.com/tm-a-t/TGPy/commit/21a0074b0317814dbc758e690d262b866d3bd4d9))

### Documentation

- Copied readme to index.md
  ([`50e7879`](https://github.com/tm-a-t/TGPy/commit/50e7879812695d983a1c08ea824afb75073a739f))

### Features

- __repr__ of Context, ping() function
  ([`a1a1443`](https://github.com/tm-a-t/TGPy/commit/a1a1443a5a266457e77506a7d19b1564687393d5))

- App object and config loading
  ([`ae9bd17`](https://github.com/tm-a-t/TGPy/commit/ae9bd176e33b9f325beb8949685a1f07b64095b3))

Load config before setting Telethon client.

- Cancel without reply
  ([`2c77e6f`](https://github.com/tm-a-t/TGPy/commit/2c77e6f5907937e9ad91b5bfc5ac24d10e80e85e))

- Changes of custom hook functions
  ([`3ed8822`](https://github.com/tm-a-t/TGPy/commit/3ed882290fb358a2b1415aa81e89b0e43b430d98))

- Ctx variable
  ([`80503a8`](https://github.com/tm-a-t/TGPy/commit/80503a866510b74222b9dd2cb9cde3c84056de7d))

- Context class for ctx variable (with ctx.msg for current msg and ctx.orig for current orig) -
  run_code.utils file for auxiliary functions and classes

- Docstrings for app/run_code/parse_code.py
  ([`b6d283a`](https://github.com/tm-a-t/TGPy/commit/b6d283aed3e6a714ca70d44a93f46087a6bd450b))

- Exception formatting
  ([`1417583`](https://github.com/tm-a-t/TGPy/commit/141758336a2f7354f4a3e795f793c187725d3458))

- Only show evaluating levels related to code - Start lines with 'File "<message>" ...'

- If message with code is deleted, ignore error on the result editing
  ([`7872678`](https://github.com/tm-a-t/TGPy/commit/78726786fcf2ba6288752e6ab0fd7eff5e54c8b4))

- If result is None, show output instead of result
  ([`bc8f1ce`](https://github.com/tm-a-t/TGPy/commit/bc8f1ce865acd87032cc4bc43df9659c1c930cee))

- Make code detection less strict
  ([`c86d842`](https://github.com/tm-a-t/TGPy/commit/c86d842eb5759b0e4c7ea92f8dc5bd2e86edc6a3))

- binary operations with constants (like "1 - 2", but not "1" or "+1") are considered code now - if
  a variable which is present in locals() appears in the message, it **is** evaluated

- Preparing for PyPI publication & single command configuration
  ([`2e7e3ca`](https://github.com/tm-a-t/TGPy/commit/2e7e3ca82bbc7778cbe3a347c7c79c559200e99f))

- add `rich` console - create app_config.py and Config class - add required files for PyPI - rename
  utils.py

- Pretty cli setup and logs
  ([`f440ea4`](https://github.com/tm-a-t/TGPy/commit/f440ea42e2e98a16442f6c5b563f5d37ad11e771))

- Pretty logging
  ([`f7d1b60`](https://github.com/tm-a-t/TGPy/commit/f7d1b605c3022bcb96423c2d3d2ad615b6018a56))

- Run using aiorun
  ([`28e95b5`](https://github.com/tm-a-t/TGPy/commit/28e95b5430097f4cb93fd561dbc616431054fd6d))

- Save hook datetime, run hooks in order of addition
  ([`e6d2cea`](https://github.com/tm-a-t/TGPy/commit/e6d2cea9b8f13356b109e3a12472f53cb312421d))

- Show 'tgpy' package version if it's installed
  ([`d9fbf77`](https://github.com/tm-a-t/TGPy/commit/d9fbf77e6e7bc3eaf2f2e591286dacd96601c6ab))

- Show username and hostname in ping()
  ([`df7722c`](https://github.com/tm-a-t/TGPy/commit/df7722c2a202df65de6e3905d639ffe9789ab16b))

- Update command
  ([`a87a803`](https://github.com/tm-a-t/TGPy/commit/a87a8030cd27d2d7122d7562478a363279077f13))

- User hooks addition and removal
  ([`0abb062`](https://github.com/tm-a-t/TGPy/commit/0abb0628d08e02bd7a93a93aa35c38b91b18fc98))

### Refactoring

- 'cancel' command
  ([`4696022`](https://github.com/tm-a-t/TGPy/commit/46960222e0291312b5a11c4a91a8f92d7bc22c53))

- App/run_code/parse_code.py: shorter lines, better function names
  ([`fc0e66d`](https://github.com/tm-a-t/TGPy/commit/fc0e66d0fb32e0a9b632f5bfcd0de6435091a620))

- Meval
  ([`187b738`](https://github.com/tm-a-t/TGPy/commit/187b73889ef3aa41f835f89b61896625e2fe3ed5))

- Meval.py changes
  ([`d84202a`](https://github.com/tm-a-t/TGPy/commit/d84202a7311b1ac22b6a6762e088bb1ab1a23548))

- Project structure
  ([`97cad96`](https://github.com/tm-a-t/TGPy/commit/97cad961662a732a0c2a84cd998205e3ba1acfd2))
