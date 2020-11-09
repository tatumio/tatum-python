import http.client
import json
import validator.blockchain as blockchain_validator
import requests
import os
from dotenv import load_dotenv
from bip_utils import Bip39EntropyGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip39MnemonicValidator, Bip39SeedGenerator
from pywallet import wallet
import mnemonic as eth_mnemonic
import pprint
import binascii
import mnemonic
import bip32utils
import hashlib
import base58

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

def generate_ethereum_wallet(query_params={}):
    if blockchain_validator.generate_litecoin_wallet(query_params):
        if query_params != {}:
            mnemonic = query_params['mnemonic']
        else:
            mnemonic = wallet.generate_mnemonic(strength=256)

        if Bip39MnemonicValidator(mnemonic).Validate():
            w = wallet.create_wallet(network="ETH", seed=mnemonic, children=1)
            return {"xpub": w['xpublic_key'].decode("utf-8") , "mnemonic": mnemonic}
        else:
            return 'Mnemonic is not valid!'

def generate_ethereum_account_address_from_extended_public_key(path_params):
    if blockchain_validator.generate_deposit_address_from_extended_public_key(path_params):
        w = wallet.create_address(network="ETH", xpub=path_params['xpub'], child=path_params['index'])
        return {"address": w['address']}

def generate_ethereum_private_key(body_params):
    if blockchain_validator.generate_private_key(body_params):
        if Bip39MnemonicValidator(body_params['mnemonic']).Validate():
            mobj = mnemonic.Mnemonic("english")
            seed = mobj.to_seed(body_params['mnemonic'])

            bip32_root_key_obj = bip32utils.BIP32Key.fromEntropy(seed)
            bip32_child_key_obj = bip32_root_key_obj.ChildKey(
                44 + bip32utils.BIP32_HARDEN
            ).ChildKey(
                60 + bip32utils.BIP32_HARDEN
            ).ChildKey(
                0 + bip32utils.BIP32_HARDEN
            ).ChildKey(0).ChildKey(body_params['index'])

            wif = bip32_child_key_obj.WalletImportFormat()

            first_encode = base58.b58decode(wif)
            private_key_full = binascii.hexlify(first_encode)
            private_key = '0x' + private_key_full[2:-10].decode("utf-8")
            return {
                'key': private_key,
            }
        else:
            return 'Mnemonic is not valid!'

def web3_http_driver(body_params):
    headers = { 'content-type': "application/json" }
    conn.request("POST", "/v3/ethereum/web3/{}".format(API_KEY), body_params, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_current_block():
    conn.request("GET", "/v3/ethereum/block/current", headers=headers())
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_block_by_hash(path_params):
    if blockchain_validator.ethereum_get_block_hash(path_params):
        conn.request("GET", "/v3/ethereum/block/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_account_balance(path_params):
    if blockchain_validator.get_ethereum_account_balance(path_params):
        conn.request("GET", "/v3/ethereum/account/balance/{}".format(path_params['address']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_erc20_account_balance(path_params, query_params = {}):
    if blockchain_validator.get_ethereum_erc20_account_balance(path_params, query_params):
        currency = ''
        contractAddress = ''
        if 'currency' in query_params.keys():
            currency = "currency={}".format(query_params['currency'])
        if 'contractAddress' in query_params.keys():
            currency = "contractAddress={}".format(query_params['contractAddress'])
        conn.request("GET", "/v3/ethereum/account/balance/erc20/{}?{}&{}".format(path_params['address'], contractAddress, currency), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_transaction(path_params):
    if blockchain_validator.get_block_by_hash_or_height(path_params):
        conn.request("GET", "/v3/ethereum/transaction/{}".format(path_params['hash']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_count_of_outgoing_ethereum_transactions(path_params):
    if blockchain_validator.get_count_of_outgoing_ethereum_transactions(path_params):
        conn.request("GET", "/v3/ethereum/transaction/count/{}".format(path_params['address']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_transactions_by_address(path_params, query_params):
    if blockchain_validator.get_transaction_by_address(path_params, query_params):
        if len(query_params) != 1:
            conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}&offset={}".format(path_params['address'], query_params['pageSize'], query_params['offset']), headers=headers())
        else:
            conn.request("GET", "/v3/ethereum/transaction/address/{}?pageSize={}".format(path_params['address'], query_params['pageSize']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def send_ethereum_erc20_from_account_to_account(body_params):
    if blockchain_validator.send_ethereum_erc20_from_account_to_account(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def invoke_smart_contract_method(body_params):
    if blockchain_validator.invoke_smart_contract_method(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/smartcontract", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    
def deploy_ethereum_erc20_smart_contract(body_params):
    if blockchain_validator.deploy_ethereum_erc20_smart_contract(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc20/deploy", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def deploy_ethereum_erc721_smart_contract(body_params):
    if blockchain_validator.deploy_ethereum_erc721_smart_contract(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc721/deploy", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def mint_ethereum_erc721(body_params):
    if blockchain_validator.mint_ethereum_erc721(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc721/mint", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def transfer_ethereum_erc721_token(body_params):
    if blockchain_validator.transfer_ethereum_erc721_token(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc721/transaction", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def mint_ethereum_erc721_multiple_tokens(body_params):
    if blockchain_validator.mint_ethereum_erc721_multiple_tokens(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc721/mint", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def burn_ethereum_erc721(body_params):
    if blockchain_validator.burn_ethereum_erc721(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/erc721/burn", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_erc721_account_balance(path_params):
    if blockchain_validator.get_ethereum_erc721_account_balance(path_params):
        conn.request("GET", "/v3/ethereum/erc721/balance/{}/{}".format(path_params['address'], path_params['contractAddress']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_erc721_token(path_params):
    if blockchain_validator.get_ethereum_erc721_token(path_params):
        conn.request("GET", "/v3/ethereum/erc721/token/{}/{}/{}".format(path_params['address'],path_params['index'], path_params['contractAddress']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_erc721_token_metadata(path_params):
    if blockchain_validator.get_ethereum_erc721_token_metadata(path_params):
        conn.request("GET", "/v3/ethereum/erc721/metadata/{}/{}".format(path_params['token'], path_params['contractAddress']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def get_ethereum_erc721_token_owner(path_params):
    if blockchain_validator.get_ethereum_erc721_token_metadata(path_params):
        conn.request("GET", "/v3/ethereum/erc721/owner/{}/{}".format(path_params['token'], path_params['contractAddress']), headers=headers())
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")

def broadcast_signed_ethereum_transaction(body_params):
    if blockchain_validator.broadcast_signed_transaction(body_params):
        body_params = json.dumps(body_params)
        conn.request("POST", "/v3/ethereum/broadcast", body_params, headers=headers(for_post=True))
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")