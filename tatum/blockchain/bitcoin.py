import http.client
import json
import validator.blockchain as blockchain_validator
import requests
import os
from dotenv import load_dotenv
from bip_utils import Bip32, Bip39EntropyGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip39MnemonicValidator, Bip39SeedGenerator
from pywallet import wallet
import pprint
import binascii
import mnemonic
import bip32utils
from bip32 import BIP32, HARDENED_INDEX




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

def generate_bitcoin_wallet(query_params={}):
    if blockchain_validator.generate_litecoin_wallet(query_params):
        if query_params != {}:
            mnemonic = query_params['mnemonic']
        else:
            mnemonic = wallet.generate_mnemonic(strength=256)

        if Bip39MnemonicValidator(mnemonic).Validate():
            seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
            bip32_ctx = Bip32.FromSeedAndPath(seed_bytes, "m/44'/0'/0'/0")
            return {"xpub": bip32_ctx.PublicKey().ToExtended() , "mnemonic": mnemonic}
        else:
            return 'Mnemonic is not valid!'

def generate_bitcoin_deposit_address_from_extended_public_key(path_params):
    if blockchain_validator.generate_deposit_address_from_extended_public_key(path_params):
        w = wallet.create_address(network="BTC", xpub=path_params['xpub'], child=path_params['index'])
        return {"address": w['address']}

def generate_bitcoin_private_key(body_params):
    if blockchain_validator.generate_private_key(body_params):
        if Bip39MnemonicValidator(body_params['mnemonic']).Validate():
            mobj = mnemonic.Mnemonic("english")
            seed = mobj.to_seed(body_params['mnemonic'])           
            bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
            bip32_child_key_obj = bip32_root_key_obj.ChildKey(
                44 + bip32utils.BIP32_HARDEN
            ).ChildKey(
                0 + bip32utils.BIP32_HARDEN
            ).ChildKey(
                0 + bip32utils.BIP32_HARDEN
            ).ChildKey(0).ChildKey(body_params['index'])
 
            return {
                'key': bip32_child_key_obj.WalletImportFormat(),
            }
        else:
            return 'Mnemonic is not valid!'


def get_blockchain_information():
    conn.request("GET", "/v3/bitcoin/info", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_block_hash(path_params):
    if blockchain_validator.get_block_hash(path_params):
        conn.request("GET", "/v3/bitcoin/block/hash/{}".format(path_params['i']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_block_by_hash_or_height(path_params):
    if blockchain_validator.get_block_by_hash_or_height(path_params):
        conn.request("GET", "/v3/bitcoin/block/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_transaction_by_hash(path_params):
    if blockchain_validator.get_block_by_hash_or_height(path_params):
        conn.request("GET", "/v3/bitcoin/transaction/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_transaction_by_address(path_params, query_params):
    if blockchain_validator.get_transaction_by_address(path_params, query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/bitcoin/transaction/address/{}?pageSize={}&offset={}".format(path_params['address'], query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/bitcoin/transaction/address/{}?pageSize={}".format(path_params['address'], query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_utxo_of_transaction(path_params):
    if blockchain_validator.get_utxo_of_transaction(path_params):
        conn.request("GET", "/v3/bitcoin/utxo/{}/{}".format(path_params['hash'], path_params['index']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def send_bitcoin_to_blockchain_addresses(body_params):
    if blockchain_validator.send_bitcoin_to_blockchain_addresses(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/bitcoin/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def broadcast_signed_bitcoin_transaction(body_params):
    if blockchain_validator.broadcast_signed_transaction(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/bitcoin/broadcast", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")