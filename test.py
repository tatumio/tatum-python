from tatum.ledger import account, virtual_currency, customer, transaction, subscription, order_book
from tatum.security import key_management_system, address
from tatum.offchain import account as offchainAccount
from tatum.offchain import withdrawal, blockchain
from tatum.blockchain import bitcoin, ethereum, bitcoin_cash, litecoin, xrp, xlm
import json
#________________________________LEDGER/ACCOUNT________________________________________________

# body_params = {"currency": "BTC", 'customer':{'externalId': '3dss5'}}
# if body_params['currency'] != json.loads(account.create_new_account(body_params))['currency']:
#     print('Currency is not same!')
# else:
#     print(account.create_new_account(body_params))



# query_params = {'pageSize': 2, 'offset': 1}
# if query_params['pageSize'] >= len(json.loads(account.list_all_accounts(query_params))):
#     print(account.list_all_accounts(query_params))
# else:
#     print('PageSize is wrong')



# path_params = {'id': '5f85570dd8b99aaea674040a'}
# query_params = {'pageSize': 10}
# resp = account.list_all_customer_accounts(path_params,query_params)
# if query_params['pageSize'] >= len(json.loads(resp)):
#     print(resp)
# else:
#     print('PageSize is wrong')



# path_params = {'id': '5f8434233115f789c669b3bd'}
# resp = account.get_account_by_ID(path_params)
# if path_params['id'] == json.loads(resp)['id']:
#     print(resp)
# else:
#     print('Ids are not same!')




# path_params = {'id': '5f8434233115f789c669b3bd'}
# print(account.get_account_balance(path_params))



# path_params = {'id': '5f8e8a5c3514ae9c925fe868'}
# body_params = {'amount': '10', 'type': 'deposit', "description": "My first blockage"}
# resp = account.block_amount_on_account(path_params, body_params)
# print(resp)




# path_params = {'id': '5f8ec03e9397255214671936'}
# body_params = {'recipientAccountId': '5f8e8a5c3514ae9c925fe868','amount': '1'}
# print(account.unlock_amount_on_account_and_perform_transaction(path_params, body_params))



# path_params = {'id': '5f8ec41e84728ebeea9edcd7'}
# print(account.unblock_blocked_amount_on_account(path_params))



# path_params = {'id': '5f85567db0fb3d7676c269a7'}
# query_params = {'pageSize': 10}
# resp = account.get_blocked_amounts_on_account(path_params, query_params)
# if query_params['pageSize'] >= len(json.loads(resp)):
#     print(resp)
# else:
#     print('PageSize is wrong')



# path_params = {'id': '5f8ec52fa0f566521e50129a'}
# print(account.deactivate_account(path_params))
# print(account.activate_account(path_params))
# print(account.freeze_account(path_params))
# print(account.unfreeze_account(path_params))



#________________________________LEDGER/ VIRTUAL CURRENY________________________________________________


# body_params = {'name': 'VC_CdsekZK', 'supply': '300', 'basePair': 'BTC'}
# resp = virtual_currency.create_new_vitual_currency(body_params)
# if 'currency' in json.loads(resp).keys() & body_params['name'] != json.loads(resp)['currency']:
#     print('Name of currency is not same.')
# else:
#     print(resp)




# body_params = {'name': 'VC_moje', 'basePair': 'ETH'}
# print(virtual_currency.update_vitual_currency(body_params))




# path_params = {'name': 'VC_moje'}
# resp=virtual_currency.get_virtual_currency(path_params)
# if path_params['name'] != json.loads(resp)['name']:
#     print('Names are not same.')
# else:
#     print(resp)




# body_params= {'accountId': '5f8454d45f59ff320a40c114', 'amount': '5000'}
# print(virtual_currency.create_new_supply_of_virtual_currency(body_params))
# print(virtual_currency.destroy_supply_of_virtual_currency(body_params))




#________________________________LEDGER/ CUSTOMER________________________________________________




# query_params = {'pageSize': 10, 'offset': 1}
# resp = customer.list_all_customers(query_params)
# if query_params['pageSize'] >= len(json.loads(resp)):
#     print(resp)
# else:
#     print('PageSize is wrong')



