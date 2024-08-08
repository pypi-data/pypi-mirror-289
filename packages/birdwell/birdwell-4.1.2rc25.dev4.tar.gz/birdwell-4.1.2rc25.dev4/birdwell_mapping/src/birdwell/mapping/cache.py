from typing import Optional
import pickle
import requests
import os
from os import PathLike
import json
import copy
from datetime import timedelta, datetime


class CachedRequester:
    def __init__(
            self,
            path: str | PathLike = '.birdwell/requests/cache.json',
            stale_timeout: timedelta | None = None,
            verbose=False
    ):
        if not str(path).endswith('.json'):
            raise ValueError('invalid cache file loc')
        self.path = path
        self._cache = None
        self.desync = True
        self.stale_timeout = stale_timeout
        self.verbose = verbose
        # atexit.register(self.dump_cache)

    @property
    def cache(self):
        if self._cache is None:
            if os.path.exists(self.path):
                with open(self.path) as f:
                    self._cache = json.load(f)
            else:
                self._cache = {}
        return self._cache

    @cache.setter
    def cache(self, val):
        self._cache = val
        self.dump_cache()

    def dump_cache(self):
        with open(self.path, mode='w') as f:
            json.dump(self._cache, f, indent=2)

    def is_stale(self, endpoint):
        if self.stale_timeout is None:
            return False

        return (datetime.now() - self.stale_timeout).timestamp() > self.cache[endpoint]['fetch_ts']

    def get_json(self, endpoint):
        if endpoint not in self.cache or self.is_stale(endpoint):
            if self.verbose:
                print(f'Requesting Resource: "{endpoint}"')
            self.cache |= {endpoint: {
                'data': requests.get(endpoint).json(),
                'fetch_ts': datetime.now().timestamp()
            }}

        return copy.deepcopy(self.cache[endpoint]['data'])
