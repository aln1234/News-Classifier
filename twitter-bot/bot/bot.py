import tweepy
import random
import time

consumer_key = 'CVXC06C2da7ZRkaJ8tSi79rWC'
consumer_secret = 'hMb5OEIyfBnW6xpEdBRuYA4nUGuWqyz6tTlPzzLnoprEwsSMIh'
key = '1264137430937952258-18uNbrh6lHqWd9hngQ2tgWdYXoZKGP'
secret = 'hlAHiSqXMrcezd8s2LyugKgV0ntJ1ONvf0Ej7gpGMsHIK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


FILE_NAME = '/last_seen.txt'
reply_collection = ['Thank You for the Mention', 'Hurray! You mentioned me!',
                    'Right O, Let Me Follow You Back', 'Finally a Mention! Following you ASAP!']
reply_this = random.choice(reply_collection)

follow_tag = 'dwitnepal'


def read_last_seen():
    FILE_NAME = 'last_seen.txt'      # finding out Tweet ID
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    FILE_NAME = 'last_seen.txt'   # storing Tweet ID
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def test():
    tweets = api.mentions_timeline(
        read_last_seen(), tweet_mode='extended')    # monitors mentions
    for tweet in reversed(tweets):
        if follow_tag in tweet.full_text.lower():
            print("Replied to ID -" + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " " +
                              " " + reply_this + " " + "#" + follow_tag, tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            api.create_friendship(tweet.user.screen_name)
            store_last_seen(FILE_NAME, tweet.id)    # stores last ID


# while True:
#     test()
#     time.sleep(60)