# path_params = {'id': '5f85570dd8b99aaea674040b'}
# resp = customer.get_customer_details(path_params)
# if path_params['id'] == json.loads(resp)['id']:
#     print(resp)
# else:
#     print('Ids are not same')


# path_params = {'id': '5f85570dd8b99aaea674040b'}
# body_params = {'externalId': '123', "providerCountry": 'AD', "customerCountry": 'CZ', "accountingCurrency": 'CZK'}
# resp = customer.update_customer(path_params, body_params)
# if body_params['providerCountry'] != json.loads(resp)['providerCountry']:
#     print('ProviderCountry is not same.')
# else:
#     print(resp)

# print(customer.deactivate_customer(path_params))
# print(customer.activate_customer(path_params))
# print(customer.disable_customer(path_params))
# print(customer.enable_customer(path_params))



#________________________________LEDGER/ TRANSACTION________________________________________________




# query_params = {'pageSize': 10, 'count': 'true'}
# body_params = {"id": "5f85717ded8cda897e2902f4"}
# count = transaction.find_transactions_for_account(query_params, body_params)
# query_params = {'pageSize': 10}
# body_params = {"id": "5f85717ded8cda897e2902f4"}
# transactions = transaction.find_transactions_for_account(query_params, body_params)
# if int(count) != len(json.loads(transactions)):
#     print('Wrong count of transactions')
# else:
#     print(transactions)




# body_params = {'name': 'VC_msgddosje', 'supply': '300', 'basePair': 'BTC'}
# print(virtual_currency.create_new_vitual_currency(body_params))
# body_params = {"currency": "VC_msgddosje"}
# print(account.create_new_account(body_params))
# body_params = {'senderAccountId': '5f901d3891a2a4514431c0cb','recipientAccountId': '5f901db2a0f566521e5012a2','amount': '20'}
# print(transaction.send_payment(body_params))




# path_params = {'id': '5f901d3891a2a4514431c0cb'}
# body_params = {'id': '5f901d3891a2a4514431c0cb'}
# print(account.get_account_balance(path_params))
# query_params = {'pageSize': 10}
# resp = transaction.find_transactions_for_account(query_params, body_params)
# if len(json.loads(resp)) != 0:
#     for i in range(0, len(json.loads(resp))):
#         if body_params['id'] != json.loads(resp)[i]['accountId']:
#             print('Wrong ids.')
# print(resp)



# query_params = {'pageSize': 50}
# body_params = {'id': '5f4fadd111a32373ca107544'}
# print(transaction.find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params))
# body_params = {'account': '5f901db2a0f566521e5012a2'}
# print(transaction.find_transactions_for_ledger(query_params, body_params))
# path_params = {'reference': '9de8580a-4440-49c8-98d7-e3771eaeb6a8'}
# resp = transaction.find_transactions_with_given_reference_across_all_accounts(path_params)
# if len(json.loads(resp)) != 0:
#     for i in range(0, len(json.loads(resp))):
#         if path_params['reference'] != json.loads(resp)[i]['reference']:
#             print('Wrong reference.')
        
# print(resp)




#________________________________LEDGER/ SUBSCRIPTION________________________________________________



# query_params = {'pageSize': 10}
# print(subscription.list_all_active_subscriptions(query_params))



# body_params = {"type":"ACCOUNT_BALANCE_LIMIT","attr":{"limit":"1000","typeOfBalance":"account"}}
# print(subscription.create_new_subcription(body_params))



# path_params = {'id': '5f8ee81d81719e9c8bd3a330'}
# print(subscription.obtain_report_for_subscription(path_params))
# print(subscription.cancel_existing_subscription(path_params))



#________________________________LEDGER/ ORDER BOOK________________________________________________




# query_params = {'pageSize': 10}
# print(order_book.list_all_historical_trades(query_params))
# print(order_book.list_all_active_sell_trades(query_params))
# print(order_book.list_all_active_buy_trades(query_params))

# query_params = {'id': '5a9cfa6ac43321052e7497a6'}
# print(order_book.get_existing_trade(query_params))

# query_params = {'id': '5f86c0c8d0629a31bebc9dfc'}
# print(order_book.cancel_existing_trade(query_params))




