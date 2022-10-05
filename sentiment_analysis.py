import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from enum import Enum

class Sentiment(Enum):
    NEG = 0
    NEU = 1
    POS = 2


def percentage(part, total):
    return 100*float(part)/float(total)

def analyse_sentiment(string):
    score = SentimentIntensityAnalyzer().polarity_scores(string)
    if score['pos'] > score['neg']:
        return Sentiment.POS
    elif score['neg'] > score['pos']:
        return Sentiment.NEG
    else:
        return Sentiment.NEU