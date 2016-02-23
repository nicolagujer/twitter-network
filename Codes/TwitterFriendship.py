import tweepy
import numpy as np

consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

source=[]
import csv
with open('tweet.csv', 'rU') as f:
    reader=csv.reader(f)
    for row in reader:
        source.append(row[0].strip())

friendship = np.zeros((len(source), len(source)),dtype=int)
# entry=1 if row i is followed by column j

np.shape(friendship)

for x in range(0, len(source)):
    f = open('SourceStatus.txt', 'w')
    print >>f, 'screen_name:', source[x], 'list position:', x
    f.close()
    for y in range(x, len(source)):
            b = api.show_friendship(source_screen_name=source[x], target_screen_name=source[y], wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            if str(b[0]).strip('Friendship').split(',')[1].lstrip(' followed_by=') == 'True':
                friendship[x,y]=1
            if str(b[0]).strip('Friendship').split(',')[11].lstrip(' following=') =='True':
                friendship[y,x]=1
            np.savetxt('Friendship Matrices/TwitterFriendship.csv', friendship, fmt='%1.0f',delimiter=',')

print friendship