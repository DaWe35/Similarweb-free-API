try:
    from requests import get
    from urllib.parse import urlparse
except ImportError as err:
    print(f"Failed to import required modules {err}")

def similarGet(website):
    domain = '{uri.netloc}'.format(uri=urlparse(website))
    domain = domain.replace("www.", "")
    ENDPOINT = 'https://api.similarweb.com/v1/SimilarWebAddon/' + domain + '/all' 
    resp = get(ENDPOINT)

    if resp.status_code == 200:
        return resp.json()
    else:
        resp.raise_for_status()
        return False
    