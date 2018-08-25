from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest, UpdateProfileRequest
from telethon.tl.functions.users import GetUsersRequest  
from src import config
from src.logger import logger

async def make_client() -> TelegramClient:
    api_id = config.get_config().telegram_id.get_value()
    api_hash = config.get_config().telegram_hash.get_value()

    return TelegramClient('steam_username', api_id, api_hash)

async def login_client(client: TelegramClient) -> None:
    # some side efflect
    password = input('Input your 2FA password: ')
    if password != '':
        await client.start(password=password)
    else:
        await client.start()
    

async def events(client: TelegramClient, status: object) -> None:
    user = await client.get_me()
    last_name = ""

    if status['gaming']:
        last_name = config.get_config().playing.get_value().format(status['game'])
    else:
        last_name = config.get_config().non_playing.get_value()
    
    if user.last_name != last_name:
        logger.info('changing lastname: {}'.format(last_name))
        await client(UpdateProfileRequest(first_name=user.first_name, last_name=last_name))