import threading

import alpaca_trade_api as tradeapi
import json as jason

open('AlpacaKeys.json')
with open('AlpacaKeys.json', 'r') as myfile:
    data=myfile.read()

vals = jason.loads(data)
# authentication and connection details
api_key = str(vals['key'])
api_secret = str(vals['secretKey'])
base_url = str(vals['url'])

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')

# obtain account information
account = api.get_account()


print(account)

conn = tradeapi.stream2.StreamConn(api_key, api_secret, base_url)

@conn.on(r'^account_updates$')
async def on_account_updates(conn, channel, account):
    print('account', account)

@conn.on(r'^trade_updates$')
async def on_trade_updates(conn, channel, trade):
    print('trade', trade)

def ws_start():
	conn.run(['account_updates', 'trade_updates'])

#start WebSocket in a thread
ws_thread = threading.Thread(target=ws_start, daemon=True)
ws_thread.start()