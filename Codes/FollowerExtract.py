import csv
import tweepy

consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open('Twitter Export csvs/twitterhandle.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    for follower in tweepy.Cursor(api.followers, screen_name="twitterhandle", wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():    
        c= (follower.screen_name.encode('utf-8'))
        d= (follower.description.encode('utf-8'))
        data = [[c,d]]
        a.writerows(data) 