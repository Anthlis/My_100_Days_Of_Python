from collections import namedtuple, Counter
import os
import re

from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta

import sys

import os
from dotenv import load_dotenv

load_dotenv()

consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)
  
if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
    
    
    tweets = item.statuses_count
    account_created_date = item.created_at
    delta = datetime.utcnow() - account_created_date
    account_age_days = delta.days
    print("Account age (in days): " + str(account_age_days))
    if account_age_days > 0:
      print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
          
#    hashtags = []
#    mentions = []
#    tweet_count = 0
#    end_date = datetime.utcnow() - timedelta(days=30)
#    for status in Cursor(auth_api.user_timeline, id=target).items():
#      tweet_count += 1
#      if hasattr(status, "entities"):
#        entities = status.entities
#        if "hashtags" in entities:
#          for ent in entities["hashtags"]:
#            if ent is not None:
#              if "text" in ent:
#                hashtag = ent["text"]
#                if hashtag is not None:
#                  hashtags.append(hashtag)
#        if "user_mentions" in entities:
#          for ent in entities["user_mentions"]:
#            if ent is not None:
#              if "screen_name" in ent:
#                name = ent["screen_name"]
#                if name is not None:
#                  mentions.append(name)
#      if status.created_at < end_date:
#        break
#        print
#    
#    print("Most mentioned Twitter users:")
#    for item, count in Counter(mentions).most_common(10):
#      print(item + "\t" + str(count))
# 
#    print
#    print("Most used hashtags:")
#    for item, count in Counter(hashtags).most_common(10):
#      print(item + "\t" + str(count))
# 
#    print
#    print ("All done. Processed " + str(tweet_count) + " tweets.")
#    print