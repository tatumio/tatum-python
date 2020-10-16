import http.client
import json
import validator
import requests
import os
from dotenv import load_dotenv

load_dotenv()

conn = http.client.HTTPSConnection(os.environ['API_URL'])
API_KEY = os.environ['API_KEY']


def generate_bitcoin_cash_wallet(query_params={}):
    validator.generate_wallet(query_params)
    headers = { 'x-api-key': API_KEY }
    if query_params != {}:
        conn.request("GET", "/v3/bcash/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers)
    else:
        conn.request("GET", "/v3/bcash/wallet", headers=headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_bitcoin_cash_deposit_address_from_extended_public_key(path_params):
    validator.generate_deposit_address_from_extended_public_key(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bcash/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def generate_bitcoin_cash_private_key(body_params):
    validator.generate_private_key(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bcash/wallet/priv", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_bitcoin_cash_blockchain_information():
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bcash/info", headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_bitcoin_cash_block_hash(path_params):
    validator.get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bcash/block/{}".format(path_params['i']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_bitcoin_cash_block_by_hash(path_params):
    validator.bitcoin_cash_get_block_hash(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bcash/block/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def get_bitcoin_cash_transaction_by_hash(path_params):
    validator.get_block_by_hash_or_height(path_params)
    headers = { 'x-api-key': API_KEY }
    conn.request("GET", "/v3/bcash/transaction/{}".format(path_params['hash']), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def get_bitcoin_cash_transaction_by_address(path_params, query_params = {}):
    validator.get_bitcoin_cash_transaction_by_address(path_params, query_params)
    headers = { 'x-api-key': API_KEY }
    skip = ''
    if 'skip' in query_params.keys():
        skip = '?skip={}'.format(query_params['skip'])
    conn.request("GET", "/v3/bcash/transaction/address/{}{}".format(path_params['address'], skip), headers=headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def send_bitcoin_cash_to_blockchain_addresses(body_params):
    validator.send_bitcoin_cash_to_blockchain_addresses(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bcash/transaction", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def broadcast_signed_bitcoin_cash_transaction(body_params):
    validator.broadcast_signed_transaction(body_params)
    body_params = json.dumps(body_params)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }
    conn.request("POST", "/v3/bcash/broadcast", body_params, headers)
#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))