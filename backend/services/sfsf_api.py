import requests
from .destination_client import get_destination


def get_random_user():
    dest = get_destination()
    base_url = dest['destinationConfiguration']['URL']
    auth_token = dest['authTokens'][0]['value']

    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Accept': 'application/json'
    }

    response = requests.get(
        f'{base_url}/User?$top = 1',
        headers=headers
    )

    if not response.ok:
        raise Exception("SFSF API call failed", response.text)
    
    return response.json()