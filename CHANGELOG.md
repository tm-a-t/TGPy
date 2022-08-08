# Changelog

<!--next-version-placeholder-->

## v0.5.0 (2022-08-08)
### Feature
* Use the latest telethon from v1.24 branch, update all dependencies ([`91894fc`](https://github.com/tm-a-t/TGPy/commit/91894fc6894e5e111baa469c3de372b46e62b049))
* Transform x.await into await x ([`6117421`](https://github.com/tm-a-t/TGPy/commit/6117421cc7b72c56dace006d2fc569edfe14b734))
* Better version detection, ping() builtin improvements ([`265b83f`](https://github.com/tm-a-t/TGPy/commit/265b83f0c604b96ae740e06a32441b7e001bac1a))
* Allow to specify data directory via environment variable TGPY_DATA ([`4d769da`](https://github.com/tm-a-t/TGPy/commit/4d769daea76bc1abe86914487f9a80d3ea0eb2fb))

### Fix
* Setting/removing reaction no longer triggers reevaluation ([`cf6e64e`](https://github.com/tm-a-t/TGPy/commit/cf6e64e82d1823202941610274a4ff38955c5cf1))
* Use custom telethon version without MessageBox as it's very buggy ([`9c7738e`](https://github.com/tm-a-t/TGPy/commit/9c7738e40cda69499974ceda711f56ca65782312))
* Apply autoawait pre_transform after regular code transformers ([`fde6291`](https://github.com/tm-a-t/TGPy/commit/fde62914540d43da01a02e547f2e62516f7cf52e))
* Message markup for utf-16 (closes #10) ([`20f48bc`](https://github.com/tm-a-t/TGPy/commit/20f48bc8e08490e85ff68bfe6feb9997eb8cbb29))
* Parsing of modules with triple quotes in code ([`485166d`](https://github.com/tm-a-t/TGPy/commit/485166d5c513e196c0db760c468599d3c6ab9581))

### Documentation
* New video on docs page ([`9abf1eb`](https://github.com/tm-a-t/TGPy/commit/9abf1eb9293313e22d68b57c3c1948365a9a7ed9))
* Readme video fix ([`383fe5b`](https://github.com/tm-a-t/TGPy/commit/383fe5bcfa8f9b1274b113ab426e1f08138dfdfd))
* Readme video ([`59a2f12`](https://github.com/tm-a-t/TGPy/commit/59a2f121339f146dcb9b509450bdff8f1af36866))
* Update readme ([`a23c076`](https://github.com/tm-a-t/TGPy/commit/a23c0765d1f83f0cb41d8297d8218d8078d0a7d4))
* Change readme assets. new video ([`d0b3565`](https://github.com/tm-a-t/TGPy/commit/d0b35657f4f98542eb6408fb2c21420e19034f5c))
* Update readme ([`5569ccb`](https://github.com/tm-a-t/TGPy/commit/5569ccbb5fa601ff9b0c8cb4011dce5ea93eab9f))
* Guide changes: ([`767473b`](https://github.com/tm-a-t/TGPy/commit/767473bdfdfebecc4e2998f0cc9b7bf7bdebecf9))
* Fix some typos here and there in the guides ([#26](https://github.com/tm-a-t/TGPy/issues/26)) ([`9d6c8a8`](https://github.com/tm-a-t/TGPy/commit/9d6c8a83c054eb4e54866f120355c44de88458b2))
* Guide changes: ([`024bce3`](https://github.com/tm-a-t/TGPy/commit/024bce351a4784dc32cef66a7d6c4dcd146d2ffb))
* Guide changes ([`b000c12`](https://github.com/tm-a-t/TGPy/commit/b000c12cbbbdaad5f2c02452dd6e2f9b9710e840))
* Guide text changes ([`903963a`](https://github.com/tm-a-t/TGPy/commit/903963a170ff5965c9044643c14b1ce41879cd15))
* Guide changes ([`237a1cd`](https://github.com/tm-a-t/TGPy/commit/237a1cdd69cd5770d995f26305ae0d51d4db5dbd))
* Guide changes. many changes. ([`74ae524`](https://github.com/tm-a-t/TGPy/commit/74ae524b7fa5f554e02ace092fd9951663c78a95))
* Guide changes: ([`9e7f832`](https://github.com/tm-a-t/TGPy/commit/9e7f832c5be8a0126efc1ae47afbbe6fc8ea9042))
* Guide theme changes ([`33dcbb0`](https://github.com/tm-a-t/TGPy/commit/33dcbb0ae247e17b09d9deb817d3b7ba733d8fb9))
* Guide changes ([`43a0779`](https://github.com/tm-a-t/TGPy/commit/43a0779c45c0f01fa2c70ff8797332aa0b11a100))
* Guide changes ([`f432d30`](https://github.com/tm-a-t/TGPy/commit/f432d30a2a860f2a1969d9d7f9de55d34cdec140))
* Guide color palette & guide changes ([`6320934`](https://github.com/tm-a-t/TGPy/commit/63209349449efe8ece23c4dcccce7585e24b1bd7))
* Restructure guide ([`8cee429`](https://github.com/tm-a-t/TGPy/commit/8cee42932b69dc8b55098ae747e7c2d99306fa19))

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
