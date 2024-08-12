import json
import requests

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

def getPostRequest(url, data, headers=None):
    if headers is None:
        headers = get_headers()
    data = ensure_json(data)
    response = requests.post(url, data=data, headers=headers)
    return response.json()

def getGetRequest(url, data, headers=None):
    if headers is None:
        headers = get_headers()
    data = ensure_json(data)
    response = requests.get(url, data=data, headers=headers)
    return response.json()
