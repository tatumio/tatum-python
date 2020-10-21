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

def send_payment(body_params):
    if ledger_validator.send_payment(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ledger/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def find_transactions_for_account(query_params, body_params):
    if ledger_validator.find_transactions_for_account(query_params, body_params):
        body_params = json.dumps(body_params)
        offset = ''
        count = ''
        for key in query_params.keys():
            if key == 'offset':
                offset = 'offset={}'.format(query_params['offset'])
            
            if key == 'count':
                count = 'count={}'.format(query_params['count'])

        conn.request("POST", "/v3/ledger/transaction/account?pageSize={}&{}&{}".format(query_params['pageSize'], offset, count), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params):
    if ledger_validator.find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params):
        body_params = json.dumps(body_params)
        offset = ''
        count = ''
        for key in query_params.keys():
            if key == 'offset':
                offset = 'offset={}'.format(query_params['offset'])
            
            if key == 'count':
                count = 'count={}'.format(query_params['count'])
        conn.request("POST", "/v3/ledger/transaction/customer?pageSize={}&{}&{}".format(query_params['pageSize'], offset, count), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def find_transactions_for_ledger(query_params, body_params):
    if ledger_validator.find_transactions_for_ledger(query_params, body_params):
        body_params = json.dumps(body_params)
        offset = ''
        count = ''
        for key in query_params.keys():
            if key == 'offset':
                offset = 'offset={}'.format(query_params['offset'])
            
            if key == 'count':
                count = 'count={}'.format(query_params['count'])

        conn.request("POST", "/v3/ledger/transaction/ledger?pageSize={}&{}&{}".format(query_params['pageSize'], offset, count), body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def find_transactions_with_given_reference_across_all_accounts(path_params):
    if ledger_validator.find_transactions_with_given_reference_across_all_accounts(path_params):
        conn.request("GET", "/v3/ledger/transaction/reference/{}".format(path_params['reference']), headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")