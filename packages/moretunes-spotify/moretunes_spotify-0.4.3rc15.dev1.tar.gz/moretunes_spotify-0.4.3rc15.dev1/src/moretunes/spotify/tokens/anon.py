import time
import json
import requests
from typing import TypedDict
import random

from ..exceptions import TokenError
from tekore import AccessToken, RefreshingToken


class ExtractedToken(TypedDict):
    accessToken: str
    accessTokenExpirationTimestampMs: int
    isAnonymous: bool
    clientId: str


class RefreshingAnonToken:
    def __init__(self):
        self._access_token: str = ''   #: token
        self._expires_at: int = 0      #: time till expiration in seconds
        self.client_id: str = ''       #: current client id
        self.anonymous: bool = True    #: anonymity status

    def __str__(self):
        """ Token value """
        return self.access_token

    @property
    def headers(self):
        user_agent = random.choice([
            f'(Windows NT 1{random.randint(0, 1)}.0; Win64; x64)',
            f'(Macintosh; Intel Mac OS X {random.randint(800, 1015) / 100}; rv:{random.randint(80, 120)}.0)',
            f'(X11; {random.choice(['', 'Fedora; ', 'Ubuntu; '])}Linux x86_64; rv:{random.randint(80, 120)}.0)',
        ])
        return {
            'User-Agent': user_agent,
            'Accept': 'application/json', 'content-type': 'application/json'}

    @property
    def access_token(self):
        if not self._access_token or self.is_expiring:
            self.fetch_token()
        return self._access_token

    @property
    def expires_in(self):
        return int(self.expires_at - time.time())

    @property
    def expires_at(self):
        return self._expires_at

    @property
    def is_expiring(self):
        return self.expires_in < 60     # check if expiring in less than 60 seconds

    def fetch_token(self, retries=3):
        resp = requests.get('https://open.spotify.com', headers=self.headers)
        if resp.status_code != 200:
            if retries > 0:
                return self.fetch_token(retries - 1)
            raise TokenError(f'Token retrieval error. Status Code: {resp.status_code}, Response: {vars(resp)}')
        page = resp.text
        start = page.find('{"accessToken":"')
        raw_token: ExtractedToken = json.loads(page[start:page.find('}', start) + 1])
        self._access_token = raw_token['accessToken']
        self._expires_at = raw_token['accessTokenExpirationTimestampMs'] // 1000
        self.client_id = raw_token['clientId']
        self.anonymous = raw_token['isAnonymous']
