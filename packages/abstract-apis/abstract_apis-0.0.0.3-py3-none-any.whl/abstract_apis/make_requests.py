import json
import requests
from abstract_utilities import *

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

def ensure_json(data):
    if isinstance(data, str):
        try:
            json.loads(data)  # Verify it's valid JSON
            return data
        except ValueError:
            pass  # Not valid JSON, continue to dump it
    return json.dumps(data)

def stripit(string, chars=[]):
    string = string or ''
    for char in make_list(chars):
        string = string.strip(char)
    return string

def make_endpoint(endpoint):
    return stripit(endpoint, chars='/')

def make_url(url):
    return stripit(url, chars='/')

def get_url(url, endpoint=None):
    return stripit(f"{make_url(url)}/{make_endpoint(endpoint)}", chars='/')

def get_text_response(response):
    try:
        return response.text
    except Exception as e:
        print(f"Could not read text response: {e}")
        return None

def get_json_response(response, response_result=None):
    response_result=response_result or 'result'
    try:
        response_json = response.json()
        result_response = response_json.get(response_result, None)
        if result_response is not None:
            return result_response
        # Fallback to the last key if 'result' is not found
        last_key = list(response_json.keys())[-1] if response_json else None
        return response_json.get(last_key, None)
    except Exception as e:
        print(f"Could not read JSON response: {e}")
        return None

def get_status_code(response):
    try:
        return response.status_code
    except Exception as e:
        print(f"Could not get status code: {e}")
        return None

def get_response(response, response_result=None,raw_response=False):
    if raw_response:
        return response
    json_response = get_json_response(response, response_result=response_result)
    if json_response is not None:
        return json_response
    text_response = get_text_response(response)
    if text_response:
        return text_response
    return response.content  # Return raw content as a last resort

def make_request(url, method='GET', data=None, headers=None, endpoint=None, result='result', status_code=False,raw_response=False,response_result=None):
    url = get_url(url, endpoint=endpoint)
    if headers is None:
        headers = get_headers()
    data = ensure_json(data)

    try:
        if method.upper() == 'POST':
            response = requests.post(url, data=data, headers=headers)
        elif method.upper() == 'GET':
            response = requests.get(url, params=data, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
    except Exception as e:
        print(f"Could not make {method} request: {e}")
        if status_code:
            return None, None
        return None

    if status_code:
        return get_response(response, result=result,raw_response=raw_response,response_result=response_result), get_status_code(response)
    return get_response(response, result=result,raw_response=raw_response,response_result=response_result)

def getPostRequest(url, data, headers=None, endpoint=None, result='result', status_code=False):
    return make_request(url, method='POST', data=data, headers=headers, endpoint=endpoint, result=result, status_code=status_code,response_result=None)

def getGetRequest(url, data, headers=None, endpoint=None, result='result', status_code=False):
    return make_request(url, method='GET', data=data, headers=headers, endpoint=endpoint, result=result, status_code=status_code,response_result=None)
