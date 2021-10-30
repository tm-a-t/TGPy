# Installation

1. You'll need Telegram API key. Register your "app" at [my.telegram.org](https://my.telegram.org) to get `api_id` and 
`api_hash`. App title and other data don't matter.

2. Clone the repo:
```shell
$ git clone https://github.com/tm-a-t/TGPy
$ cd TGPy
```

3. Create `config.py`. Enter your API data and your phone to log in:
```python
api_id = ...
api_hash = ...
phone = ...
```

4. Install the requirements and run TGPy:
```shell
$ pip install -r requirements.txt
$ python -m app
```

5. For the first time, you'll have to log in with a confirmation code from Telegram


## Updating

Update to the newest version with:

```shell
$ git pull
```

Or right from Telegram:

```python
update()
```
