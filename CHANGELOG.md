# Changelog

<!--next-version-placeholder-->

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
