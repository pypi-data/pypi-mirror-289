from typing import Literal, get_args

from moretunes.apple import Token, MTAppleMusicAPI
from os import environ as env


SearchTypes = Literal[
    'activities', 'albums', 'apple-curators', 'artists', 'curators',
    'music-videos', 'playlists', 'record-labels', 'songs', 'stations'
]

AllowedSearchTypes = Literal['ANY'] | SearchTypes


class SimpleAPI:
    @classmethod
    def from_env(cls, overrides: dict | None = None):
        """
        Pulls all init args from environment. Keys used are:
        "MT_AM_KEY",
        "MT_AM_KID",
        "MT_AM_TID",
        "MT_AM_ORIGINS",
        "MT_AM_USER",
        "MT_AM_STORE"
        """
        with open(env['MT_AM_KEY'], 'rb') as key_file:
            key = key_file.read()

        return cls(
            token=Token(key, key_id=env['MT_AM_KID'], team_id=env['MT_AM_TID'], origins=env.get('MT_AM_ORIGINS')),
            user=env.get('MT_AM_USER'),
            storefront=env.get('MT_AM_STORE')
        )

    def __init__(self, token: Token, user: str | None = None, storefront: str | None = None):
        self.api = MTAppleMusicAPI(auth=token)
        self.user = user
        self._storefront = storefront

    @property
    def storefront(self):
        if self._storefront is None:
            data = self.api.get_storefront_any(self.user)
            self._storefront = data.data[0].id
        return self._storefront

    def search(self, query: str, types: list[SearchTypes] | AllowedSearchTypes = 'ANY', offset: int = 0, limit: int = 25):

        if isinstance(types, str):
            if types == 'ANY':
                types = get_args(SearchTypes)
            elif types in get_args(SearchTypes):
                types = [types]

        out = self.api.get_search_any(self.storefront, query, types, offset=str(offset), limit=limit)
        return out
