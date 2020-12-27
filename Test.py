import alpaca_trade_api as tradeapi


tradeapi.submit_order(symbol="AAPL",
								  qty=1,
								  side='buy',
								  time_in_force='gtc',
								  type='limit',
								  client_order_id=1,
								  order_class='bracket',
								  take_profit=dict(131.97))
