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

with open('TwitterDetails.csv', 'w') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(['id', 'name', 'twitter', 'location', 'description', 'type', 'inst2', 'inst3', 'followers', 'following', 'FavCount', 'NumTweets'])
    for x in range(0, len(source)):           
        b = api.get_user(screen_name=source[x], wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        print "id:",x        
        print "name:",b.name
        print "screen_name:",b.screen_name
        print "location:", b.location
        print "description:",b.description
        print "followers_count:",b.followers_count
        print "following_count:",b.friends_count
        print "favourites_count:",b.favourites_count
        print "statuses_count:",b.statuses_count
        print ""
        n = x        
        c = (b.name.encode('utf-8')) 
        d = (b.screen_name.encode('utf-8')) 
        e = (b.location.encode('utf-8')) 
        f = (b.description.encode('utf-8'))
        g = ''
        h = ''
        i = ''
        j = b.followers_count
        k = b.friends_count
        l = b.favourites_count
        m = b.statuses_count
        data = [[n, c, d, e, f, g, h, i, j, k, l, m]]
        a.writerows(data) 