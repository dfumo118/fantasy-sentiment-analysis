import tweepy
import pandas as pd
import os
import datetime
import sentiment_analysis as sa
from sentiment_analysis import Sentiment
import calculate_points as cp

def pull_tweet_info(client, player):
    start_date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y-%m-%dT00:00:00Z")
    
    tweets = client.search_recent_tweets(
            query= f"{player} fantasy",
            start_time= start_date
        )

    tweet_list = []
    if tweets.data:
        for tweet in tweets.data:
            tweet_list.append(tweet.text)

    tweet_list = [*set(tweet_list)]
    return tweet_list

# to be ran on tuesday following matchups
def pull_tweet_data(players):
    result = pd.DataFrame([], columns=['name', 'pos', 'neu', 'neg', 'tweets'])
    try:
        BEARER_TOKEN = os.environ["BEARER_TOKEN"]
    except:
        return

    client = tweepy.Client(
        bearer_token= BEARER_TOKEN
        )

    # make query using players, start, end
    for player in players:
        tweet_list = pull_tweet_info(client, player)
        pos = 0
        neg = 0
        neu = 0
        total = 0
        if tweet_list:
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

        result.loc[len(result.index)] = [player, pos_per, neu_per, neg_per, tweet_list]

    return result

def pull_fantasy_data(players, week):
    result = pd.DataFrame([], columns=['name', 'points'])

    for player in players:
        result.loc[len(result.index)] = [player, cp.get_fantasy_points(player, week)]

    return result