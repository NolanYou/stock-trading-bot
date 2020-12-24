import re
from collections import defaultdict

import praw
import json as jason
from praw.models import MoreComments


# get 10 hot posts from the MachineLearning subreddit

with open('AlpacaKeys.json', 'r') as myfile:
    data=myfile.read()

vals = jason.loads(data)

# authentication and connection details
secretKey = str(vals['redditSecretKey'])
clientId = str(vals['personalUseScript'])
appName = str(vals['appName'])

reddit = praw.Reddit(client_id=clientId, client_secret=secretKey, user_agent=appName)

tickerDict = defaultdict(int)


pinned_posts = reddit.subreddit('WallStreetBets').sticky()
pinned_posts.comments.replace_more(limit=0)

#These pop up way too frequently. Send help :(
bannedWords = {"AOC", "WSB", "BULL", "LOL", "GIVE", "CNBC", "WSJ", "WILL", "YOLO", "LMAO"}


for top_level_comment in pinned_posts.comments:
    #CapsLock idiot protection :brain:
    if(top_level_comment.body.isupper()):
        continue
    match = re.search(r"\b[A-Z]{3,4}\b[.!?]?", top_level_comment.body)
    if(match != None and not match.group() in bannedWords):
        stockName = match.group()
        tickerDict[stockName] += 1
for ticker in sorted(tickerDict, key=tickerDict.get, reverse= True):
        print(ticker, tickerDict[ticker])
