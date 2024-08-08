import pytest
from os import environ as env

from moretunes.spotify import Spotify, WebSpotify, ACToken


@pytest.fixture(name='sp_acl')
def fixture_sp_wcl() -> Spotify:
    token = ACToken()
    return Spotify(token)


@pytest.fixture(name='spw_cl')
def fixture_sp_wcl() -> WebSpotify:

    return WebSpotify()
