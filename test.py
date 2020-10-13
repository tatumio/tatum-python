from tatum.ledger import account, virtual_currency, customer, transaction, subscription, order_book
api = "4f7315df-b6ca-41c7-a45e-95d7e44d4d95"


# body_params = {"currency": "BTC", 'customer':{'externalId': '3ds5'}}
# account.create_new_account("4f7315df-b6ca-41c7-a45e-95d7e44d4d95", body_params)

# query_params = {'pageSize': 10, 'offset': 1}
# account.list_all_accounts("4f7315df-b6ca-41c7-a45e-95d7e44d4d95", query_params)

# path_params = {'id': '5f85570dd8b99aaea674040a'}
# query_params = {'pageSize': 10}
# account.list_all_customer_accounts(api, path_params, query_params)

# path_params = {'id': '5f8434233115f789c669b3bd'}
# account.get_account_by_ID(api, path_params)
# account.get_account_balance(api, path_params)
# body_params = {'amount': '10', 'type': 'deposit', "description": "My first blockage"}
# account.block_amount_on_account(api, path_params, body_params)

# path_params = {'id': '5f843e49dc6c947705e83af7'}
# body_params = {'recipientAccountId': '5f84295ddc6c947705e83af6','amount': '1'}
# account.unlock_amount_on_account_and_perform_transaction(api, path_params, body_params)
# account.unblock_blocked_amount_on_account(api, path_params)

# path_params = {'id': '5f85567db0fb3d7676c269a7'}
# query_params = {'pageSize': 10}
# account.get_blocked_amounts_on_account(api, path_params, query_params)
# account.unblock_all_blocked_amounts_on_account(api, path_params)

# account.deactivate_account(api,path_params)
# account.activate_account(api, path_params)
# account.freeze_account(api, path_params)
# account.unfreeze_account(api,path_params)

# body_params = {'name': 'VC_CZK', 'supply': '300', 'basePair': 'BTC'}
# virtual_currency.create_new_vitual_currency(api, body_params)

# body_params = {'name': 'VC_moje', 'basePair': 'ETH'}
# virtual_currency.update_vitual_currency(api, body_params)

# path_params = {'name': 'VC_moje'}
# virtual_currency.get_virtual_currency(api, path_params)

# body_params= {'accountId': '5f8454d45f59ff320a40c114', 'amount': '5000'}
# virtual_currency.create_new_supply_of_virtual_currency(api, body_params)
# virtual_currency.destroy_supply_of_virtual_currency(api, body_params)


# query_params = {'pageSize': 10, 'offset': 1}
# customer.list_all_customers(api, query_params)
# path_params = {'id': '5f85570dd8b99aaea674040b'}
# customer.get_customer_details(api, path_params)

# body_params = {'externalId': '123', "providerCountry": 'AD', "customerCountry": 'CZ', "accountingCurrency": 'CZK'}
# customer.update_customer(api, path_params, body_params)
# customer.deactivate_customer(api, path_params)
# customer.activate_customer(api,path_params)
# customer.disable_customer(api, path_params)
# customer.enable_customer(api, path_params)

# query_params = {'pageSize': 10, 'count': 'true'}
# body_params = {"id": "5f43bb8fda35b2413aa88410"}
# transaction.find_transactions_for_account(api, query_params, body_params)


# body_params = {'name': 'VC_msdoje', 'supply': '300', 'basePair': 'BTC'}
# virtual_currency.create_new_vitual_currency(api, body_params)
# body_params = {"currency": "VC_msdoje"}
# account.create_new_account(api, body_params)
# body_params = {'senderAccountId': '5f85717ded8cda897e2902f4','recipientAccountId': '5f85717db0fb3d7676c269a9','amount': '20'}
# transaction.send_payment(api, body_params)

# body_params = {'id': '5f85717db0fb3d7676c269a9'}
# account.get_account_balance(api, path_params)
# query_params = {'pageSize': 10}
# transaction.find_transactions_for_account(api, query_params, body_params)
# body_params = {'id': '5f4fadd111a32373ca107544'}
# transaction.find_transactions_for_customer_across_all_accounts_of_customer(api, query_params, body_params)
# body_params = {'account': '5f85717db0fb3d7676c269a9'}
# transaction.find_transactions_for_ledger(api, query_params, body_params)
# path_params = {'reference': '9de8580a-4440-49c8-98d7-e3771eaeb6a8'}
# transaction.find_transactions_with_given_reference_across_all_accounts(api, path_params)

# subscription.list_all_active_subscriptions(api, query_params)
# body_params = {"type":"ACCOUNT_BALANCE_LIMIT","attr":{"limit":"1000","typeOfBalance":"account"}}
# subscription.create_new_subcription(api, body_params)
# path_params = {'id': '5f8591d0dc6c947705e83afa'}
# subscription.cancel_existing_subscription(api, path_params)
# subscription.obtain_report_for_subscription(api, path_params)

# query_params = {'pageSize': 10}
# order_book.list_all_historical_trades(api, query_params)
# order_book.list_all_active_sell_trades(api, query_params)
# order_book.list_all_active_buy_trades(api, query_params)

# query_params = {'id': '5a9cfa6ac43321052e7497a6'}
# order_book.get_existing_trade(api, query_params)

# query_params = {'id': '5ed0b1e501b150287a7f6aac'}
# order_book.cancel_existing_trade(api, query_params)

# query_params = {'id': '5e9fe150392b786b9dc6f7d8'}
# order_book.cancel_all_existing_trades_for_account(api, query_params)


body_params = {
	"type":"SELL",
	"price":"1",
	"amount":"10",
	"pair":"VC_EUR/VC_CZK",
	"currency1AccountId":"5f85b6dc03e34c3164a48b3a",
	"currency2AccountId":"5f85b83e2aafd5315e3ab20b"
}

order_book.store_buy_sell_trade(api, body_params)