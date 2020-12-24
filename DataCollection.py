import threading

import alpaca_trade_api as tradeapi
import json as jason
import yfinance as wahoo

class DataGetter():
    def __init__(self, stockNames):
        self.stockNames = stockNames
        with open('AlpacaKeys.json', 'r') as myfile:
            data=myfile.read()

        vals = jason.loads(data)
        # authentication and connection details
        self.api_key = str(vals['key'])
        self.api_secret = str(vals['secretKey'])
        self.base_url = str(vals['url'])

    def getUserData(self):


        # instantiate REST API
        api = tradeapi.REST(self.api_key, self.api_secret, self.base_url, api_version='v2')

        # obtain account information
        account = api.get_account()

        print(account)

        conn = tradeapi.stream2.StreamConn(self.api_key, self.api_secret, self.base_url)

        @conn.on(r'^account_updates$')
        async def on_account_updates(conn, channel, account):
            print('account', account)

        @conn.on(r'^trade_updates$')
        async def on_trade_updates(conn, channel, trade):
            print('trade', trade)



        connInitArr = ['account_updates', 'trade_updates']

        def ws_start():
            conn.run(connInitArr)

        #start WebSocket in a thread
        ws_thread = threading.Thread(target=ws_start, daemon=True)
        ws_thread.start()

    def getStockData(self):
        self.historical_datas = {}
        for ticker in self.stockNames:
            self.historical_datas[ticker] = wahoo.get_data(ticker)

    def getCurrentStockVal(self):
        historical_datas[ticker]