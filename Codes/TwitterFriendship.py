"""
@author: Nicola Gujer

This script will check who follows each other from a given list of twitter handles and create an adjacency matrix.
"""

import tweepy
import numpy as np
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
#Opens the csv file that has a list of the twitter handles you wish to check
with open('twitterusers.csv', 'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        source.append(row[0].strip())

friendship = np.zeros((len(source), len(source)),dtype=int)
# entry = 1 if row i is followed by column j

np.shape(friendship)

for x in range(0, len(source)):
#This will print into a txt file which user the code is checking. If the code breaks, you will know where it got up to so the starting point can be altered and you can run the code from the new starting point and add this to the previous output later.
    f = open('SourceStatus.txt', 'w')
    print >>f, 'screen_name:', source[x], 'list position:', x
    f.close()
    for y in range(x, len(source)):
            b = api.show_friendship(source_screen_name=source[x], target_screen_name=source[y],
#Makes the code wait when it has reached the call limit enforced by Twitter
 wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=100, retry_delay=100)
            if str(b[0]).strip('Friendship').split(',')[1].lstrip(' followed_by=') == 'True':
                friendship[x,y]=1
            if str(b[0]).strip('Friendship').split(',')[11].lstrip(' following=') =='True':
                friendship[y,x]=1
            #Creates the adjacency matrix that shows who follows who
            np.savetxt('TwitterFriendship.csv', friendship, fmt='%1.0f',delimiter=',')

print friendship