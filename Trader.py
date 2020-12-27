import alpaca_trade_api as tradeapi
import json as jason
import datetime as ts


class Trader:
	def __init__(self, stockName, stockTotal, data):
		with open('AlpacaKeys.json', 'r') as myfile:
			f = myfile.read()

		vals = jason.loads(f)
		# authentication and connection details
		self.api_key = str(vals['key'])
		self.api_secret = str(vals['secretKey'])
		self.base_url = str(vals['url'])
		with open('TradeConstants.json', 'r') as myfile:
			file = myfile.read()

		vals = jason.loads(file)
		# authentication and connection details

		self.stockName = stockName
		self.marginPos = vals['PosProfitMargin']
		self.marginNeg = vals['NegProfitMargin']
		self.stockTotal = stockTotal
		self.data = data
		self.getData()



	def getData(self):
		self.initPrice = self.data.getCurrentStockVal(self.stockName)

	def buy(self):
		stockNumber = self.stockTotal // self.initPrice
		try:
			api = tradeapi.REST(self.api_key, self.api_secret, self.base_url, api_version='v2')
			api.submit_order(symbol=self.stockName,
									  qty=stockNumber,
									  side='buy',
									  time_in_force='gtc',
									  type='limit',
									  limit_price=self.initPrice,
									  order_class='bracket',
									  stop_loss= dict(stop_price=str(self.initPrice * (1 - self.marginNeg))),
									  take_profit=dict(limit_price=str(self.initPrice * (1 + self.marginPos))))
		except:
			print("fail")
			return -1



