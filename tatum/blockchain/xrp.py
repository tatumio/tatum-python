import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_xrp_account():
    headers = { 'x-api-key': API_KEY }
    
    conn.request("GET", "/v3/xrp/account", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_xrp_blockchain_information():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xrp/info", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_actual_blockchain_fee():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xrp/fee", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_xrp_transaction_by_hash(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xrp/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_transactions(path_params, query_params = {}):
    validator.get_account_transactions(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    min = ''
    if 'min' in query_params.keys():
        min = 'min={}'.format(query_params['min'])
    marker = ''
    if 'marker' in query_params.keys():
        marker = 'marker={}'.format(query_params['marker'])

    conn.request("GET", "/v3/xrp/account/tx/{}?{}&{}".format(path_params['account'], min, marker), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_info(path_params):
    validator.get_account_info(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/xrp/account/{}".format(path_params['account']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_balance(path_params):
    validator.get_account_info(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/xrp/account/{}/balance".format(path_params['account']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def get_ledger(path_params):
    validator.get_ledger(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/xrp/ledger/{}".format(path_params['i']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def send_xrp_to_blockchain_addresses(body_params):
    validator.send_xrp_to_blockchain_addresses(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xrp/transaction", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def broadcast_signed_xrp_transaction(body_params):
    validator.broadcast_signed_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xrp/broadcast", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_update_delete_xrp_trust_line(body_params):
    validator.create_update_delete_xrp_trust_line(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xrp/trust", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def modify_xrp_account(body_params):
    validator.modify_xrp_account(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/xrp/account/settings", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))