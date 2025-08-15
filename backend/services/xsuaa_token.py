import os
import json
import requests


def get_xsuaa_token():
    if os.getenv("VCAP_SERVICES") is None:
        os.environ["VCAP_SERVICES"] = json.dumps({
            "xsuaa": [
                {
                    "credentials": {
                        "clientid": "sb-fastapi-app!t499921",
                        "clientsecret": "438bb9e3-c313-42d3-ba55-6328e5c708ef$aAV9SbJFpgNOZm7vmMIhxtL9LMmH2a7_Xjjngg6tFpg=",
                        "url": "https://d32b58f2trial.authentication.us10.hana.ondemand.com",
                        "xsappname": "fastapi-app!t499921"
                    }
                }
            ],
            "destination": [
                {
                    "credentials": {
                        "clientid": "sb-clone3b81feeb87b945d6bc7e5b5b992bc554!b499921|destination-xsappname!b62",
                        "clientsecret": "a75235a7-9d9e-4f1f-89d9-2dffdf5be960$pKoBADnsh-HCp5KIkfJV7fedWJLp7tBDVadRel-ZAAg=",
                        "uri": "https://destination-configuration.cfapps.us10.hana.ondemand.com",
                        "url": "https://d32b58f2trial.authentication.us10.hana.ondemand.com",
                        "xsappname": "clone3b81feeb87b945d6bc7e5b5b992bc554!b499921|destination-xsappname!b62"
                    }
                }
            ]
        })
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