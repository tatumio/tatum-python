import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def send_bitcoin_from_tatum_account_to_address(body_params):
    validator.send_from_tatum_account_to_address(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/bitcoin/transfer", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    
def send_bitcoin_cash_from_tatum_account_to_address(body_params):
    validator.send_from_tatum_account_to_address(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/bcash/transfer", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
     
def send_litecoin_from_tatum_account_to_address(body_params):
    validator.send_from_tatum_account_to_address(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/litecoin/transfer", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def send_ethereum_from_tatum_ledger_to_blockchain(body_params):
    validator.send_ethereum_from_tatum_ledger_to_blockchain(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/ethereum/transfer", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))    

def create_new_ERC20_token(body_params):
    validator.create_new_ERC20_token(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/ethereum/erc20", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))    

def deploy_ethereum_erc20_smart_contract_offchain(body_params):
    validator.deploy_ethereum_erc20_smart_contract_offchain(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/ethereum/erc20/deploy", body_params, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))   

def set_erc20_token_contract_address(path_params):
    validator.set_erc20_token_contract_address(path_params)
    headers = { 'x-api-key': API_KEY }

    conn.request("POST", "/v3/offchain/ethereum/erc20/{}/{}".format(path_params['name'], path_params['address']), headers=headers)

#   _______________________________________________________________
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def transfer_ethereum_erc20_from_tatum_ledger_to_blockchain(body_params):
    validator.transfer_ethereum_erc20_from_tatum_ledger_to_blockchain(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/offchain/ethereum/erc20/transfer", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))  

def send_xlm_asset_from_tatum_ledger_to_blockchain(body_params):
    validator.send_xlm_asset_from_tatum_ledger_to_blockchain(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/offchain/xlm/transfer", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_xlm_based_asset(body_params):
    validator.create_xlm_based_asset(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/offchain/xlm/asset", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def send_xrp_from_tatum_ledger_to_blockchain(body_params):
    validator.send_xrp_from_tatum_ledger_to_blockchain(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/offchain/xrp/transfer", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def create_xrp_based_asset(body_params):
    validator.create_xrp_based_asset(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/offchain/xrp/asset", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))