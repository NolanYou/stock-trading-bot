import DataCollection as dc
import Scraper as sc
from Trader import Trader

lowAccountFunds = 25000




scrape = sc.Scraper()
stonks = scrape.returnStocksDict()
stonks = stonks[0:5]

dg = dc.DataGetter(stonks)

def update():
    scrape.update()
    dg.updateStockData("1d", "1m")

def checkAccount():
    if(float(dg.getUserData().cash) <= lowAccountFunds):
        return False

tr1 = Trader(stonks[0], 40000, dg)
tr2 = Trader(stonks[1], 20000, dg)
tr3 = Trader(stonks[2], 10000, dg)
tr4 = Trader(stonks[3], 10000, dg)
tr5 = Trader(stonks[4], 10000, dg)
tr1.buy()
tr2.buy()
tr3.buy()
tr4.buy()
tr5.buy()

while True:
    if(checkAccount()):
        trCons = Trader(stonks[0], dg.getUserData().get("Cash") - 25000, dg)
        trCons.buy()
    update()


