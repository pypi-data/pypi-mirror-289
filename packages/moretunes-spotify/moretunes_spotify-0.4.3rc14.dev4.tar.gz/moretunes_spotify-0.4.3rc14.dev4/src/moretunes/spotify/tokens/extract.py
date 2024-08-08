import browser_cookie3
from http.cookiejar import CookieJar
from typing import Literal

from moretunes.spotify.exceptions import CookieFailure


def from_browser(
        browser: Literal['firefox', 'chrome', 'safari', 'edge'] | None = 'DEFAULT'
) -> CookieJar:

    match browser:
        case 'firefox':
            cookies = browser_cookie3.Firefox(domain_name='.spotify.com').load()
        case 'chrome':
            cookies = browser_cookie3.Chrome(domain_name='.spotify.com').load()
        case 'safari':
            cookies = browser_cookie3.Safari(domain_name='.spotify.com').load()
        case 'edge':
            cookies = browser_cookie3.Edge(domain_name='.spotify.com').load()
        # default and None
        case _:
            cookies = browser_cookie3.load('.spotify.com')

    sp_dc = next((x for x in cookies if x.name == 'sp_dc'), None)
    if not sp_dc:
        raise CookieFailure()

    jar = CookieJar()
    jar.set_cookie(sp_dc)

    return jar