# query_params = {'id': '5e9fe150392b786b9dc6f7d8'}
# print(order_book.cancel_all_existing_trades_for_account(query_params))





# body_params = {
# 	"type":"SELL",
# 	"price":"1",
# 	"amount":"10",
# 	"pair":"VC_EUR/VC_CZK",
# 	"currency1AccountId":"5f85b6dc03e34c3164a48b3a",
# 	"currency2AccountId":"5f85b83e2aafd5315e3ab20b"
# }

# print(order_book.store_buy_sell_trade(body_params))




#________________________________LEDGER/ KEY MANAGEMENT________________________________________________

# path_params = {'chain': 'ETH'}
# print(key_management_system.get_pending_transactions_to_sign(path_params))

# path_params = {'id': '5f1aa020a3010936da0201e1', 'txId': '5f1aa020a3010936da0201e1'}
# print(key_management_system.complete_pending_transaction_to_sign(path_params))

# path_params = {'id': '5f37ac89ba22cf64e76e28fe'}
# print(key_management_system.get_transaction_details(path_params))

# path_params = {'id': '5f23efad74077f321604176f'}
# query_params = {'revert': 'false'}
# print(key_management_system.delete_transaction(path_params, query_params))




#________________________________LEDGER/ ADDRESS________________________________________________



# path_params = {'address': 'nevalidniemail@eoopy.com'}
# resp = address.check_malicous_address(path_params)
# if 'status' not in json.loads(resp).keys():
#     print("Response doesn't have key 'status'")
# else:
#     print(resp)




#________________________________OFFCHAIN/ ACCOUNT________________________________________________




# path_params = {'id': '5f887ae3e23af8bf1b813325'}
# query_params = {'index': 3}
# print(offchainAccount.create_new_deposit_address(path_params, query_params))
# print(offchainAccount.get_all_deposit_addresses_for_account(path_params))




# path_params = {'address': 'mrj2QoM9j6JrcAW8JiVfx8M6noK6i8REr9', 'currency': 'BTC'}
# print(offchainAccount.check_if_deposit_address_is_asigned(path_params))




# path_params = {'address': 'bchtest:qpkn9k2h0h0cxzlg59gxfhpkj3508vgq6cfhvzkymf', 'id': '5e71d8a1ec60617c2e301b3a'}
# print(offchainAccount.remove_address_for_account(path_params))
# print(offchainAccount.assign_address_for_account(path_params))





#________________________________OFFCHAIN/ WITHDRAWAL ________________________________________________

# body_params = {
#   "address": "0x8c76887d2e738371bd750362fb55887343472346",
#   "amount": "0.0001",
#   "senderAccountId": "5e71dc0bba2ba02c332f62e2",
#   "senderBlockchainAddress":"0xe31aa662406f984556ac5fa79ef8ddba209ba1f3",
#   "fee":"0.000005"
# }
# print(withdrawal.store_withdrawal(body_params))
# print(withdrawal.check_withdrawal(body_params)) 




# path_params = {'id': '5f1aa020a3010936da0201e1', 'txId': '5f1aa020a3010936da0201e1'}
# print(withdrawal.complete_withdrawal(path_params))




# path_params = {'id': '5f1aa020a3010936da0201e1'}
# print(withdrawal.cancel_withdrawal(path_params))





# body_params = ?????
# withdrawal.broadcast_signed_transaction_and_complete_withdrawal(body_params)



#________________________________ BLOCKCHAIN/ BITCOIN ________________________________________________




# bitcoin.generate_bitcoin_wallet()

# path_params = {'xpub': 'tpubDEwc9DswWvzSoRWF2L2KJssX5ejwX66k9XK8genoBFVPS96ZRCsgAfDsxotgz8nJGE9LbvhWyAcuhCDh9qrRY48yAkNX8X4gHWZ8XtPECBW', 'index': 2} 
# bitcoin.generate_bitcoin_deposit_address_from_extended_public_key(path_params)

# body_params = {
#   "index":1, 
#   "mnemonic": "airport organ level bubble autumn rigid spike girl coffee senior health donate air genuine impulse camp cement fluid coin tell border sport narrow liar"
# }
# bitcoin.generate_bitcoin_private_key(body_params)

