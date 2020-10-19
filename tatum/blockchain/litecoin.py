import http.client
import json
import validator.blockchain as blockchain_validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_litecoin_wallet(query_params={}):
    blockchain_validator.generate_wallet(query_params)
    headers = { 'x-api-key': API_KEY }
    if query_params != {}:
        conn.request("GET", "/v3/litecoin/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers)
    else:
        conn.request("GET", "/v3/litecoin/wallet", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_litecoin_deposit_address_from_extended_public_key(path_params):
    blockchain_validator.generate_deposit_address_from_extended_public_key(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_litecoin_private_key(body_params):
    blockchain_validator.generate_private_key(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/litecoin/wallet/priv", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")


def get_litecoin_blockchain_information():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/info", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_litecoin_block_hash(path_params):
    blockchain_validator.get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/block/{}".format(path_params['i']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_litecoin_block_by_hash_or_height(path_params):
    blockchain_validator.ethereum_get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/block/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def get_litecoin_transaction_by_hash(path_params):
    blockchain_validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_litecoin_transaction_by_address(path_params, query_params):
    blockchain_validator.get_transaction_by_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    offset = ''
    if 'offset' in query_params.keys():
        offset = 'offset={}'.format(query_params['offset'])

    conn.request("GET", "/v3/litecoin/transaction/address/{}?pageSize={}&{}".format(path_params['address'], query_params['pageSize'], offset), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_utxo_of_transaction(path_params):
    blockchain_validator.get_utxo_of_transaction(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/litecoin/utxo/{}/{}".format(path_params['hash'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def send_litecoin_to_blockchain_addresses(body_params):
    blockchain_validator.send_to_blockchain_addresses(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/litecoin/transaction", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")

def broadcast_signed_litecoin_transaction(body_params):
    blockchain_validator.broadcast_signed_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/litecoin/broadcast", body_params, headers)

    res = conn.getresponse()
    data = res.read()
#   _______________________________________________________________
    print(data.decode("utf-8"))
#   _______________________________________________________________
    return data.decode("utf-8")