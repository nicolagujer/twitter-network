"""
@author: Nicola Gujer

This script will extract stats and information about each Twitter user on your list from twitterusers.csv. The TwitterDetails.csv file is what you will use to create your json file.
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
#Opens the csv file that has a list of the twitter handles you wish to get information on.
with open('twitterusers.csv', 'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        source.append(row[0].strip())

#Creates the csv file in which the extracted information will be saved.
with open('TwitterDetails.csv', 'w') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(['id', 'name', 'twitter', 'location', 'description', 'type', 'inst2', 'inst3', 'followers', 'following', 'FavCount', 'NumTweets'])
    for x in range(0, len(source)):   
#Makes the code wait when it has reached the call limit enforced by Twitter        
        b = api.get_user(screen_name=source[x], wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        print "id:",x        
        print "name:",b.name #Name
        print "screen_name:",b.screen_name #Twitter handle
        print "location:", b.location #Location, if specified
        print "description:",b.description #User description
        print "followers_count:",b.followers_count #How many follows user
        print "following_count:",b.friends_count #How many user follows
        print "favourites_count:",b.favourites_count #How many likes user has done
        print "statuses_count:",b.statuses_count #Number of tweets
        print ""
        n = x        
        c = (b.name.encode('utf-8')) 
        d = (b.screen_name.encode('utf-8')) 
        e = (b.location.encode('utf-8')) 
        f = (b.description.encode('utf-8'))
        g = '' #Creates space to insert affiliated institution
        h = '' #Creates space to insert affiliated institution
        i = '' #Creates space to insert affiliated institution
        j = b.followers_count
        k = b.friends_count
        l = b.favourites_count
        m = b.statuses_count
        data = [[n, c, d, e, f, g, h, i, j, k, l, m]]
        a.writerows(data) 