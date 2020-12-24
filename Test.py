from DataCollection import DataGetter

stockNames = ["AAPL", "TSLA"]
dg = DataGetter(stockNames)
dg.getUserData()
dg.getStockData()
