import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_xlm_account():
    headers = { 'x-api-key': API_KEY }
    
    conn.request("GET", "/v3/xlm/account", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_xlm_blockchain_information():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xlm/info", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_actual_blockchain_fee():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xlm/fee", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_xlm_transaction_by_hash(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xlm/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_transactions(path_params):
    validator.get_account_transactions(path_params, query_params = {})
    headers = { 'x-api-key': API_KEY }
    
    conn.request("GET", "/v3/xlm/account/tx/{}".format(path_params['account']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_info(path_params):
    validator.get_account_info(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/xlm/account/{}".format(path_params['account']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def send_xlm_from_address_to_address(body_params):
    validator.send_xlm_from_address_to_address(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xlm/transaction", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def broadcast_signed_xlm_transaction(body_params):
    validator.broadcast_signed_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xlm/broadcast", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_update_delete_xlm_trust_line(body_params):
    validator.create_update_delete_xlm_trust_line(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xlm/trust", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def modify_xlm_account(body_params):
    validator.modify_xlm_account(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xlm/account/settings", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))