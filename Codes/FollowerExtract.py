"""
@author: Nicola Gujer

This script will extract a list of followers from a particular user showing the twitter handle and description.
"""

import csv
import tweepy

#Insert keys and access tokens obtained from https://apps.twitter.com/
consumer_key = 'XXXXXXX'
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXXX'
access_token_secret = 'XXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Creates a new csv file into which the extracted data can be written
with open('twitterhandle.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    for follower in tweepy.Cursor(api.followers, screen_name="twitterhandle",
 #Makes the code wait when it has reached the call limit enforced by Twitter
 wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():    
        c= (follower.screen_name.encode('utf-8'))
        d= (follower.description.encode('utf-8'))
        data = [[c,d]]
        a.writerows(data) 