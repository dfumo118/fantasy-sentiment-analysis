from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from PIL import Image
import json
import csv
import datetime
import sentiment_analysis as sa
from sentiment_analysis import Sentiment

# to be ran on tuesday following matchups
def pull_data(players):
    file = open("config.json")
    config = json.load(file)
    file.close()

    client = tweepy.Client(
        bearer_token= config['bearerToken']
        )

    start_date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%dT00:00:00Z")
    # make query using players, start, end
    for player in players:
        tweets = client.search_recent_tweets(
            query= f"{player} fantasy",
            start_time= start_date
        )

        tweet_list = []
        for tweet in tweets.data:
            tweet_list.append(tweet.text)

        tweet_list = [*set(tweet_list)] # removes duplicates
        pos = 0
        neg = 0
        neu = 0
        total = len(tweet_list)
        for tweet in tweet_list:
            # analyze tweets for scores
            sentiment = sa.analyse_sentiment(tweet)
            if sentiment == Sentiment.POS:
                pos += 1
            elif sentiment == Sentiment.NEG:
                neg += 1
            else:
                neu += 1
        
        # assign player percentages
        pos_per = sa.percentage(pos, total)
        neg_per = sa.percentage(neg, total)
        neu_per = sa.percentage(neu, total)
                


if __name__ == "__main__":
    pull_data(["Patrick Mahomes"])