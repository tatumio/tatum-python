import http.client
import json
import validator.ledger as ledger_validator
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

def create_new_account(body_params):
    if ledger_validator.create_new_account(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ledger/account", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def list_all_accounts(query_params):
    if ledger_validator.page_size_query_params(query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/ledger/account?pageSize={}&offset={}".format(query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/ledger/account?pageSize={}".format(query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def list_all_customer_accounts(path_params, query_params):
    if ledger_validator.list_all_customer_accounts(path_params, query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/ledger/account/customer/{}?pageSize={}&offset={}".format(path_params['id'], query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/ledger/account/customer/{}?pageSize={}".format(path_params['id'], query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_account_by_ID(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("GET", "/v3/ledger/account/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_account_balance(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("GET", "/v3/ledger/account/{}/balance".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    
def block_amount_on_account(path_params, body_params):
    if ledger_validator.block_amount_on_account(path_params, body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ledger/account/block/{}".format(path_params['id']), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def unlock_amount_on_account_and_perform_transaction(path_params, body_params):
    if ledger_validator.unlock_amount_on_account_and_perform_transaction(path_params, body_params):
        body_params = json.dumps(body_params)
        conn.request("PUT", "/v3/ledger/account/block/{}".format(path_params['id']), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    
def unblock_blocked_amount_on_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("DELETE", "/v3/ledger/account/block/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_blocked_amounts_on_account(path_params, query_params):
    if ledger_validator.get_blocked_amounts_on_account(path_params, query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/ledger/account/block/{}?pageSize={}&offset={}".format(path_params['id'], query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/ledger/account/block/{}?pageSize={}".format(path_params['id'], query_params['pageSize']), headers=headers())

        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def unblock_all_blocked_amounts_on_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("DELETE", "/v3/ledger/account/block/{}".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def activate_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/account/{}/activate".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def deactivate_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/account/{}/deactivate".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def freeze_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/account/{}/freeze".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def unfreeze_account(path_params):
    if ledger_validator.id_path_param(path_params):
        conn.request("PUT", "/v3/ledger/account/{}/unfreeze".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")