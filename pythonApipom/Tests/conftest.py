import json
import random
from urllib.parse import urljoin
import jsonpath
import requests
from Library.config import Config, TestData
from src.Basepage import CommanActions


def get_access_token(self,):
    num = random.randint(1, 100000)
    body = {"clientName": "ram", "clientEmail": f"ram+{num}@example.com"}
    res = CommanActions.post_with_body(body)
    token_list = jsonpath.jsonpath(res, "accessToken")
    token = token_list[0]
    print(token)
    return token