# bitcoin.get_blockchain_information()

# path_params = {'i': 1670150}
# bitcoin.get_block_hash(path_params)

# path_params = {'hash': '1670150'}
# bitcoin.get_block_by_hash_or_height(path_params)
# path_params = {'hash': '000000000000006fb7a0612c92addf7b7e6c55b2d307433fe65f551adf8454b4'}
# bitcoin.get_block_by_hash_or_height(path_params)

# path_params = {'hash': 'ad18541c8efa384e49f6da092f0580c646b367de2a48648f19a9e5b8e5e202ae'}
# bitcoin.get_transaction_by_hash(path_params)


# path_params = {'address': 'mrbNHC32JvsBdP4LapQFmNfgHw4oJMCASJ'}
# query_params = {'pageSize': 50, 'offset': 1}
# bitcoin.get_transaction_by_address(path_params, query_params)

# path_params = {'hash': '5b6430975de264abc9b44a7d7261accd3f80f234e6d1ed55893e16a87bc35e38', 'index': 0}
# bitcoin.get_utxo_of_transaction(path_params)


              # body_params = {
              # "txData":" "
              # }
              # bitcoin.broadcast_signed_bitcoin_transaction(body_params)
              # bitcoin.send_bitcoin_to_blockchain_addresses()




#________________________________ BLOCKCHAIN/ ETHEREUM ________________________________________________
# query_params = {'mnemonic': "maze truly suit grape buzz vessel coil broken photo rain material bind struggle hybrid cargo bench trash want ecology black enroll kid birth hurt"}
# print(ethereum.generate_ethereum_wallet(query_params))

# path_params = {'xpub': 'xpub6EZZ1UyZogf9rGwRn9ySSFDLHQbPqswbY8boHAbiLRZy6A79PTq3izy2p435H51e39uLcDzSi3SVYeJ7LtuDfjc6G2nczaZ8We14DmZHsVP', 'index': 1}
# ethereum.generate_ethereum_account_address_from_extended_public_key(path_params)

# body_params = {
# "index":301,
# "mnemonic": "palm mad orbit race shock call author blade write vicious leave charge powder banana task eternal wrap van observe depth surface citizen female bag"
# }

# ethereum.generate_ethereum_private_key(body_params)

              # ethereum.web3_http_driver()
# ethereum.get_current_block()

# path_params = {'hash': '7530722'}
# ethereum.get_block_by_hash(path_params) 

# path_params = {'address': '0x0ff64c166a462b31ed657c9d88c5ac4fef6b88b6'}
# ethereum.get_ethereum_account_balance(path_params)

# path_params = {'address': '0x811dfbff13adfbc3cf653dcc373c03616d3471c9'}
# query_params = {'contractAddress': '0x494394c74bFF7f93C8EB390D4Ab3586Aa2BcAb0C'}
# ethereum.get_ethereum_erc20_account_balance(path_params, query_params)

# path_params = {'hash': '0xdb44e82ba5bdf5d323c766e3bdbd835e6e9a31ccfd7742b4cfc013d869dd6da'}
# ethereum.get_ethereum_transaction(path_params)

# path_params = {'address': '0x811dfbff13adfbc3cf653dcc373c03616d3471c9'}
# ethereum.get_count_of_outgoing_ethereum_transactions(path_params)

# path_params = {'address': '0xdb44e82ba5bdf5d323c766e3bdbd835e6e9a31ccfd7742b4cfc013d869dd6da'}
# query_params = {'pageSize': 10}
# ethereum.get_ethereum_transactions_by_address(path_params, query_params)



#________________________________ BLOCKCHAIN/ BITCOIN CASH ________________________________________________

# bitcoin_cash.generate_bitcoin_cash_wallet()

# path_params = {'xpub': 'xpub6En1k99NzVdo3fg8QE6HjmukpLNcNqvunJRkeid12qfrkPJ4KHaCqtFWLXVGCfkdTfFYpfJbGCiWd57PgjK2iuLhys3CDNwXGhfAamSvxyC', 'index': 5}
# bitcoin_cash.generate_bitcoin_cash_deposit_address_from_extended_public_key(path_params)


