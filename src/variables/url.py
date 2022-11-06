from variables.types import StrDict

baseUrl: str = "https://www.amazon.com/s"
loginUrl: str = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"

params: StrDict = {
    "k": "computer+monitor",
    "sprefix": "compu%2Caps%2C451",
    "ref": "nav_signin",
}

headers: StrDict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
}

cookies: StrDict = {
    "session-token": "G1rM4xxxdjwzHtLw/EXSuuNOD1qwyMz0YEm8IEO6VtJdwqUA7pmQhkVJ+v+IeANmdCr0M4DE24TvsC3rnQD26YO1LD2k7p1TIPkisjUmxBleYCqk10K457r+gxcnWIX/5MTvH6JEw0XQ/ZtwFDiyNUB2au+ltBsGLJX504eh2ojkHhoStLOy7HkbZQoO3Eqh9OTrSUU4KiOlZ0rLNpkF9Zq6Mn1I4JwaSqqvqzQn9xvi9PoygjAXQnkH4PlY12UDYwA1eLlGudn1I8zexNFL/Q=="
}
