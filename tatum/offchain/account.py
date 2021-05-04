import http.client
import json
import validator.offchain as offchain_validator
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
            
def create_new_deposit_address(path_params, query_params = {}):
    if offchain_validator.create_new_deposit_address(path_params, query_params):
        index = ''
        if query_params != {}:
            index = 'index={}'.format(query_params['index'])
        conn.request("POST", "/v3/offchain/account/{}/address?{}".format(path_params['id'], index), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_all_deposit_addresses_for_account(path_params):
    if offchain_validator.id_path_param(path_params):
        conn.request("GET", "/v3/offchain/account/{}/address".format(path_params['id']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def create_new_deposit_address_in_a_batch_call(body_params):
    if offchain_validator.create_new_deposit_address_in_a_batch_call(body_params):
        body_params=json.dumps(body_params)
        conn.request("POST", "/v3/offchain/account/address/batch", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
        
def check_if_deposit_address_is_asigned(path_params, query_params = {}):
    if offchain_validator.check_if_deposit_address_is_asigned(path_params, query_params):
        index = ''
        if query_params != {}:
            index = 'index={}'.format(query_params['index'])
        conn.request("GET", "/v3/offchain/account/address/{}/{}?{}".format(path_params['address'], path_params['currency'], index), headers=headers())


        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    
def remove_address_for_account(path_params):
    if offchain_validator.remove_address_for_account(path_params):    
        conn.request("DELETE", "/v3/offchain/account/{}/address/{}".format(path_params['id'], path_params['address']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

    
def assign_address_for_account(path_params):
    if offchain_validator.remove_address_for_account(path_params):
        conn.request("POST", "/v3/offchain/account/{}/address/{}".format(path_params['id'], path_params['address']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")