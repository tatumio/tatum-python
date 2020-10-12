from tatum.ledger import account
api = "4f7315df-b6ca-41c7-a45e-95d7e44d4d95"


# body_params = {"currency": "BTC", 'customer':{'externalId': '325'}}
# account.create_new_account("4f7315df-b6ca-41c7-a45e-95d7e44d4d95", body_params)

# query_params = {'pageSize': 10, 'offset': 1}
# account.list_all_accounts("4f7315df-b6ca-41c7-a45e-95d7e44d4d95", query_params)

# path_params = {'id': '5f841b3aaf79e04dc95b0139'}
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

# path_params = {'id': '5f8434233115f789c669b3bd'}
# query_params = {'pageSize': 10}
# account.get_blocked_amounts_on_account(api, path_params, query_params)
# account.unblock_all_blocked_amounts_on_account(api, path_params)

# account.deactivate_account(api,path_params)
# account.activate_account(api, path_params)
# account.freeze_account(api, path_params)
# account.unfreeze_account(api,path_params)