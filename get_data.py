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
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
import json
import csv
import datetime
import calculate_points as cp

def pull_tweet_info(client, player):
    start_date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%dT00:00:00Z")
    
    tweets = client.search_recent_tweets(
            query= f"{player} fantasy",
            start_time= start_date
        )

    tweet_list = []
    for tweet in tweets.data:
        tweet_list.append(tweet.text)

    tweet_list = [*set(tweet_list)]
    return tweet_list

# to be ran on tuesday following matchups
def pull_tweet_data(players):
    file = open("config.json")
    config = json.load(file)
    file.close()

    client = tweepy.Client(
        bearer_token= config['bearerToken']
        )

    # make query using players, start, end
    for player in players:
        tweet_list = pull_tweet_info(client, player)

        for tweet in tweet_list:
            # analyze tweets for scores
            break

def pull_fantasy_data(players):
    for player in players:
        print(cp.get_fantasy_points(player, 1))