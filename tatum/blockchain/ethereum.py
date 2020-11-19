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
import time
# from brownie import Token, accounts

from web3 import Web3, IPCProvider
web3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/0fb2f5e906884367b08fdec2e556b4c1'))
# print(web3.isConnected())

contract_address = '0x0C0db1Eeb7c420eBebf34C50c80da0C6361688d7'
wallet_private_key = '0xc2b15388fcc36ce104842dcf9c18dcd5dd87f765f511e569a4037965afd92845'
wallet_address = '0x5911774BC465d36135516D60bDAA361bb8587aF1'
# Because we’re using some features of Web3.py that haven’t been fully audited for security, we need to call w3.eth.enable_unaudited_features() to acknowledge that we’re aware that bad things might happen
# web3.eth.enable_unaudited_features()

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
            return {"xpriv": w['xprivate_key'].decode("utf-8"), 
                    "xpub": w['xpublic_key'].decode("utf-8") , 
                    "mnemonic": mnemonic}
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
    # https://hackernoon.com/ethereum-smart-contracts-in-python-a-comprehensive-ish-guide-771b03990988
    # http://remix.ethereum.org/#optimize=false&evmVersion=null&version=soljson-v0.6.6+commit.6c089d02.js
    # if blockchain_validator.send_ethereum_erc20_from_account_to_account(body_params):  
    
    amount_in_wei = web3.toWei(body_params['amount'],'ether')
    nonce = web3.eth.getTransactionCount('0x0C0db1Eeb7c420eBebf34C50c80da0C6361688d7')
    # kde získám nonce nebo adresu smlouvy?
    txn_dict = {
            'to': body_params['to'],
            'value': amount_in_wei,
            'gas': int(body_params['fee']['gasLimit']),
            'gasPrice': web3.toWei(body_params['fee']['gasPrice'], 'gwei'),
            'nonce': nonce,
            'chainId': 3, #https://ethereum.stackexchange.com/questions/17051/how-to-select-a-network-id-or-is-there-a-list-of-network-ids
            # nastavit pro testnet a mainnet
    }

    signed_txn = web3.eth.account.signTransaction(txn_dict, body_params['fromPrivateKey'])

    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_hash = '0x{}'.format(binascii.hexlify(txn_hash).decode("utf-8"))
    count = 0
    while (count < 30):
        count=+1
        conn.request("GET", "/v3/ethereum/transaction/{}".format(txn_hash), headers=headers())
        res = conn.getresponse()
        transaction = res.read().decode("utf-8")
        if json.loads(transaction)['hash'] == txn_hash:
            return({'txId': txn_hash,"failed": 'false'})
        time.sleep(5)
    if json.loads(transaction)['hash'] != txn_hash:
            return({'txId': txn_hash,"failed": 'true'})
    # txId je txhash?



def invoke_smart_contract_method(body_params):
    # if blockchain_validator.invoke_smart_contract_method(body_params):
    web3.eth.defaultAccount = web3.eth.accounts[0]
    print(web3.eth.defaultAccount)
    abi = json.loads('[{"constant":true,"inputs":[],"name":"getCurrentOpinion","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_soapboxer","type":"address"}],"name":"isApproved","outputs":[{"name":"approved","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_opinion","type":"string"}],"name":"broadcastOpinion","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"_soapboxer","type":"address"},{"indexed":false,"name":"_opinion","type":"string"}],"name":"OpinionBroadcast","type":"event"}]')
    bytecode = '608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680635f1d90ae146100c0578063673448dd14610150578063805c2b6c146101ab575b66470de4df8200003411156100be5760016000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548160ff0219169083151502179055505b005b3480156100cc57600080fd5b506100d561022c565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101155780820151818401526020810190506100fa565b50505050905090810190601f1680156101425780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561015c57600080fd5b50610191600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506102ce565b604051808215151515815260200191505060405180910390f35b3480156101b757600080fd5b50610212600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610323565b604051808215151515815260200191505060405180910390f35b606060018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102c45780601f10610299576101008083540402835291602001916102c4565b820191906000526020600020905b8154815290600101906020018083116102a757829003601f168201915b5050505050905090565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff169050919050565b60008060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900460ff161561048457816001908051906020019061038c92919061048e565b507fcda4350c176dee701be26e34bb6ddef641e5f6847b5ff6ca83ccca7faa85ddaf336001604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018060200182810382528381815460018160011615610100020316600290048152602001915080546001816001161561010002031660029004801561046c5780601f106104415761010080835404028352916020019161046c565b820191906000526020600020905b81548152906001019060200180831161044f57829003601f168201915b5050935050505060405180910390a160019050610489565b600090505b919050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106104cf57805160ff19168380011785556104fd565b828001600101855582156104fd579182015b828111156104fc5782518255916020019190600101906104e1565b5b50905061050a919061050e565b5090565b61053091905b8082111561052c576000816000905550600101610514565b5090565b905600a165627a7a72305820e1048c48b1c3fdcb61f121c5dc1c2db485b2a98d1461a28be351104f41063e5a0029'
    SoapBox = web3.eth.contract(abi, bytecode)
    tx_hash = SoapBox.constructor().transact()
    print(tx_hash)
    # https://www.youtube.com/watch?v=UGcInULTCwU&t=212s 

def deploy_ethereum_erc20_smart_contract(): #body_params
    # if blockchain_validator.deploy_ethereum_erc20_smart_contract(body_params):
    Token.deploy("Test Token", "TST", 18, 1e23, {'from': accounts[0]})
    # https://eth-brownie.readthedocs.io/en/stable/quickstart.html
    # https://medium.com/better-programming/part-1-brownie-smart-contracts-framework-for-ethereum-basics-5efc80205413

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