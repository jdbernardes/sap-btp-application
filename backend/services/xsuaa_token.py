import os
import json
import requests


def get_xsuaa_token():
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    credentials = vcap['xsuaa'][0]['credentials']
    url = credentials['url'] + '/oauth/token'
    client_id = credentials['clientid']
    client_secret = credentials['clientsecret']

    response = requests.post(
        url,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
    )

    if not response.ok:
        raise Exception('XSUAA token fetch failed', response.text)
    
    return response.json()['access_token']