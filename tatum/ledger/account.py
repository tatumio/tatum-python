import http.client
import json
import validator

conn = http.client.HTTPSConnection("api.tatum.io")


def create_new_account(payload, API_KEY):
    validator.create_new_account(payload)

    payload = json.dumps(payload)
    headers = {
        'content-type': "application/json",
        'x-api-key': API_KEY
        }

    conn.request("POST", "/v3/ledger/account", payload, headers)

#   _______________________________________________________________

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))



