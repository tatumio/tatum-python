from tatum.ledger import account, virtual_currency, customer, transaction, subscription, order_book
from tatum.security import key_management_system, address
from tatum.offchain import account as offchainAccount
from tatum.offchain import withdrawal

# body_params = {"currency": "BTC", 'customer':{'externalId': '3dss5'}}
# account.create_new_account(body_params)

# query_params = {'pageSize': 10, 'offset': 1}
# account.list_all_accounts(query_params)

# path_params = {'id': '5f85570dd8b99aaea674040a'}
# query_params = {'pageSize': 10}
# account.list_all_customer_accounts(path_params, query_params)

# path_params = {'id': '5f8434233115f789c669b3bd'}
# account.get_account_by_ID(path_params)
# account.get_account_balance(path_params)
# body_params = {'amount': '10', 'type': 'deposit', "description": "My first blockage"}
# account.block_amount_on_account(path_params, body_params)

# path_params = {'id': '5f843e49dc6c947705e83af7'}
# body_params = {'recipientAccountId': '5f84295ddc6c947705e83af6','amount': '1'}
# account.unlock_amount_on_account_and_perform_transaction(path_params, body_params)
# account.unblock_blocked_amount_on_account(path_params)

# path_params = {'id': '5f85567db0fb3d7676c269a7'}
# query_params = {'pageSize': 10}
# account.get_blocked_amounts_on_account(path_params, query_params)
# account.unblock_all_blocked_amounts_on_account(path_params)

# account.deactivate_account(api,path_params)
# account.activate_account(path_params)
# account.freeze_account(path_params)
# account.unfreeze_account(api,path_params)

# body_params = {'name': 'VC_CsZK', 'supply': '300', 'basePair': 'BTC'}
# virtual_currency.create_new_vitual_currency(body_params)

# body_params = {'name': 'VC_moje', 'basePair': 'ETH'}
# virtual_currency.update_vitual_currency(body_params)

# path_params = {'name': 'VC_moje'}
# virtual_currency.get_virtual_currency(path_params)

# body_params= {'accountId': '5f8454d45f59ff320a40c114', 'amount': '5000'}
# virtual_currency.create_new_supply_of_virtual_currency(body_params)
# virtual_currency.destroy_supply_of_virtual_currency(body_params)


# query_params = {'pageSize': 10, 'offset': 1}
# customer.list_all_customers(query_params)
# path_params = {'id': '5f85570dd8b99aaea674040b'}
# customer.get_customer_details(path_params)

# body_params = {'externalId': '123', "providerCountry": 'AD', "customerCountry": 'CZ', "accountingCurrency": 'CZK'}
# customer.update_customer(path_params, body_params)
# customer.deactivate_customer(path_params)
# customer.activate_customer(api,path_params)
# customer.disable_customer(path_params)
# customer.enable_customer(path_params)

# query_params = {'pageSize': 10, 'count': 'true'}
# body_params = {"id": "5f43bb8fda35b2413aa88410"}
# transaction.find_transactions_for_account(query_params, body_params)


# body_params = {'name': 'VC_msgdoje', 'supply': '300', 'basePair': 'BTC'}
# virtual_currency.create_new_vitual_currency(body_params)
# body_params = {"currency": "VC_msdoje"}
# account.create_new_account(body_params)
# body_params = {'senderAccountId': '5f85717ded8cda897e2902f4','recipientAccountId': '5f85717db0fb3d7676c269a9','amount': '20'}
# transaction.send_payment(body_params)

# body_params = {'id': '5f85717db0fb3d7676c269a9'}
# account.get_account_balance(path_params)
# query_params = {'pageSize': 10}
# transaction.find_transactions_for_account(query_params, body_params)
# body_params = {'id': '5f4fadd111a32373ca107544'}
# transaction.find_transactions_for_customer_across_all_accounts_of_customer(query_params, body_params)
# body_params = {'account': '5f85717db0fb3d7676c269a9'}
# transaction.find_transactions_for_ledger(query_params, body_params)
# path_params = {'reference': '9de8580a-4440-49c8-98d7-e3771eaeb6a8'}
# transaction.find_transactions_with_given_reference_across_all_accounts(path_params)

