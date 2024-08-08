import tekore as tk
import httpx
from os import environ as env


class Spotify(tk.Spotify):
    """Moretunes wrapper for Tekore.Spotify"""


# TODO: rework
class SuperCred:
    def __init__(
            self,
            client=env.get('SPOTIFY_ID', None),
            secret=env.get('SPOTIFY_SECRET', None),
            uri=env.get('SPOTIFY_URI', None),
    ):
        self.client = client
        self.secret = secret
        self.uri = uri

    @property
    def cred(self):
        return tk.RefreshingCredentials(self.client, self.secret, self.uri, sender=tk.RetryingSender(2))


class Tuned:
    @classmethod
    def from_db(cls, pack: dict):
        return cls(
            super_cred=SuperCred(
                client=pack['client'],
                secret=pack['secret'],
                uri=pack.get('uri', [None])[0]
            ),
            rf_tk=pack['refresh_token']
        )

    def __init__(self, super_cred=None, rf_tk=None):
        self._refresh_token = rf_tk if rf_tk else env['RF_TK']
        self._sc = super_cred if super_cred else SuperCred()
        self._token = None
        self._sp = tk.Spotify(self.token, max_limits_on=True, sender=tk.RetryingSender(retries=2))
        self._sid = None

    @property
    def sid(self):
        if not self._sid:
            self._sid = self.sp.current_user().id
        return self._sid

    @property
    def token(self):
        if not self._token or self._token.is_expiring:
            self._token = self._sc.cred.refresh_user_token(self._refresh_token)
        return self._token

    @property
    def sp(self):
        trans = httpx.HTTPTransport(retries=3)
        client = httpx.Client(timeout=20, transport=trans)
        sender = tk.RetryingSender(retries=3, sender=tk.SyncSender(client=client))
        return tk.Spotify(self.token, sender=sender, max_limits_on=True)

    @property
    def asp(self):
        # FIXME: This feels wrong
        trans = httpx.AsyncHTTPTransport(retries=3)
        client = httpx.AsyncClient(timeout=20, transport=trans)
        sender = tk.RetryingSender(retries=3, sender=tk.AsyncSender(client=client))
        return tk.Spotify(self.token, sender=sender, max_limits_on=True)
