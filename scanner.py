import requests
from os import getenv

def get_new_tokens():
    api_key = getenv("BIRDEYE_API_KEY")
    url = 'https://public-api.birdeye.so/public/tokenlist'
    headers = {'X-API-KEY': api_key}
    res = requests.get(url, headers=headers)
    tokens = res.json().get("data", {}).get("tokens", [])
    filtered = [
        t for t in tokens
        if float(t.get('liquidity', 0)) > 5 and int(t.get('unique_buyers', 0)) > 100
    ]
    return filtered[:5]