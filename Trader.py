import alpaca_trade_api as tradeapi
import json as jason
import datetime as ts


class Trader:
	def __init__(self, stockName, stockTotal, data):
		with open('TradeConstants.json', 'r') as myfile:
			file = myfile.read()

		vals = jason.loads(file)
		# authentication and connection details

		self.stockName = stockName
		self.marginPos = str(vals['PosProfitMargin'])
		self.marginNeg = str(vals['NegProfitMargin'])
		self.stockTotal = stockTotal
		self.data = data
		self.getData()



	def getData(self):
		self.initPrice = self.data.getCurrentStockVal(self.stockName)

	def buy(self):
		stockNumber = self.stockTotal / self.initPrice
		try:
			tradeapi.submit_order(symbol=self.stockName,
								  qty=stockNumber,
								  side='buy',
								  time_in_force='gtc',
								  type='limit',
								  client_order_id=1,
								  order_class='bracket',
								  stop_loss=dict(self.initPrice * (1 + self.marginNeg)),
								  take_profit=dict(self.initPrice * (1 + self.marginPos)))
		except:
			return -1



