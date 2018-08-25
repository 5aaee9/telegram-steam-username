import asyncio
from src import bot
from src.config import get_config

async def main():
    bot_client = await bot.make_client()
    await bot.login_client(bot_client)