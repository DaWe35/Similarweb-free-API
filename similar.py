try:
    from requests import get
    from urllib.parse import urlparse
except ImportError as err:
    print(f"Failed to import required modules {err}")
    
def similarGet(website):
    parsed_uri = urlparse(website)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    ENDPOINT = 'https://api.similarweb.com/v1/SimilarWebAddon/' + domain + '/all' 
    resp = get(ENDPOINT)

    if resp.status_code == 200:
        return resp.json()
    else:
        resp.raise_for_status()
        return False
    