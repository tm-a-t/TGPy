# Changelog

<!--next-version-placeholder-->

## v0.13.2 (2023-12-10)

### Fix

* Update telethon (fix draft constructor), update all dependencies ([`a2b6064`](https://github.com/tm-a-t/TGPy/commit/a2b60641af3a0cab9fef08e95e07447b6c61432a))

## v0.13.1 (2023-12-06)

### Fix

* Use official cryptg (prebuilt wheels for Python 3.12), bump telethon (fixes usage of Draft), set minimum python version to 3.10 ([`9e49739`](https://github.com/tm-a-t/TGPy/commit/9e497391f83dc6b333a6752f221d1221ea3d6cdb))

## v0.13.0 (2023-12-05)

### Feature

* Support proxy ([`cd6bc90`](https://github.com/tm-a-t/TGPy/commit/cd6bc9086a818c45ee129ace88a0662980ad6c92))

## v0.12.1 (2023-10-28)

### Fix

* **Telethon:** New layer fix ([`8145bd3`](https://github.com/tm-a-t/TGPy/commit/8145bd3c58371e047114e834e2fbdba2de7ec575))

## v0.12.0 (2023-10-28)

### Feature

* **Telethon:** Update to layer 166 ([`a18dc0d`](https://github.com/tm-a-t/TGPy/commit/a18dc0d663362b50dfe7827ebac6ea2971220248))

## v0.11.0 (2023-09-29)

### Feature

* **Telethon:** Fixes for the new layer and many more fixes from upstream ([`800fcd5`](https://github.com/tm-a-t/TGPy/commit/800fcd5f9799e82ed8a85155afd1c884b22355d3))

## v0.10.0 (2023-09-25)

### Feature

* **Telethon:** Layer 164 ([`2d0c186`](https://github.com/tm-a-t/TGPy/commit/2d0c1865fad08c8ee1f511f6749a22ede7374641))

### Documentation

* Revert narrowing container ([`bb0bff9`](https://github.com/tm-a-t/TGPy/commit/bb0bff98b058041a62f45fed260bf1f42ce32900))
* Recipes and new homepage ([`28e8eba`](https://github.com/tm-a-t/TGPy/commit/28e8ebae6f57642ce2dea7a70d4bd0bcfee94dc0))
* Fix transformer example ([`8007b25`](https://github.com/tm-a-t/TGPy/commit/8007b2587046550937cc63f7e5cd66f86e928f29))

## v0.9.7 (2023-07-23)
### Fix
* Consistent colors in setup across all terminals ([`faa625b`](https://github.com/tm-a-t/TGPy/commit/faa625bd2f4543b08ea7af361c8217cf006303d2))

## v0.9.6 (2023-06-01)
### Fix
* Strip device model ([`a775cc5`](https://github.com/tm-a-t/TGPy/commit/a775cc5a6415e92d023c421578f31bdd57a7a88d))

## v0.9.5 (2023-06-01)
### Fix
* Try to fix session termination issue by setting device_model and system_version to real values from the system ([`44e1c3d`](https://github.com/tm-a-t/TGPy/commit/44e1c3d8faf17f52ec289c3b6c69ae44ed75271e))

## v0.9.4 (2023-05-05)
### Fix
* Initial setup can now be interrupted with ctrl+c ([`e6253c7`](https://github.com/tm-a-t/TGPy/commit/e6253c7573f1eed9bbaefe739a967181a9c932e9))
* Initial setup prompts now work properly ([`8713dff`](https://github.com/tm-a-t/TGPy/commit/8713dff2f216bdadb9b07269c68f909b6867f681))

## v0.9.3 (2023-02-25)
### Fix
* Deleting message no longer produces an error ([`ef317d9`](https://github.com/tm-a-t/TGPy/commit/ef317d98b9e817843eca8f0756147855217ccb3b))

## v0.9.2 (2023-02-25)
### Fix
* Message editing bug ([`3d1d566`](https://github.com/tm-a-t/TGPy/commit/3d1d566864381ea939143fae3fad607e03b5a548))

## v0.9.1 (2023-02-25)
### Fix
* Update from older versions ([`df11e8b`](https://github.com/tm-a-t/TGPy/commit/df11e8b0b8801b7c0e47f29b173964a7b63fa887))

## v0.9.0 (2023-02-25)
Major update
- restructured the code
- cancel, // now remember cancellation permanently
- reactions fix now remembers message content hashes after a restart. This means no more 'Edit message again to evaluate' messages
- implemented simple key-value store for storing various data
  - `tgpy.api.config.get(key: str, default: JSON = None) -> JSON`
  - `tgpy.api.config.set(key: str, value: JSON)`
  - `tgpy.api.config.unset(key: str)`
  - `tgpy.api.config.save()` useful when modifying objects acquired using the .get method in place
- if the `__all__` variable is set in a module, only objects with names in that list are exported (added to variables list)
- `ctx.is_module` is True if the code is executed as a module (on startup)
- `ctx.is_manual_output` can be set to True to prevent the last message edit by TGPy so that you can edit it yourself
- cancel, //, restart, ping, update, modules object and .await syntax are now implemented as regular modules in the `std` directory
  - builtin modules can be disabled with `core.disable_modules` config option (for example, `tgpy.api.config.set('core.disable_modules', ['postfix_await'])`)
- extra keys are now allowed in module metadata. They are parsed into `Module.extra` dict
- `tgpy.api` module is now used for public API instead of the `tgpy` object
- moved `get_installed_version`, `get_running_version`, `installed_as_package`, `get_user`, `get_hostname`, `running_in_docker`, `try_await`, `outgoing_messages_filter`
  functions to `tgpy.api` (`tgpy.api.utils`)
- new public API functions:
  - `async parse_code(text: str) -> ParseResult(is_code: bool, original: str, transformed: str, tree: AST | None)`
  - `parse_tgpy_message(message: Message) -> MessageParseResult(is_tgpy_message: bool, code: str | None, result: str | None)`
  - `async tgpy_eval(code: str, message: Message = None, *, filename: str = None) -> EvalResult(result: Any, output: str)`
- AST transformers. AST transformers are applied after code transformers
- exec hooks. Exec hooks are executed before the message is parsed and handled. Exec hooks must have the following signature: `async hook(message: Message, is_edit: bool) -> Message | bool | None`. An exec hook may edit the message using Telegram API methods and/or alter the message in place. If a hook returns Message object or alters it in place, it's used instead of the original Message object during the rest of handling (including calling other hook functions). If a hook returns True or None, execution completes normally. If a hook returns False, the rest of hooks are executed and then the handling stops without further message parsing or evaluating
  - Apply hooks with `tgpy.api.exec_hooks.apply(message: Message, *, is_edit: bool) -> Message | False`. This method returns False if any of the hooks returned False, Message object that should be used instead of the original one otherwise
- new dict/list compatible transformers/hooks interface (`store_obj` is one of `tgpy.api.code_transformers`, `tgpy.api.ast_transformers` or `tgpy.api.exec_hooks`)
  - add a function with `store_obj.add(name, function)`
  - add/replace a function with `store_obj[name] = function`
  - get a function with `store_obj[name or index]`
  - iter functions with `for name, function in store_obj`
  - apply transformers/hooks with `tgpy.api.code_transformers.apply(code: str) -> str`, `tgpy.api.ast_transformers.apply(tree: AST) -> AST` or `tgpy.api.exec_hooks.apply` (documented above)
- podman is now correctly detected so that tgpy doesn't try to update itself in the container
- Change in-message url to tgpy.tmat.me ([`8737ca9`](https://github.com/tm-a-t/TGPy/commit/8737ca92d600e0f57987426fa0ab9ba2fc655183))
- Move tokenize_string and untokenize_to_string to tgpy.api ([`7d8c3b2`](https://github.com/tm-a-t/TGPy/commit/7d8c3b2cadb46bd7447f9e908da1b9cadfe012e8))

## v0.8.0 (2023-02-15)
### Feature
* Wrap sys.stdout instead of print to capture output + properly use contextvars ([`7aa2015`](https://github.com/tm-a-t/TGPy/commit/7aa2015215ad621b405c6471add250bf11aa70c2))

### Fix
* Don't stop on unhandled errors. They may happen when, for example, a module uses asyncio.create_task ([`3584f22`](https://github.com/tm-a-t/TGPy/commit/3584f223064902f8238f35715219289b6a16ea13))

## v0.7.0 (2023-02-05)
### Feature
* Update telethon (new markdown parser, html parser fixes) ([`43dd76f`](https://github.com/tm-a-t/TGPy/commit/43dd76f0953e6ba2e77e9b5bc25f2748a36967ee))
* Update dependencies (layer 152) ([`234dc86`](https://github.com/tm-a-t/TGPy/commit/234dc86399c8545b07f55c1cddbcfbabcac2c372))

### Fix
* Handle entities properly when editing "//" message ([`6d989dc`](https://github.com/tm-a-t/TGPy/commit/6d989dc5349e026338857115d93f5c532f760578))
* Specify parse_mode in error handler to support markdown global parse mode ([`60cd81b`](https://github.com/tm-a-t/TGPy/commit/60cd81b9ca5cbb85ed72808e6ce3954bee455c3a))
* Use message.raw_text instead of message.text to detect // ([`a85b1c8`](https://github.com/tm-a-t/TGPy/commit/a85b1c834135f2b7c251ff8482afbab93f73002e))

## v0.6.2 (2023-01-22)
### Fix
* Fix IndentationError appearing for some non-code messages ([`599c84f`](https://github.com/tm-a-t/TGPy/commit/599c84f9ba4104d678476b07b090c54529246ab9))
* **docker:** Add /venv/bin to path ([`00be149`](https://github.com/tm-a-t/TGPy/commit/00be149b4ce827e97bb31b84f39cfa988a68d1ee))

### Documentation
* Update readme intro ([`c334669`](https://github.com/tm-a-t/TGPy/commit/c334669fcab8a6fc7a3f8330ae3217de21b97430))

## v0.6.1 (2023-01-06)
### Fix
* Update command saying "Already up to date" while in fact updating correctly ([`9b25fe6`](https://github.com/tm-a-t/TGPy/commit/9b25fe60809cfbb045bd605c0fa78f5ae19d57d0))

## v0.6.0 (2022-11-26)
### Feature
* Use MessageEntityPre with language set to 'python' to enable syntax highlighting on supported clients (e.g. WebZ). Closes #24 ([`5de6ded`](https://github.com/tm-a-t/TGPy/commit/5de6ded579c237f0221b6223dfd18254a2ebb1cd))

### Fix
* Keep 'cancel' message when replying to other user (fixes #21) ([`057231d`](https://github.com/tm-a-t/TGPy/commit/057231d7a437d5ab4fca280b130714573904a67e))
* Ignore error when running code deletes the message itself ([`d022450`](https://github.com/tm-a-t/TGPy/commit/d0224502c5393dc423c9790e88fedc94bbb5afbf))

### Documentation
* Update readme ([`a321bbf`](https://github.com/tm-a-t/TGPy/commit/a321bbfe474e8ae97132a7f0f4d11c009495c482))

## v0.5.1 (2022-08-09)
### Fix
* Restart() now edits message properly ([`60afa44`](https://github.com/tm-a-t/TGPy/commit/60afa44e7002fa87a5c0d2adb60c2065e885f1ec))
* Compatibility with python 3.9 ([`f3c0468`](https://github.com/tm-a-t/TGPy/commit/f3c046847f9d7f549586c829dbec74238f264ed2))

## v0.5.0 (2022-08-08)
### Feature
* Use custom telethon fork with updated layer ([`91894fc`](https://github.com/tm-a-t/TGPy/commit/91894fc6894e5e111baa469c3de372b46e62b049)) ([`9c7738e`](https://github.com/tm-a-t/TGPy/commit/9c7738e40cda69499974ceda711f56ca65782312))
* Transform x.await into await x ([`6117421`](https://github.com/tm-a-t/TGPy/commit/6117421cc7b72c56dace006d2fc569edfe14b734)) ([`fde6291`](https://github.com/tm-a-t/TGPy/commit/fde62914540d43da01a02e547f2e62516f7cf52e))
* Better version detection, ping() builtin improvements ([`265b83f`](https://github.com/tm-a-t/TGPy/commit/265b83f0c604b96ae740e06a32441b7e001bac1a))
* Allow to specify data directory via environment variable TGPY_DATA ([`4d769da`](https://github.com/tm-a-t/TGPy/commit/4d769daea76bc1abe86914487f9a80d3ea0eb2fb))

### Fix
* Setting/removing reaction no longer triggers reevaluation (#25) ([`cf6e64e`](https://github.com/tm-a-t/TGPy/commit/cf6e64e82d1823202941610274a4ff38955c5cf1))
* Emojis no longer break messages markup (#10) ([`20f48bc`](https://github.com/tm-a-t/TGPy/commit/20f48bc8e08490e85ff68bfe6feb9997eb8cbb29))
* Parsing of modules with triple quotes in code ([`485166d`](https://github.com/tm-a-t/TGPy/commit/485166d5c513e196c0db760c468599d3c6ab9581))

### Documentation
* Guide rewrite

## v0.4.1 (2022-01-10)
### Fix
* **code detection:** Ignore messages like "fix: fix" ([`1b73815`](https://github.com/tm-a-t/TGPy/commit/1b73815928fdbdae3eae1202c01b4b53b9906ba4))

## v0.4.0 (2022-01-10)
### Feature
* Multiple improvements ([`6b9cbda`](https://github.com/tm-a-t/TGPy/commit/6b9cbdaf79b11cd1e5922999f96e9321a2df4051))

### Fix
* **code detection:** Ignore messages like "cat (no)" and "fix: fix" ([`75bb43e`](https://github.com/tm-a-t/TGPy/commit/75bb43eae71f9e024a3e7f299cd0614c860c2457))
* Data directory path on Windows ([`7d0e283`](https://github.com/tm-a-t/TGPy/commit/7d0e2835b8c2f5b6327b012a5c56035a63433ba9))
* Print now always writes to message from which code is executed ([`0e46527`](https://github.com/tm-a-t/TGPy/commit/0e46527446749dd691263069def260ae29453077))
* Ctx.msg now always points to message from which code is executed ([`59acde9`](https://github.com/tm-a-t/TGPy/commit/59acde9ec7baef5ff130d6fb77d74c2981bd15e2))

### Documentation
* Readme & guide updates ([`59a4036`](https://github.com/tm-a-t/TGPy/commit/59a40360ed3c0c6315f933dc3871c147bcf4bcd2))
* Installation with pip & other readme changes ([`b220b94`](https://github.com/tm-a-t/TGPy/commit/b220b9451a7e882817292ea7ccfe2c4be9739741))

## v0.3.0 (2021-12-26)
### Feature
* **update:** Show when no updates are available ([`62145ff`](https://github.com/tm-a-t/TGPy/commit/62145ff10215e25793e49d7a83d350d665946fce))

## v0.2.3 (2021-12-26)
### Fix
* **update:** Try both regular installation and --user installation ([`50ffbe9`](https://github.com/tm-a-t/TGPy/commit/50ffbe94da5f8e061326be492f064c891bb63817))

## v0.2.2 (2021-12-26)
### Fix
* **update:** Use --user installation when updating ([`1902672`](https://github.com/tm-a-t/TGPy/commit/19026724dbe26e29562e580d187575c774125da8))

## v0.2.1 (2021-12-26)
### Fix
* Update from pypi, if installed as package ([`a80b78f`](https://github.com/tm-a-t/TGPy/commit/a80b78fccc710b902b5264a738451b52765f49a5))
* Store data in system config dir instead of module directory ([`7d92544`](https://github.com/tm-a-t/TGPy/commit/7d9254425e72640bce07a06205cb0fb692b72250))
