from typing import MutableMapping, Union, Optional, Any, TypedDict
import json
from redis import Redis
from os import environ as env


class BaseConfig(TypedDict):
    host: str
    port: int
    password: Optional[Any]
    db: Optional[int]


class RedisMapping(MutableMapping):
    @classmethod
    def from_env(cls, db_idx: int):
        ks = ['RM_HOST', 'RM_PORT', 'RM_PASS']
        not_present = [x for x in ks if x not in env]
        if not_present:
            print(f'Redis Mapping from env using default values for {not_present}')

        return cls({
            'host': env.get('RM_HOST', 'localhost'),
            'port': env.get('RM_PORT', 6379),
            'password': env.get('RM_PASS', None)
        }, db_idx)

    def __init__(self, base_config: Union[BaseConfig, dict], db_idx: int):
        self.config = base_config | {'db': db_idx}
        self.cxn = Redis(**self.config)

    def __getitem__(self, item):
        if found := self.cxn.get(item):
            try:
                return json.loads(found)
            except UnicodeDecodeError:
                return found
        raise KeyError

    def __len__(self):
        return self.cxn.info().get('db0', {'keys': 0})['keys']

    def __setitem__(self, key, value):
        if not (isinstance(value, str) or isinstance(value, bytes)):
            value = json.dumps(value)
        self.cxn.set(key, value)

    def __delitem__(self, key):
        if self.cxn.exists(key):
            self.cxn.delete(key)

    def __iter__(self):
        for x in self.cxn.keys():
            yield x
