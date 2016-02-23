import tweepy
import csv

consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

source=[]
with open('tweet.csv', 'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        source.append(row[0].strip())

for x in range(0, len(source)): 
    f = open('CheckStatus.txt', 'w')
    print >>f, 'screen_name:', source[x], 'list position:', x
    f.close()          
    b = api.user_timeline(screen_name=source[x], count=1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    print "name:",source[x]
    print ""