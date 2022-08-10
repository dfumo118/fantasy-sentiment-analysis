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

file = open("config.json")
config = json.load(file)
file.close()

players = {}
with open("player_data.csv") as f:
    r = csv.reader(f, delimiter=',')
    line_count = 0
    for row in r:
        if line_count != 0:
            players[row[0]] = []
        line_count += 1

client = tweepy.Client(bearer_token=config['bearerToken'])

