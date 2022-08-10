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

file = open("config.json")
config = json.load(file)
file.close()

players = {}
start_date = ""
end_date = ""
with open("player_data.csv") as f:
    r = csv.reader(f, delimiter=',')
    line_count = 0
    for row in r:
        if line_count == 0:
            last_date = row[len(row)-1]
            month = int(last_date[0:-2])
            year = int(last_date[-2:])

            start_date = datetime.datetime(2000+year, month+1, 1).strftime("%Y-%m-%dT00:00:00Z")
            end_date = (datetime.datetime(2000+year, month+2, 1) - datetime.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00Z")

        else:
            players[row[0]] = []
        line_count += 1

client = tweepy.Client(bearer_token=config['bearerToken'])

# make query using players, start, end