# Telegram Steam Username

Connect your steam playing status with your Telegream last name.

# Set Up

We need Two keys, one from steam and the other from Telegram

## Get steam key

Go to [steam key page](https://steamcommunity.com/dev/apikey)
 and get your unique key

## Get Telegram client key

Go to [Telegram Apps](https://my.telegram.org/apps) and create your client

## Config

Edit settings in `config.json`

```
api_key -> steam API key
user_id" -> steam unique user id
telegram_id -> telegram client id
telegram_hash -> telegram client screct
non_playing -> last name when you not play game
playing -> last name when you playing game, {} will been replaced as game
```

## Run

```bash
# first run
pip install -r requirements.txt
python login.py

python main.py
```

Enjoy!
