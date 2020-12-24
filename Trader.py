import alpaca_trade_api as tradeapi
import json as jason
import datetime as ts


class Trader:
	def __init__(self, stockName, stockNumber, data):
		with open('TradeConstants.json', 'r') as myfile:
			data = myfile.read()

		vals = jason.loads(data)
		# authentication and connection details

		self.stockName = stockName
		self.marginPos = str(vals['PosProfitMargin'])
		self.marginNeg = str(vals['NegProfitMargin'])
		self.stockNumber = stockNumber
		self.data = data



	def getData(self):
		self.init = self.data.getCurrentStockVal(self.stockName)

	def buy(self):
		try:
			tradeapi.submit_order(symbol=self.stockName,
							  qty=self.stockNumber,
							  side='buy',
							  time_in_force='gtc',
							  type='limit',
							  limit_price= initPrice * (1 + marginPos),
							  client_order_id=001,
							  order_class='bracket',
							  stop_loss=dict(stop_price='360.00'),
							  take_profit=dict(limit_price='440.00'))
		except:
			return -1