# body_params = {
#   "index": 0,
#   "mnemonic": "snack style neutral purity dumb judge oak melody please track old practice"
# }
# bitcoin_cash.generate_bitcoin_cash_private_key(body_params)

# bitcoin_cash.get_bitcoin_cash_blockchain_information()

# path_params = {'hash': '0000000000ec41bc6deb8aea79a926c1b014eac4467c50f55fcbb9710dbdb066'}
# bitcoin_cash.get_bitcoin_cash_block_by_hash(path_params)

# path_params = {'i': 1372778}
# bitcoin_cash.get_bitcoin_cash_block_hash(path_params)

# path_params = {'hash': 'eaec3c2d3d093a83f406e8955fa141e62654bf5bcf108cd30168eaeb89f1ac33'}
# bitcoin_cash.get_bitcoin_cash_transaction_by_hash(path_params)


# path_params = {'address': 'bchtest:qrppgud79n5h5ehqt9s7x8uc82pcag82es0w9tada0'}
# query_params = {'skip': 1}

# bitcoin_cash.get_bitcoin_cash_transaction_by_address(path_params, query_params)



#________________________________ BLOCKCHAIN/ LITECOIN ________________________________________________

# query_params = {'mnemonic': "sknack style nejtral prthrtity durthmb judge oak melody please rack old practice"}
# litecoin.generate_litecoin_wallet(query_params)


# path_params = {'index': 1,'xpub': 'ttub4gLJbfAoX8GS9s1ih2eu68M8XhPLRFy6tZyQQ6Ua1tF3WUyG6tGEGzEir7sxB2A2fp567qXFsr8pCjMrNRopFx2gAJmPgxiwVQYB4tWwQrD'}
# litecoin.generate_litecoin_deposit_address_from_extended_public_key(path_params)

# body_params = {
#   "index": 1,
#   "mnemonic": "brick buyer sniff prefer remind audit town stool awful asset pool state hire town leisure leader tiny coyote lock panda awesome hire bitter regular"
# }
# litecoin.generate_litecoin_private_key(body_params)

# litecoin.get_litecoin_blockchain_information()

# path_params = {'i': 1598649}
# litecoin.get_litecoin_block_hash(path_params)


# path_params = {'hash': '1598649'}
# litecoin.get_litecoin_block_by_hash_or_height(path_params)

# path_params = {'hash': '59eeec314fe5dfe7ffa06ac740884561a3723a9a56ecfcbd9bde4d06dc05f7af'}
# litecoin.get_litecoin_transaction_by_hash(path_params)

# path_params = {'address': 'LZMeooohf7QEU6FNyZcMXerdt5daTJu8gG'}
# query_params = {'pageSize': 50}
# litecoin.get_litecoin_transaction_by_address(path_params, query_params)

# path_params = {'hash': '2d96ec8dfdd2101e47c92e602944a341268b1be73c6dd98860db3faeb3a2c403', 'index': 2}
# litecoin.get_utxo_of_transaction(path_params)



#________________________________ BLOCKCHAIN/ XRP ________________________________________________

# query_params = {'pageSize': 50}
# xrp.generate_xrp_account()
# xrp.get_xrp_blockchain_information()
# xrp.get_actual_blockchain_fee()

# path_params = {'account': 'rPh8bRqJgokvRaSMNPk2wQXFnYFxiSnRsa'}
# xrp.get_account_transactions(path_params)

# path_params = {'i': 1}
# xrp.get_ledger(path_params)


# path_params = {'hash': '773EBE4272BE03919CFFFC135721CE0662A2FB1360849056898BC704F4A7246E'}
# xrp.get_xrp_transaction_by_hash(path_params)

# path_params = {'account': 'rPh8bRqJgokvRaSMNPk2wQXFnYFxiSnRsa'}
# xrp.get_account_info(path_params)
# xrp.get_account_balance(path_params)


# body_params = {
# "fromAccount": "rPh8bRqJgokvRaSMNPk2wQXFnYFxiSnRsa",
# "fromSecret": "ssVCfc6t5topqeHVxTHiW1iBbay85", 
# "rippling": False
# }

# xrp.modify_xrp_account(body_params)

