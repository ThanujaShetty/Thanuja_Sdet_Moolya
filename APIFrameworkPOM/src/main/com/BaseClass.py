import requests
from src.main.utility.CreateURL import CreateURL


obj_url = CreateURL()

class BaseClass:
    def post_call(self, request_url,json=None,params=None,headers=None):
        response = requests.post(request_url,json=json, params=params, headers=headers)
        if response.status_code != 201:
            raise Exception(
                "Failure while submitting order, status code: "+ str(response.status_code) +
                " and the response body was: " + response.text)
        else:
            return response

    def get_call(self, request_url, headers=None, params=None, auth=None):
        response =  requests.get(request_url, headers=headers, params=params, auth=auth)
        if response.status_code != 200:
            raise Exception(
                "Failure while getting order details, status code: "+ str(response.status_code) +
                " and the response body was: " + response.text)
        else:
            return response

    def patch_call(self, request_url, data=None, json=None, headers=None):
        response =  requests.patch(request_url, data=data, json=json, headers=headers)
        if response.status_code != 204:
            raise Exception(
                "Failure while updating order details, status code: "+ str(response.status_code) +
                " and the response body was: " + response.text)
        else:
            return response


    def delete_call(self, request_url, headers=None):
        response = requests.delete(request_url, headers=headers)
        if response.status_code != 204:
            raise Exception(
                "Failure while updating order details, status code: "+ str(response.status_code) +
                " and the response body was: " + response.text)
        else:
            return response

    def put_call(self, request_url,headers=None):
        response = requests.delete(request_url,json=None, headers=headers)
        if response.status_code != 204:
            raise Exception(
                "Failure while updating order details, status code: " + str(response.status_code) +
                " and the response body was: " + response.text)
        else:
            return response