import http.client
import json
import validator.security as security_validator
import requests
import os
from dotenv import load_dotenv
load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']

def headers(for_post = False):
    if for_post:
        return {
            'content-type': "application/json",
            'x-api-key': API_KEY
            }
    else:
        return {
            'x-api-key': API_KEY
            }


def get_pending_transactions_to_sign(path_params):
    if security_validator.get_pending_transactions_to_sign(path_params):
        conn.request("GET", "/v3/kms/pending/{}".format(path_params['chain']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def complete_pending_transaction_to_sign(path_params):
    if security_validator.complete_pending_transaction_to_sign(path_params):
        conn.request("PUT", "/v3/kms/{}/{}".format(path_params['id'], path_params['txId']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def get_transaction_details(path_params):
    if security_validator.id_path_param(path_params):
        conn.request("GET", "/v3/kms/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def delete_transaction(path_params, query_params = {}):
    if security_validator.delete_transaction(path_params, query_params):
        if query_params != {}:
            conn.request("DELETE", "/v3/kms/{}?revert={}".format(path_params['id'], query_params['revert']), headers=headers())
        else:
            conn.request("DELETE", "/v3/kms/{}?revert=true".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")