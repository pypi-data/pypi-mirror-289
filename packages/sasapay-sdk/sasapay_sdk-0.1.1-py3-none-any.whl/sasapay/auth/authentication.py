

import requests
from requests.auth import HTTPBasicAuth


def authenticate(base_url, client_id, client_secret):
    url = f'{base_url}/api/v1/auth/token/'
    params = {'grant_type': 'client_credentials'}
    response = requests.get(url,
                            auth=HTTPBasicAuth(client_id, client_secret), params=params)
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    return None
