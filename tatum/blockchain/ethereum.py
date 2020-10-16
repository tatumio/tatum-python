import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_ethereum_wallet(query_params={}):
    validator.generate_wallet(query_params)
    headers = { 'x-api-key': API_KEY }
    if query_params != {}:
        conn.request("GET", "/v3/ethereum/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers)
    else:
        conn.request("GET", "/v3/ethereum/wallet", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_ethereum_account_address_from_extended_public_key(path_params):
    validator.generate_deposit_address_from_extended_public_key(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_ethereum_private_key(body_params):
    validator.generate_private_key(body_params)
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

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_current_block():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/block/current", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_block_by_hash(path_params):
    validator.ethereum_get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/block/{}".format(path_params['hash']), headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_ethereum_account_balance(path_params):
    validator.get_ethereum_account_balance(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/account/balance/{}".format(path_params['address']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_ethereum_erc20_account_balance(path_params, query_params = {}):
    validator.get_ethereum_erc20_account_balance(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    currency = ''
    contractAddress = ''
    if 'currency' in query_params.keys():
        currency = "currency={}".format(query_params['currency'])
    if 'contractAddress' in query_params.keys():
        currency = "contractAddress={}".format(query_params['contractAddress'])
    conn.request("GET", "/v3/ethereum/account/balance/erc20/{}?{}&{}".format(path_params['address'], contractAddress, currency), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_ethereum_transaction(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_count_of_outgoing_ethereum_transactions(path_params):
    validator.get_count_of_outgoing_ethereum_transactions(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/ethereum/transaction/count/{}".format(path_params['address']), headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_ethereum_transactions_by_address(path_params, query_params):
    validator.get_transaction_by_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    if len(query_params) != 1:
        conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}&offset={}".format(path_params['address'], query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}".format(path_params['address'], query_params['pageSize']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))










# def get_utxo_of_transaction(path_params):
#     validator.get_utxo_of_transaction(path_params)
#     headers = { 'x-api-key': API_KEY }
#     conn.request("GET", "/v3/ethereum/utxo/{}/{}".format(path_params['hash'], path_params['index']), headers=headers)
# #   _______________________________________________________________

#     res = conn.getresponse()
#     data = res.read()

#     print(data.decode("utf-8"))

# def send_ethereum_to_blockchain_addresses(body_params):
#     validator.send_ethereum_to_blockchain_addresses(body_params)
#     body_params = json.dumps(body_params)
#     headers = {
#         'content-type': "application/json",
#         'x-api-key': API_KEY
#         }
#     conn.request("POST", "/v3/ethereum/transaction", body_params, headers)
# #   _______________________________________________________________

#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))

# def broadcast_signed_ethereum_transaction(body_params):
#     validator.broadcast_signed_ethereum_transaction(body_params)
#     body_params = json.dumps(body_params)
#     headers = {
#         'content-type': "application/json",
#         'x-api-key': API_KEY
#         }
#     conn.request("POST", "/v3/ethereum/broadcast", body_params, headers)
# #   _______________________________________________________________

#     res = conn.getresponse()
#     data = res.read()
#     print(data.decode("utf-8"))