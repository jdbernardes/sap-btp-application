import base64
import requests
from .destination_client import get_destination

def get_random_user():
    dest = get_destination("SFSF_TEST")
    cfg = dest["destinationConfiguration"]

    base_url = cfg["URL"]  # e.g. https://<sfsf>/odata/v2
    auth_type = cfg.get("Authentication")
    headers = {"Accept": "application/json"}

    if auth_type == "BasicAuthentication":
        user = cfg.get("User")
        pwd  = cfg.get("Password")
        if not user or not pwd:
            raise Exception("Destination is BasicAuthentication but User/Password are missing.")
        token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
        headers["Authorization"] = f"Basic {token}"
    else:
        # For OAuth destinations, you might use dest["authTokens"][0]["value"]
        # but not for BasicAuthentication.
        pass

    resp = requests.get(f"{base_url}/User?$top=1", headers=headers, timeout=30)
    if not resp.ok:
        raise Exception("SFSF API call failed", resp.text)
    return resp.json()
