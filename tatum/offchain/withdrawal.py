import http.client
import json
import validator.offchain as offchain_validator
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
            

def store_withdrawal(body_params):
    if offchain_validator.store_withdrawal(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/offchain/withdrawal", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def complete_withdrawal(path_params):
    if security_validator.complete_pending_transaction_to_sign(path_params):
        conn.request("PUT", "/v3/offchain/withdrawal/{}/{}".format(path_params['id'], path_params['txId']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def cancel_withdrawal(path_params, query_params = {}):
    if security_validator.delete_transaction(path_params, query_params):
        if query_params != {}:
            conn.request("DELETE", "/v3/offchain/withdrawal/{}?revert={}".format(path_params['id'], query_params['revert']), headers=headers())
        else:
            conn.request("DELETE", "/v3/offchain/withdrawal/{}?revert=true".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")

def broadcast_signed_transaction_and_complete_withdrawal(body_params):
    if offchain_validator.broadcast_signed_transaction_and_complete_withdrawal(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/offchain/withdrawal/broadcast", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def check_withdrawal(body_params):
    if offchain_validator.store_withdrawal(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/offchain/withdrawal/ethereum/hint", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
