import DataCollection as dc
import Scraper as sc
from Trader import Trader

lowAccountFunds = 25000

ownedStocks = {}

stonks = sc.Scraper().returnStocksDict()[0:4]

dg = dc.DataGetter()


def update():
    stonks.update()
    dg.updateStockData()

def checkAccount():
    if(dg.getUserData().get("Cash") <= lowAccountFunds):
        return False

while True:
    if(checkAccount()):
        checkAccount()

    update()


