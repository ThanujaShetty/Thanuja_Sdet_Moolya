import json
from urllib.parse import urljoin

import requests

from Library.config import Config, TestData


class CommanActions:

    def post_with_body(self,body):
        response = requests.post(urljoin(Config.BASE_URL, TestData.Authentication_end_point),json=body)
        res = json.loads(response.text)

    def get_staus(self):
        response = requests.get(urljoin(Config.BASE_URL, endpoint))
        res = json.loads(response.text)