# subscription.list_all_active_subscriptions(query_params)
# body_params = {"type":"ACCOUNT_BALANCE_LIMIT","attr":{"limit":"1000","typeOfBalance":"account"}}
# subscription.create_new_subcription(body_params)
# path_params = {'id': '5f8591d0dc6c947705e83afa'}
# subscription.cancel_existing_subscription(path_params)
# subscription.obtain_report_for_subscription(path_params)

# query_params = {'pageSize': 10}
# order_book.list_all_historical_trades(query_params)
# order_book.list_all_active_sell_trades(query_params)
# order_book.list_all_active_buy_trades(query_params)

# query_params = {'id': '5a9cfa6ac43321052e7497a6'}
# order_book.get_existing_trade(query_params)

# query_params = {'id': '5ed0b1e501b150287a7f6aac'}
# order_book.cancel_existing_trade(query_params)

# query_params = {'id': '5e9fe150392b786b9dc6f7d8'}
# order_book.cancel_all_existing_trades_for_account(query_params)


# body_params = {
# 	"type":"SELL",
# 	"price":"1",
# 	"amount":"10",
# 	"pair":"VC_EUR/VC_CZK",
# 	"currency1AccountId":"5f85b6dc03e34c3164a48b3a",
# 	"currency2AccountId":"5f85b83e2aafd5315e3ab20b"
# }

# order_book.store_buy_sell_trade(body_params)

# path_params = {'chain': 'ETH'}
# key_management_system.get_pending_transactions_to_sign(path_params)

# path_params = {'id': '5f1aa020a3010936da0201e1', 'txId': '5f1aa020a3010936da0201e1'}
# key_management_system.complete_pending_transaction_to_sign(path_params)

# path_params = {'id': '5f37ac89ba22cf64e76e28fe'}
# key_management_system.get_transaction_details(path_params)

# path_params = {'id': '5f23efad74077f321604176f'}
# query_params = {'revert': 'false'}
# key_management_system.delete_transaction(path_params, query_params)

# path_params = {'address': 'nevalidniemail@eoopy.com'}
# address.check_malicous_address(path_params)

# path_params = {'id': '5f887ae3e23af8bf1b813325'}
# query_params = {'index': 3}
# offchainAccount.create_new_deposit_address(path_params, query_params)
# offchainAccount.get_all_deposit_addresses_for_account(path_params)

# path_params = {'address': 'mrj2QoM9j6JrcAW8JiVfx8M6noK6i8REr9', 'currency': 'BTC'}
# offchainAccount.check_if_deposit_address_is_asigned(path_params)

path_params = {'address': 'bchtest:qpkn9k2h0h0cxzlg59gxfhpkj3508vgq6cfhvzkymf', 'id': '5e71d8a1ec60617c2e301b3a'}
# offchainAccount.remove_address_for_account(path_params)
# offchainAccount.assign_address_for_account(path_params)

body_params = {
  "address": "0x8c76887d2e738371bd750362fb55887343472346",
  "amount": "0.0001",
  "senderAccountId": "5e71dc0bba2ba02c332f62e2",
  "senderBlockchainAddress":"0xe31aa662406f984556ac5fa79ef8ddba209ba1f3",
  "fee":"0.000005"
}
# withdrawal.store_withdrawal(body_params)
# withdrawal.check_withdrawal(body_params) 

# path_params = {'id': '5f1aa020a3010936da0201e1', 'txId': '5f1aa020a3010936da0201e1'}
# withdrawal.complete_withdrawal(path_params)

# path_params = {'id': '5f1aa020a3010936da0201e1'}
# withdrawal.cancel_withdrawal(path_params)


# body_params = ?????
# withdrawal.broadcast_signed_transaction_and_complete_withdrawal(body_params)
