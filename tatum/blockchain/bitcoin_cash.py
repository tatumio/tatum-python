import http.client
import json
import validator.blockchain as blockchain_validator
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

def generate_bitcoin_cash_wallet(query_params={}):
    if blockchain_validator.generate_wallet(query_params):
        if query_params != {}:
            conn.request("GET", "/v3/bcash/wallet?mnemonic={}".format(query_params['mnemonic']), headers=headers())
        else:
            conn.request("GET", "/v3/bcash/wallet", headers=headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def generate_bitcoin_cash_deposit_address_from_extended_public_key(path_params):
    if blockchain_validator.generate_deposit_address_from_extended_public_key(path_params):
        conn.request("GET", "/v3/bcash/address/{}/{}".format(path_params['xpub'], path_params['index']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def generate_bitcoin_cash_private_key(body_params):
    if blockchain_validator.generate_private_key(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/bcash/wallet/priv", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def get_bitcoin_cash_blockchain_information():
    conn.request("GET", "/v3/bcash/info", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_bitcoin_cash_block_hash(path_params):
    if blockchain_validator.get_block_hash(path_params):
        conn.request("GET", "/v3/bcash/block/{}".format(path_params['i']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_bitcoin_cash_block_by_hash(path_params):
    if blockchain_validator.bitcoin_cash_get_block_hash(path_params):
        conn.request("GET", "/v3/bcash/block/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_bitcoin_cash_transaction_by_hash(path_params):
    if blockchain_validator.get_block_by_hash_or_height(path_params):
        conn.request("GET", "/v3/bcash/transaction/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_bitcoin_cash_transaction_by_address(path_params, query_params = {}):
    if blockchain_validator.get_bitcoin_cash_transaction_by_address(path_params, query_params):
        skip = ''
        if 'skip' in query_params.keys():
            skip = '?skip={}'.format(query_params['skip'])
        conn.request("GET", "/v3/bcash/transaction/address/{}{}".format(path_params['address'], skip), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


def send_bitcoin_cash_to_blockchain_addresses(body_params):
    if blockchain_validator.send_bitcoin_cash_to_blockchain_addresses(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/bcash/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def broadcast_signed_bitcoin_cash_transaction(body_params):
    if blockchain_validator.broadcast_signed_transaction(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/bcash/broadcast", body_params, headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")