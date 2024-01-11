import json
import pytest

from src.main.com.BaseClass import obj_url,BaseClass
from src.main.utility.Authentication import get_token
from src.main.utility.payloadconverter import json_helper

obj_baseclass = BaseClass()


@pytest.mark.smoke
def test_submit_order():
    global order_id
    global token
    token = get_token()
    headers = {
        'Authorization': 'Bearer ' + token}
    body = json_helper().jsonreader('get_payload.json')
    url = obj_url.get_url("/orders")
    res = obj_baseclass.post_call(url, json=body, headers=headers)
    response_body = json.loads(res.text)
    order_id = response_body['orderId']
    return order_id

@pytest.mark.smoke
def test_get_order():
    headers = {
        'Authorization': 'Bearer ' + token}
    url = obj_url.get_url("/orders/" + order_id)
    res = obj_baseclass.get_call(url, headers=headers)
    response_body = json.loads(res.text)
    return response_body

@pytest.mark.smoke
def test_update_order():
    headers = {
        'Authorization': 'Bearer ' + token}
    body = json_helper().jsonreader('update_order.json')
    url = obj_url.get_url("/orders/" + order_id)
    res = obj_baseclass.patch_call(url, json=body, headers=headers)
    status_code = res.status_code
    print(status_code)
    return status_code

@pytest.mark.smoke
def test_delete_order():
    headers = {
        'Authorization': 'Bearer ' + token}
    url = obj_url.get_url("/orders/" + order_id)
    res = obj_baseclass.delete_call(url, headers=headers)
    status_code = res.status_code
    print("order is deleted", status_code)
    return status_code