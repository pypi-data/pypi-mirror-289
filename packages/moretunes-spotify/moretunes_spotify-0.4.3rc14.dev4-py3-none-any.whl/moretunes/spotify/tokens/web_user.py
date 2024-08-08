from tekore._auth.expiring import AccessToken
from http.cookiejar import CookieJar
import requests
from time import time

from ..exceptions import TokenError


class RefreshingWebAccessToken(AccessToken):
    _refresh_url = 'https://open.spotify.com/get_access_token?reason=transport&productType=web_player'

    def __init__(self, sp_dc: str | CookieJar):
        self._cookie = {'sp_dc': sp_dc} if isinstance(sp_dc, str) else sp_dc
        self._token: str | None = None
        self.expires_at: int = 0

    @property
    def is_expiring(self):
        # token expires in less than 5 mins boolean
        return self.expires_in < 60 * 5

    @property
    def expires_in(self):
        return self.expires_at - int(time())

    @property
    def access_token(self):
        if not self._token or self.is_expiring:
            self._refresh()
        return self._token

    def _refresh(self):
        resp = requests.get(self._refresh_url, cookies=self._cookie)

        if not resp.ok:
            raise TokenError()

        if not isinstance(self._cookie, CookieJar):
            self._cookie = resp.cookies

        data = resp.json()
        self._token = data['accessToken']
        self.expires_at = data['accessTokenExpirationTimestampMs'] // 1_000

    @property
    def header(self):
        return {'Authorization': f'Bearer {self.access_token}'}