import threading

import alpaca_trade_api as tradeapi
import json as jason
import yfinance as wahoo

class DataGetter():
    def __init__(self, stockNames):
        self.historical_datas = {}
        self.stockNames = stockNames
        with open('AlpacaKeys.json', 'r') as myfile:
            data=myfile.read()

        vals = jason.loads(data)
        # authentication and connection details
        self.api_key = str(vals['key'])
        self.api_secret = str(vals['secretKey'])
        self.base_url = str(vals['url'])
        self.updateStockData("1d", "1m")
    def getUserData(self):

        # instantiate REST API
        api = tradeapi.REST(self.api_key, self.api_secret, self.base_url, api_version='v2')

        # obtain account information
        return api.get_account()

    def updateStockData(self, period, interval):
            for ticker in self.stockNames:
                self.historical_datas[ticker] = wahoo.Ticker(ticker).history(period= period, interval= interval)


    def getCurrentStockVal(self, ticker):
        try:
            return self.historical_datas[ticker].iloc[len(self.historical_datas[ticker]) - 1].to_dict().get('Close')
        except:
            return -1

