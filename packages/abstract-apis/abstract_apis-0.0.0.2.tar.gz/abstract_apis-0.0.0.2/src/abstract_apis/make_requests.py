import json
import requests
from abstract_utilities import *
def get_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

def ensure_json(data):
    # Check if the data is already a JSON string
    if isinstance(data, str):
        try:
            json.loads(data)  # Verify it's valid JSON
            return data
        except ValueError:
            pass  # Not valid JSON, continue to dump it
    # If it's not a string, or not valid JSON, dump it
    return json.dumps(data)

def stripit(string,chars=[]):
    string = string or ''
    for char in make_list(chars):
        string = string.strip(char)
    return string

def make_endpoint(endpoint):
  return stripit(endpoint,chars='/')

def make_url(url):
    return stripit(url,chars='/')

def get_url(url,endpoint=None):
    return stripit(f"{make_url(url)}/{make_endpoint(endpoint)}",chars='/')

def getPostRequest(url, data, headers=None,endpoint=None):
    if headers is None:
        headers = get_headers()
    data = ensure_json(data)
    url = get_url(url,endpoint=endpoint)
    response = requests.post(url, data=data, headers=headers)
    return response.json()

def getGetRequest(url, data, headers=None,endpoint=None):
    if headers is None:
        headers = get_headers()
    data = ensure_json(data)
    url = get_url(url,endpoint=endpoint)
    response = requests.get(url, data=data, headers=headers)
    return response.json()
