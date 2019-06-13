from collections import namedtuple, Counter
import os
import re
import tweepy
import pprint

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



def main():
    app_header()
    print("Starting... ")
    print(api)

    # prints 1272 as at 4 June 19
    tweets = list(get_tweets())
    print(f" There are {len(tweets)} to look through, hang on in there...")

    print("\nGrab a coffee... Likes and Retweets coming up! ")
    likes_and_retweets()
    count_hashtags()


def app_header():
    print()
    print("------------------------------------------------------")
    print("              TWEEPY TWITTER APP")
    print("------------------------------------------------------")
    print()

def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items():
        yield Tweet(tw.id, tw.text, tw.created_at, tw.favorite_count, tw.retweet_count)
        

def likes_and_retweets():
    tweets = list(get_tweets())
    excl_rts = [tweet for tweet in tweets if not tweet.text.startswith('RT')]
    top_10 = sorted(excl_rts, key=lambda tw: (tw.likes + tw.rts)/2, reverse=True)

    fmt = '{likes:<5} | {rts: <5} | {text}'
    print(fmt.format(likes='❤', rts='♺', text='✎'))
    print('-'*100)
    for tw in top_10:
        print(fmt.format(likes=tw.likes, rts=tw.rts, text=tw.text.replace('\n', ' ⏎ ')))

    return

def count_hashtags():
    tweets = list(get_tweets())
    hashtag = re.compile(r'#[-_A-Za-z0-9]+')
    mention = re.compile(r'@[-_A-Za-z0-9]+')

    all_tweets = ' '.join([tw.text.lower() for tw in tweets])
    all_tweets_excl_rt = ' '.join([tw.text.lower() for tw in tweets if not tw.text.startswith('RT')])

    hashtags = hashtag.findall(all_tweets)
    cnt = Counter(hashtags)
    print(cnt.most_common(20))
    return


if __name__ == '__main__':
    main()