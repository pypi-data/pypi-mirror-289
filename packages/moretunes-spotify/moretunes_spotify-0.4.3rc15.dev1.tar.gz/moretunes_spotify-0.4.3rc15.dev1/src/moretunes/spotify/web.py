import requests
import json
import hashlib
from .exceptions import EndpointError
from .tokens import RefreshingWebAccessToken


class UserWebSpotify:
    """Spotify Web API client for hidden endpoints with built-in refreshing access token"""

    def __init__(self, token: RefreshingWebAccessToken):
        self.token = token
        self._id = None

    @property
    def id(self):
        if not self._id:
            self._id = self.current_user()['id']
        return self._id

    def _fetch(self, url: str, rsp_key: str | None = None):
        resp = requests.get(
            url=url,
            headers={'Authorization': f'Bearer {self.token.access_token}'}
        )
        if not resp.ok:
            raise EndpointError()

        data = resp.json()
        return data.get(rsp_key) if rsp_key else data

    def _post(self, pack):
        url = f'https://api-partner.spotify.com/pathfinder/v1/query'
        resp = requests.post(
            url=url,
            headers={'Authorization': f'Bearer {self.token.access_token}'},
            json=pack
        )
        if not resp.ok:
            raise EndpointError()

        return resp.json()

    def current_user(self):
        url = 'https://api.spotify.com/v1/me'
        return self._fetch(url)

    def activity(self):
        url = 'https://guc-spclient.spotify.com/presence-view/v1/buddylist'
        return self._fetch(url, 'friends')

    def following(self, alt_user: str | None = None):
        user = alt_user if alt_user else self.id
        url = f'https://spclient.wg.spotify.com/user-profile-view/v3/profile/{user}/following?market=from_token'
        return self._fetch(url, 'profiles')

    def followers(self, alt_user: str | None = None):
        user = alt_user if alt_user else self.id
        url = f'https://spclient.wg.spotify.com/user-profile-view/v3/profile/{user}/followers?market=from_token'
        return self._fetch(url, 'profiles')

    def playlist_add(self, playlist_id: str, uris: list):
        pack = {
            "variables": {
                "uris": uris,
                "playlistUri": f"spotify:playlist:{playlist_id}",
                "newPosition": {
                    "moveType": "BOTTOM_OF_PLAYLIST",
                    "fromUid": None}},
            "operationName": "addToPlaylist",
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "47c69e71df79e3c80e4af7e7a9a727d82565bb20ae20dc820d6bc6f94def482d"}}}
        return self._post(pack)

    def playlist_insert(self, playlist_id: str, uris: list):
        pack = {
            "variables": {
                "uris": uris,
                "playlistUri": f"spotify:playlist:{playlist_id}",
                "newPosition": {
                    "moveType": "AFTER_UID",
                    "fromUid": "75463e0f175ba57e"}},
            "operationName": "addToPlaylist",
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "47c69e71df79e3c80e4af7e7a9a727d82565bb20ae20dc820d6bc6f94def482d"}}}
        return self._post(pack)


