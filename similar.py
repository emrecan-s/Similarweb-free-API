try:
    from requests import get
    from urllib.parse import urlparse
except ImportError as err:
    print(f"Failed to import required modules {err}")

def similarGet(website):
   
    ENDPOINT = 'https://api.similarweb.com/v1/SimilarWebAddon/' + website + '/all' 
    resp = get(ENDPOINT)

    if resp.status_code == 200:
        return resp.json()
    else:
       
        return resp.status_code
    