# body_params = {
#   "fromAccount": "rU96Vo5z9HCES8CF3HUqfWs3jZDywgcnpJ",
#   "fromSecret": "snRr2gksVnuRYSfm4TeU1Rb7X5FcX",
#   "issuerAccount": "rpdqTe353R8W2pL3XwdWY9saj7Xn7tXb4B",
#   "limit": "10000",
#   "token": "2939A3EE5E6B4B0D3255BFEF95601890AFD80700"
# }
# xrp.create_update_delete_xrp_trust_line(body_params)

# body_params = {
# 	"fromAccount":"rPh8bRqJgokvRaSMNPk2wQXFnYFxiSnRsa", 
# 	"fromSecret":"ssVCfc6t5topqeHVxTHiW1iBbay85",
# 	"to":"rf7FX2X8AVrJuNoT71xKgJZXNhxrXtXsfd",
# 	"amount": "100"
# }

# xrp.send_xrp_to_blockchain_addresses(body_params)



#________________________________ BLOCKCHAIN/ XLM ________________________________________________

# xlm.generate_xlm_account()
# xlm.get_xlm_blockchain_information()
# xlm.get_actual_blockchain_fee()

# path_params = {'hash': 'cbf8fed5d01b9d76020572eb3112bf5142578a98bc7409e2662e8c13952ce1b6'}
# xlm.get_xlm_transaction_by_hash(path_params)

# path_params = {'account': 'GA442JNOFCOX2R5ZGUCHV65CTEY5KRTU7R7CQLYQQNK7FHKFOTRT4NCP'}
# xlm.get_account_transactions(path_params)
# xlm.get_account_info(path_params)

# body_params = {
#    "fromAccount": "GC2NG6LDLRCQ7MC4ZE5P6TUZPI6ZEKOGAA3M4OHTMCYLQIQ4Y23PHRHE",
# 	"fromSecret": "SBBL2NUXC6DZEX6CMMVQAREJNLJZQNJ6SPWDGEF2TJZV7E3N7QOTN4ET",
# 	"to": "GC2NG6LDLRCQ7MC4ZE5P6TUZPI6ZEKOGAA3M4OHTMCYLQIQ4Y23PHRHE",
# 	"issuerAccount":"GC2NG6LDLRCQ7MC4ZE5P6TUZPI6ZEKOGAA3M4OHTMCYLQIQ4Y23PHRHE",
# 	"amount": "200",
# 	"token":"njn"
# }
# xlm.send_xlm_from_address_to_address(body_params)


# body_params ={
#   "txData": "4351ddfb1d240138893f2817452e1a2cdff1334c73f325019cf59f63a0943a58"
# }
# xlm.broadcast_signed_xlm_transaction(body_params)

# body_params = {
# 	"fromAccount":"GA442JNOFCOX2R5ZGUCHV65CTEY5KRTU7R7CQLYQQNK7FHKFOTRT4NCP",
# 	"fromSecret":"SCKXIEAFDAFF7GN26IMXUNUXRHPH4KHIIYZVIEDA4N4GOLUBFE4TSQMD",
# 	"issuerAccount":"GDYX2H3E53LOU3BTKCLWVAP4DYTNEFT5XQ47KOC6PT4MFJ6KABB7PBND",
# 	"limit":"1000",
# 	"token":"patek"
# }
# xlm.create_update_delete_xlm_trust_line(body_params)



#________________________________ BLOCKCHAIN/ ETHEREUM ________________________________________________

# path_params = {'address': '0x811dfbff13adfbc3cf653dcc373c03616d3471c9', 'contractAddress': '0x494394c74bFF7f93C8EB390D4Ab3586Aa2BcAb0C'}
# ethereum.get_ethereum_erc721_account_balance(path_params)

# path_params = {'address': '0x8c76887d2e738371bd750362fb55887343472346', 'index': 1,'contractAddress': '0x3621381e663883a1d2e483c7da404f68dc0d6d8a'}
# ethereum.get_ethereum_erc721_token(path_params)

# path_params = {'token': '2', 'contractAddress': '0xf9a2d14b1150c2b5d76cedb00f49fa1ea52b5a6c'}
# ethereum.get_ethereum_erc721_token_metadata(path_params)
# ethereum.get_ethereum_erc721_token_owner(path_params)