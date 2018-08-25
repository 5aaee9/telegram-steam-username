import asyncio
import time
from src import bot, steam
from src.config import get_config

async def main():
    steam_client = steam.Steam(get_config())
    bot_client = await bot.make_client()
    
    await bot_client.connect()

    while True:
        status = await steam_client.pull_status()
        await bot.events(bot_client, status)
        time.sleep(10)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())