class ClientWebSpotify:
    """WebClientAPI for private API methods"""
    def __init__(self):
        self.core_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Accept': 'application/json', 'content-type': 'application/json'}
        self._client_token = None
        self._auth = None
        self.persist = None

    @property
    def headers(self):
        return self.core_headers | {
            'Authorization': f'Bearer {self.auth['accessToken']}',
            'client-token': self.client_token['token']
        }

    @property
    def auth(self):
        if not self._auth:
            resp = requests.get('https://open.spotify.com', headers=self.core_headers)
            # print('AUTH FETCH:', vars(resp.headers))
            page = resp.text
            start = page.find('{"accessToken":"')
            partial = page[start:page.find('}', start) + 1]
            self._auth = json.loads(partial)
        return self._auth

    @property
    def client_token(self):
        if not self._client_token:
            body = '{"client_data":{"client_id":"' + self.auth['clientId'] + '","js_sdk_data":{}}}'
            self.persist = hashlib.sha256(body.encode()).hexdigest()
            pr = requests.post('https://clienttoken.spotify.com/v1/clienttoken',
                               data=body, headers=self.core_headers)
            # print('TOKEN POST:', vars(pr.headers))
            self._client_token = pr.json()['granted_token']

        return self._client_token

    def _query_fetch(self, operation_pack: dict, url=''):
        url = 'https://api-partner.spotify.com/pathfinder/v1/query'
        params = {
            'operationName': operation_pack['name'],
            'variables': json.dumps(operation_pack['variables']),
            'extensions': json.dumps({
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": operation_pack['sha256']}
            })
        }
        resp = requests.get(url, params=params, headers=self.headers)
        # print('QUERY FETCH:', vars(resp.headers))
        return resp.json()

    def _api_fetch(self, endpoint: str, params: dict):
        url = f'https://api.spotify.com{endpoint}'
        resp = requests.get(url, params=params, headers=self.headers)
        return resp.json()

    def search(self, q):
        pack = {
            'name': 'searchDesktop',
            'variables': {
                "searchTerm": q,
                "offset": 0,
                "limit": 10,
                "numberOfTopResults": 5,
                "includeAudiobooks": False
            },
            'sha256': '7ca3ca85f5af2a16184bd0c222ba6342041f6d2e5c55b772f784366c1c8f7755'
        }

        return self._query_fetch(pack)

    def album(self, sp_bid: str):
        pack = {
            'name': 'getAlbum',
            'variables': {
                "uri": f"spotify:album:{sp_bid}",
                "locale": "",
                "offset": 0,
                "limit": 50
            },
            'sha256': "01c6295923a9603d5a97eb945fc7e54d6fb5129ea801b54321647abe0d423c25"
        }
        data = self._query_fetch(pack)['data']['albumUnion']
        data['id'] = data['uri'].rsplit(':', 1)[-1]
        return data

    def album_tracks(self, sp_bid: str):
        pack = {
            'name': 'queryAlbumTracks',
            'variables': {
                "uri": f"spotify:album:{sp_bid}",
                "offset": 0,
                "limit": 300
            },
            'sha256': 'd64c60c66bff2726868dc0a05ddbd54b0fe744680cf7fef97ed7469d1c353b1f',
        }
        return self._query_fetch(pack)['data']['albumUnion']

    def recommendations(self, sp_tid: str):
        pack = {
            'name': 'internalLinkRecommenderTrack',
            'variables': {
                "uri": f"spotify:track:{sp_tid}",
                "strategy": "CONTENT_ONLY"},
            'sha256': "97f52864d50ba62ab761a7bff47f1a9921d9e357316f7d60ad84ae3788eea4cf"
        }
        return self._query_fetch(pack)

    def track(self, sp_tid):
        pack = {
            'name': 'getTrack',
            'variables': {"uri": f"spotify:track:{sp_tid}"},
            'sha256': 'e101aead6d78faa11d75bec5e36385a07b2f1c4a0420932d374d89ee17c70dd6'
        }
        return self._query_fetch(pack)

    def tracks(self, sp_tids: list[str], market='US'):
        endpoint = '/v1/tracks'
        pack = {
            'ids': ','.join(sp_tids),
            'market': market
        }
        return self._api_fetch(endpoint, pack)['tracks']

    def fetch_entities(self, sp_uris: list[str]):
        pack = {
            'name': 'fetchEntitiesForRecentlyPlayed',
            'variables': {
                "uris": sp_uris},
            'sha256': '536679a239ba7a37855e198c90c3f544282f81754cbaed2f758e5a2221369122'
        }
        return self._query_fetch(pack)

    def playlist_meta(self, sp_pid: str):
        pack = {
            'name': 'fetchPlaylistMetadata',
            'variables': {
                "uri": f"spotify:playlist:{sp_pid}",
                "offset": 0,
                "limit": 100},
            'sha256': '8a4f7d81136b3c8662cf78384ea8e1a8af149560cb6e161a788d43786bdcf7c9'
        }
        return self._query_fetch(pack)
