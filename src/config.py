import json

class SafeDict():
    def __init__(self, source: dict):
        self._data = source

    def get_value(self) -> object:
        return self._data

    def __getattr__(self, name: str):
        if not name.startswith('_'):
            if self._data and name in self._data:
                return SafeDict(self._data[name])
            return SafeDict(None)

_config = {}

def get_config() -> SafeDict:
    return SafeDict(_config)

def reload_config() -> None:
    with open('config.json', 'r') as fd:
        _config.update(json.load(fd))

reload_config()
