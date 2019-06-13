
from collections import namedtuple, Counter
import os
import re

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tweepy
from wordcloud import WordCloud, STOPWORDS

Tweet = namedtuple('Tweet', 'id text created likes rts')

TWITTER_ACCOUNT = 'anthlis'





all_tweets_excl_rts_mentions = ' '.join([tw.text.lower() for tw in tweets
                                        if not tw.text.startswith('RT') and not tw.text.startswith('@')])

pb_mask = np.array(Image.open("twit_outline.png"))
stopwords = set(STOPWORDS)

stopwords.add('co')
stopwords.add('https')

wc = WordCloud(background_color="white", max_words=2000, mask=pb_mask,
               stopwords=stopwords)

wc.generate(all_tweets_excl_rts_mentions)

plt.figure(figsize=(15, 15))
plt.imshow(wc, interpolation="bilinear")
plt.margins(x=0, y=0)
plt.axis("off")