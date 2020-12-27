from DataCollection import DataGetter
from Scraper import Scraper

sc = Scraper()
sc.update()
sc.printStocks()
stockNames = sc.returnStocksDict()
dg = DataGetter(stockNames)
dg.getUserData()
dg.updateStockData("1d", "1m")
print(dg.getCurrentStockVal(stockNames[1]))