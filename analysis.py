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

file = open("config.json")
config = json.load(file)
consumerKey = config['consumerKey']
consumerSecret = config['consumerSecret']
accessToken = config['accessToken']
accessTokenSecret = config['accessTokenSecret']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Good!")
except:
    print("No bueno")