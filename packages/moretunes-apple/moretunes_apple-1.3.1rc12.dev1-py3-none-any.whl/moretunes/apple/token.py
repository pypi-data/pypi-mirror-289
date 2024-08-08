from time import time
import requests
import jwt
from datetime import datetime, timedelta
from typing import Optional


class Token:
    def __init__(self, key: bytes, key_id: str, team_id: str, origins: Optional[list[str]] = None):
        self.key = key
        self.key_id = key_id
        self.team_id = team_id
        self.origins = origins
        self.header = {'alg': 'ES256', 'kid': self.key_id}
        self._token = None
        self.expires_at = -1

    @property
    def token(self):
        if not self._token or (self.expires_at + 5 * 60) < time():
            self.regen()

        return self._token

    def regen(self):
        payload = {
            'iss': self.team_id,
            'iat': int(datetime.now().timestamp()),
            'exp': int((datetime.now() + timedelta(hours=6)).timestamp()),
        }

        if self.origins is not None:
            payload['origins'] = self.origins

        self._token = jwt.encode(payload, self.key, 'ES256', self.header)
        self.expires_at = payload['exp']


class APIException(Exception):
    """API error"""


class MTAppleMusic:
    api_base = 'https://api.music.apple.com'

    def __init__(self, auth: Token):
        self.auth = auth

    @property
    def headers(self):
        return {'Authorization': f'Bearer {self.auth.token}'}

    def _api_request(
            self,
            endpoint: str,
            method: str = 'GET',
            params: dict | None = None,
            body: dict | None = None,
            user_token: str | None = None
    ) -> tuple[int, dict | str | bytes]:

        # build headers to match request type
        headers = self.headers
        if user_token:
            headers |= {'Music-User-Token': user_token}

        resp = requests.request(
            method=method,
            url=f'{self.api_base}{endpoint}',
            params=params,
            json=body,
            headers=headers
        )

        # successful requests and errors response both return json, others none
        # if resp.status_code < 400 or resp.status_code == 500:
        #     return resp.status_code, resp.json()

        return resp.status_code, resp.json()

