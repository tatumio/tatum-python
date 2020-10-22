import http.client
import json
import validator.blockchain as blockchain_validator
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

def generate_xlm_account():    
    conn.request("GET", "/v3/xlm/account", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_xlm_blockchain_information():
    conn.request("GET", "/v3/xlm/info", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_actual_blockchain_fee():
    conn.request("GET", "/v3/xlm/fee", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_xlm_transaction_by_hash(path_params):
    if blockchain_validator.get_block_by_hash_or_height(path_params):
        conn.request("GET", "/v3/xlm/transaction/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_account_transactions(path_params):
    if blockchain_validator.get_account_transactions(path_params, query_params = {}):    
        conn.request("GET", "/v3/xlm/account/tx/{}".format(path_params['account']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_account_info(path_params):
    if blockchain_validator.get_account_info(path_params):
        conn.request("GET", "/v3/xlm/account/{}".format(path_params['account']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def send_xlm_from_address_to_address(body_params):
    if blockchain_validator.send_xlm_from_address_to_address(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/xlm/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def broadcast_signed_xlm_transaction(body_params):
    if blockchain_validator.broadcast_signed_transaction(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/xlm/broadcast", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def create_update_delete_xlm_trust_line(body_params):
    if blockchain_validator.create_update_delete_xlm_trust_line(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/xlm/trust", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def modify_xlm_account(body_params):
    if blockchain_validator.modify_xlm_account(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/xlm/account/settings", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")