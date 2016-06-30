"""
@author: Nicola Gujer

This script will try to extract information about twitter users which will show if they are private profiles or not. If they are private, you will not be able to extract who they follow which will break the Twitter Friendship code. It is best to run this through to check your users as a quick code before you start the long friendship check.
"""

import tweepy
import csv

#Insert keys and access tokens obtained from https://apps.twitter.com/
consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

source=[]
#Opens the csv file that has a list of the twitter handles you wish to check.
with open('twitterusers.csv', 'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        source.append(row[0].strip())

#This will print into a txt file which user the code is checking. If the code breaks, you will know where it got up to which means that user has a private profile and you will need to remove them from your network.
for x in range(0, len(source)): 
    f = open('CheckStatus.txt', 'w')
    print >>f, 'screen_name:', source[x], 'list position:', x
    f.close()  
#Makes the code wait when it has reached the call limit enforced by Twitter.        
    b = api.user_timeline(screen_name=source[x], count=1, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#Prints the Twitter handle into the Python console so you can see who has succesfully been checked.
    print "name:",source[x]
    print ""