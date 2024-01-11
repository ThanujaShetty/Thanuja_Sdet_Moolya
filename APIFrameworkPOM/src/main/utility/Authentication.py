import json
import random

import jsonpath
import requests

from Library.config import TestData
from src.main.utility.CreateURL import CreateURL


# def get_token():
#     url = CreateURL().get_url("/api-clients/")
#     num = random.randint(1, 1000)
#     data = {"clientName": "arnu", "clientEmail": f"thanu+{num}@example.com"}
#     response = requests.post(url, json=data)
#     assert response.status_code == 201
#     res = json.loads(response.text)
#     token = (jsonpath.jsonpath(res, "accessToken"))
#     return token[0]

def get_token():
    url = CreateURL().get_url("/api-clients/")
    num = random.randint(1, 1000)
    data = {"clientName": "arnu", "clientEmail": f"thanu+{num}+@example.com"}
    response = requests.post(url, json=data)
    if response.status_code != 201:
        raise Exception(
            "The response from the access token request failed with the status code: " + str(response.status_code) +
                " and the response body was: " + response.text)
    else:
        response_body = json.loads(response.text)
        token = response_body['accessToken']
        return token
