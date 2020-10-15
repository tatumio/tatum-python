import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']

def create_new_deposit_address(path_params, query_params = {}):
    validator.create_new_deposit_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    index = ''
    if query_params != {}:
        index = 'index={}'.format(query_params['index'])
    conn.request("POST", "/v3/offchain/account/{}/address?{}".format(path_params['id'], index), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_all_deposit_addresses_for_account(path_params):
    validator.id_path_param(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("GET", "/v3/offchain/account/{}/address".format(path_params['id']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def check_if_deposit_address_is_asigned(path_params, query_params = {}):
    validator.check_if_deposit_address_is_asigned(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    index = ''
    if query_params != {}:
        index = 'index={}'.format(query_params['index'])

    conn.request("GET", "/v3/offchain/account/address/{}/{}?{}".format(path_params['address'], path_params['currency'], index), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
    
def remove_address_for_account(path_params):
    validator.remove_address_for_account(path_params)
    headers = { 'x-api-key': API_KEY }
    
    conn.request("DELETE", "/v3/offchain/account/{}/address/{}".format(path_params['id'], path_params['address']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

    
def assign_address_for_account(path_params):
    validator.remove_address_for_account(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("POST", "/v3/offchain/account/{}/address/{}".format(path_params['id'], path_params['address']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))