from collections import namedtuple, Counter

import re
import tweepy

import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_KEY=os.getenv("CONSUMER_KEY")
TWITTER_SECRET=os.getenv("CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
TWITTER_ACCESS_SECRET=os.getenv("ACCESS_TOKEN_SECRET")

Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'anthlis'


auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)
print(api)

def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)
        
tweets = list(get_tweets())

print(len(tweets))