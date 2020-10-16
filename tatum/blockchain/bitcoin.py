import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_bitcoin_wallet(query_params={}):
    validator.generate_wallet(query_params)
    headers = { 'x-api-key': API_KEY }
    if query_params != {}:
        conn.request("GET", "/v3/bitcoin/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers)
    else:
        conn.request("GET", "/v3/bitcoin/wallet", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_bitcoin_deposit_address_from_extended_public_key(path_params):
    validator.generate_deposit_address_from_extended_public_key(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_bitcoin_private_key(body_params):
    validator.generate_private_key(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bitcoin/wallet/priv", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_blockchain_information():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/info", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_block_hash(path_params):
    validator.bitcoin_get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/block/hash/{}".format(path_params['i']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_block_by_hash_or_height(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/block/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_transaction_by_hash(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_transaction_by_address(path_params, query_params):
    validator.get_transaction_by_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    if len(query_params) != 1:
        conn.request("GET", "/v3/bitcoin/transaction/address/{}?pageSize={}&offset={}".format(path_params['address'], query_params['pageSize'], query_params['offset']), headers=headers)
    else:
        conn.request("GET", "/v3/bitcoin/transaction/address/{}?pageSize={}".format(path_params['address'], query_params['pageSize']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_utxo_of_transaction(path_params):
    validator.get_utxo_of_transaction(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bitcoin/utxo/{}/{}".format(path_params['hash'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def send_bitcoin_to_blockchain_addresses(body_params):
    validator.send_bitcoin_to_blockchain_addresses(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bitcoin/transaction", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def broadcast_signed_bitcoin_transaction(body_params):
    validator.broadcast_signed_bitcoin_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bitcoin/broadcast", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))