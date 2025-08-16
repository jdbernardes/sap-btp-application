import json
import base64
import requests
from .destination_client import get_destination, create_autorization

def get_random_user():
    auth = create_autorization()
    base_url = auth['base_url']
    headers = {
        'Accept': 'application/json',
        'Authorization': auth['authorization']
    }

    resp = requests.get(f"{base_url}/User?$top=1", headers=headers, timeout=30)
    if not resp.ok:
        raise Exception("SFSF API call failed", resp.text)
    return resp.json()


def get_single_user(username:str):
    auth = create_autorization()
    base_url = auth['base_url']
    headers = {
        'Accept': 'application/json',
        'Authorization': auth['authorization']
    }
    uri = f"""
        {base_url}/User?$filter=username eq '{username}'
    """
    resp = requests.get(uri, headers=headers, timeout=30)
    if not resp.ok:
        raise Exception("SFSF API call failed", resp.text)
    return resp.json()

def get_users(filter:str, page_size:int):
    auth = create_autorization()
    base_url = auth['base_url']
    headers = {
        'Accept': 'application/json',
        'Authorization': auth['authorization']
    }
    uri = f"""
        {base_url}/User?$filter={filter}&paging=snapshot&customPageSize={page_size}'
    """
    resp = requests.get(uri, headers=headers, timeout=30)
    data = resp.json()
    all_results = data.get('d', {}).get('results', [])
    next_link = data.get('d',{}).get('__next')
    while next_link:
        resp = requests.get(next_link, headers=headers)
        data = resp.json()
        all_results.extend(data.get('d', {}).get('results', []))
        next_link = data.get('d',{}).get('__next')
    return all_results

def create_user(body):
    auth = create_autorization()
    base_url = auth['base_url']
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth['authorization'],
        'Accept': 'application/json'
    }
    uri = f"{base_url}/upsert?$format=json"
    resp = requests.post(url=uri, headers=headers, data=body)
    result = resp.json()
    return {'response': result}