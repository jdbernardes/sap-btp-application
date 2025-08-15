import requests
from .xsuaa_token import get_xsuaa_token


def get_destination(destination_name = 'SFSF_TEST'):
    token = get_xsuaa_token()

    response = requests.get(
        f"https://destination-configuration.cfapps.eu10.hana.ondemand.com/destination-configuration/v1/destinations/{destination_name}",
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    if not response.ok:
        raise Exception('Failed to fetch destination', response.text)
    
    return response.json()