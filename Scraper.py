import re
from collections import defaultdict

import praw
import json as jason
from praw.models import MoreComments

class Scraper():


    def __init__(self):
        self.tickerDict = defaultdict(int)

    def update(self):
        with open('AlpacaKeys.json', 'r') as myfile:
            data=myfile.read()

        vals = jason.loads(data)

        # authentication and connection details
        secretKey = str(vals['redditSecretKey'])
        clientId = str(vals['personalUseScript'])
        appName = str(vals['appName'])

        reddit = praw.Reddit(client_id=clientId, client_secret=secretKey, user_agent=appName)




        pinned_posts = reddit.subreddit('WallStreetBets').sticky()
        pinned_posts.comments.replace_more(limit=0)

        #These pop up way too frequently. Send help :(
        bannedWords = {"AOC", "WSB", "BULL", "LOL", " GIVE", "CNBC", "WSJ", "WILL", "YOLO", "LMAO", "AINT", "LETS", "SEC", "GPA", "ELON", "CCP", "KEK"}


        for top_level_comment in pinned_posts.comments:
            #CapsLock idiot protection :brain:
            if(top_level_comment.body.isupper()):
                continue
            match = re.search(r"\b[A-Z]{3,4}\b[.!?]?", top_level_comment.body)
            if(match != None and not match.group() in bannedWords):
                stockName = match.group()
                self.tickerDict[stockName] += 1

    def printStocks(self):
        for ticker in sorted(self.tickerDict, key=self.tickerDict.get, reverse= True):
            print(ticker, self.tickerDict[ticker])

    def returnStocksDict(self):
        return sorted(self.tickerDict, key=self.tickerDict.get, reverse= True)