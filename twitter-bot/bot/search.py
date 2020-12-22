import tweepy
import time
import random

consumer_key = 'CVXC06C2da7ZRkaJ8tSi79rWC'
consumer_secret = 'hMb5OEIyfBnW6xpEdBRuYA4nUGuWqyz6tTlPzzLnoprEwsSMIh'
key = '1264137430937952258-18uNbrh6lHqWd9hngQ2tgWdYXoZKGP'
secret = 'hlAHiSqXMrcezd8s2LyugKgV0ntJ1ONvf0Ej7gpGMsHIK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


# tag_collection = ['Xiaomi', 'Redmi', 'POCOF2Pro', 'MIUI12', '#MiTrueWirelessEarphones2', 'NoMiWithoutYou', 'XiaomiNepal']
# tag = random.choice(tag_collection)

reply_collection = ['This is a great post!', 'Great Post!', 'Well Said!', 'Great Insight', 'Honestly, this is an excellent tweet!']
reply_this = random.choice(reply_collection)

add_tag = '#BudgetKingXiaomi #XiaomiForever'



def searchbot(filename,tag,reply):

    tweets = tweepy.Cursor(api.search, tag).items(filename)
   
    
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print(reply)

            api.update_status("@" + tweet.user.screen_name + " " + reply_this+ " " + add_tag, tweet.id)
            print('Retweeted!')
            time.sleep(3600)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3600)


# searchbot(filename)