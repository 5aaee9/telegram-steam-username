import asyncio
from src import bot
from src.config import get_config

async def main():
    bot_client = await bot.make_client()
    await bot.login_client(bot_client)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())