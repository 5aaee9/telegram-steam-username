import aiohttp
from src import config

_STEAM_ENDPOINT = "https://api.steampowered.com/"

class Steam():
    def __init__(self, cfg: config.SafeDict):
        self._config = cfg

    async def pull_status(self) -> object:
        api_url = _STEAM_ENDPOINT + 'ISteamUser/GetPlayerSummaries/v2/?key={}&format=json&steamids={}'
        req_url = api_url.format(self._config.api_key.get_value(), self._config.user_id.get_value())

        async with aiohttp.ClientSession() as session:
            async with session.get(req_url) as r:
                res = await r.json()
                player = res['response']['players'][0]

                if 'gameextrainfo' in player:
                    return {
                        'gaming': True,
                        'game': player['gameextrainfo']
                    }
                return {
                    'gaming': False
                }
