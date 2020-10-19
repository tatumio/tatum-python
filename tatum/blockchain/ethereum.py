import http.client
import json
import validator.blockchain as blockchain_validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_ethereum_wallet(query_params={}):
    blockchain_validator.generate_wallet(query_params)
    headers = { 'x-api-key': API_KEY }
    if query_params != {}:
        conn.request("GET", "/v3/ethereum/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers)
    else:
        conn.request("GET", "/v3/ethereum/wallet", headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def generate_ethereum_account_address_from_extended_public_key(path_params):
    blockchain_validator.generate_deposit_address_from_extended_public_key(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def generate_ethereum_private_key(body_params):
    blockchain_validator.generate_private_key(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/wallet/priv", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def web3_http_driver(body_params):
    headers = { 'content-type': "application/json" }

    conn.request("POST", "/v3/ethereum/web3/{}".format(API_KEY), body_params, headers)



    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_current_block():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/block/current", headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_block_by_hash(path_params):
    blockchain_validator.ethereum_get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/block/{}".format(path_params['hash']), headers=headers)



    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_account_balance(path_params):
    blockchain_validator.get_ethereum_account_balance(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/account/balance/{}".format(path_params['address']), headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_erc20_account_balance(path_params, query_params = {}):
    blockchain_validator.get_ethereum_erc20_account_balance(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    currency = ''
    contractAddress = ''
    if 'currency' in query_params.keys():
        currency = "currency={}".format(query_params['currency'])
    if 'contractAddress' in query_params.keys():
        currency = "contractAddress={}".format(query_params['contractAddress'])
    conn.request("GET", "/v3/ethereum/account/balance/erc20/{}?{}&{}".format(path_params['address'], contractAddress, currency), headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_transaction(path_params):
    blockchain_validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/transaction/{}".format(path_params['hash']), headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_count_of_outgoing_ethereum_transactions(path_params):
    blockchain_validator.get_count_of_outgoing_ethereum_transactions(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/transaction/count/{}".format(path_params['address']), headers=headers)



    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_transactions_by_address(path_params, query_params):
    blockchain_validator.get_transaction_by_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    if len(query_params) != 1:
        conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}&offset={}".format(path_params['address'], query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}".format(path_params['address'], query_params['pageSize']), headers=headers)


    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def send_ethereum_erc20_from_account_to_account(body_params):
    blockchain_validator.send_ethereum_erc20_from_account_to_account(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/transaction", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def invoke_smart_contract_method(body_params):
    blockchain_validator.invoke_smart_contract_method(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/smartcontract", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")
    
def deploy_ethereum_erc20_smart_contract(body_params):
    blockchain_validator.deploy_ethereum_erc20_smart_contract(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc20/deploy", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def deploy_ethereum_erc721_smart_contract(body_params):
    blockchain_validator.deploy_ethereum_erc721_smart_contract(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc721/deploy", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def mint_ethereum_erc721(body_params):
    blockchain_validator.mint_ethereum_erc721(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc721/mint", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def transfer_ethereum_erc721_token(body_params):
    blockchain_validator.transfer_ethereum_erc721_token(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc721/transaction", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def mint_ethereum_erc721_multiple_tokens(body_params):
    blockchain_validator.mint_ethereum_erc721_multiple_tokens(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc721/mint", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def burn_ethereum_erc721(body_params):
    blockchain_validator.burn_ethereum_erc721(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/erc721/burn", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_erc721_account_balance(path_params):
    blockchain_validator.get_ethereum_erc721_account_balance(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/erc721/balance/{}/{}".format(path_params['address'], path_params['contractAddress']), headers=headers)
    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_erc721_token(path_params):
    blockchain_validator.get_ethereum_erc721_token(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/erc721/token/{}/{}/{}".format(path_params['address'],path_params['index'], path_params['contractAddress']), headers=headers)
    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_erc721_token_metadata(path_params):
    blockchain_validator.get_ethereum_erc721_token_metadata(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/erc721/metadata/{}/{}".format(path_params['token'], path_params['contractAddress']), headers=headers)
    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def get_ethereum_erc721_token_owner(path_params):
    blockchain_validator.get_ethereum_erc721_token_metadata(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/erc721/owner/{}/{}".format(path_params['token'], path_params['contractAddress']), headers=headers)
    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def broadcast_signed_ethereum_transaction(body_params):
    blockchain_validator.broadcast_signed_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/ethereum/broadcast", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))