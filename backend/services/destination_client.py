import base64
import os
import json
import requests


def _get_destination_service_token_and_uri():
    # Use the DESTINATION binding credentials, not app xsuaa
    vcap = json.loads(os.getenv("VCAP_SERVICES"))
    creds = vcap["destination"][0]["credentials"]

    token_resp = requests.post(
        creds["url"] + "/oauth/token",              # same auth domain
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "client_id": creds["clientid"],
            "client_secret": creds["clientsecret"],
        },
        timeout=30,
    )
    if not token_resp.ok:
        raise Exception("Failed to get Destination token", token_resp.text)

    access_token = token_resp.json()["access_token"]
    # Destination Configuration API base
    dest_api_base = creds["uri"]  # e.g. https://destination-configuration.cfapps.us10.hana.ondemand.com
    return access_token, dest_api_base

def get_destination(destination_name: str = "SFSF_TEST") -> dict:
    token, dest_api_base = _get_destination_service_token_and_uri()
    resp = requests.get(
        f"{dest_api_base}/destination-configuration/v1/destinations/{destination_name}",
        headers={"Authorization": f"Bearer {token}"},
        timeout=30,
    )
    if not resp.ok:
        raise Exception("Failed to fetch destination", resp.text)
    return resp.json()

def create_autorization(destination_name: str = "SFSF_TEST"):
    dest = get_destination(destination_name)
    cfg = dest["destinationConfiguration"]

    base_url = cfg["URL"]  # e.g. https://<sfsf>/odata/v2
    auth_type = cfg.get("Authentication")
    auth = ""

    if auth_type == "BasicAuthentication":
        user = cfg.get("User")
        pwd  = cfg.get("Password")
        if not user or not pwd:
            raise Exception("Destination is BasicAuthentication but User/Password are missing.")
        token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
        auth = f"Basic {token}"
    else:
        # For OAuth destinations, you might use dest["authTokens"][0]["value"]
        # but not for BasicAuthentication.
        pass

    return{
        'base_url' : base_url,
        'authorization': auth
    }