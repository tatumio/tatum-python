import http.client
import json
import validator
import requests

conn = http.client.HTTPSConnection("api.tatum.io")


def create_new_account(API_KEY, body_params):
    validator.create_new_account(body_params)

    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/ledger/account", body_params, headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def list_all_accounts(API_KEY, query_params):
    validator.list_all_accounts(query_params)

    headers = { 'x-api-key': API_KEY }
    if len(query_params) != 1:
        conn.request("GET", "/v3/ledger/account?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ledger/account?pageSize={}".format(query_params['pageSize']), headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def list_all_customer_accounts(API_KEY, path_params, query_params):
    validator.list_all_customer_accounts(path_params, query_params)
    headers = { 'x-api-key': API_KEY }

    if len(query_params) != 1:
         conn.request("GET", "/v3/ledger/account/customer/{}?pageSize={}&offset={}".format(path_params['id'], query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ledger/account/customer/{}?pageSize={}".format(path_params['id'], query_params['pageSize']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_by_ID(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/ledger/account/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_account_balance(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/ledger/account/{}/balance".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    
def block_amount_on_account(API_KEY, path_params, body_params):
    validator.block_amount_on_account(path_params, body_params)
    body_params = json.dumps(body_params)
    headers = { 
        'content-type': "application/json",
        'x-api-key': API_KEY }

    conn.request("POST", "/v3/ledger/account/block/{}".format(path_params['id']), body_params, headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def unlock_amount_on_account_and_perform_transaction(API_KEY, path_params, body_params):
    validator.unlock_amount_on_account_and_perform_transaction(path_params, body_params)
    body_params = json.dumps(body_params)
    headers = { 
        'content-type': "application/json",
        'x-api-key': API_KEY }

    conn.request("PUT", "/v3/ledger/account/block/{}".format(path_params['id']), body_params, headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    
def unblock_blocked_amount_on_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("DELETE", "/v3/ledger/account/block/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_blocked_amounts_on_account(API_KEY, path_params, query_params):
    validator.get_blocked_amounts_on_account(path_params, query_params)
    headers = { 
        'x-api-key': API_KEY }
    if len(query_params) != 1:
        conn.request("GET", "/v3/ledger/account/block/{}?pageSize={}&offset={}".format(path_params['id'], query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ledger/account/block/{}?pageSize={}".format(path_params['id'], query_params['pageSize']), headers=headers)
#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def unblock_all_blocked_amounts_on_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("DELETE", "/v3/ledger/account/block/{}".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def activate_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("PUT", "/v3/ledger/account/{}/activate".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def deactivate_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("PUT", "/v3/ledger/account/{}/deactivate".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def freeze_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("PUT", "/v3/ledger/account/{}/freeze".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def unfreeze_account(API_KEY, path_params):
    validator.id_path_param(path_params)
    headers = { 
        'x-api-key': API_KEY }

    conn.request("PUT", "/v3/ledger/account/{}/unfreeze".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))