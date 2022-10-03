# fantasy-sentiment-analysis
Fantasy football sentiment analysis of the top 100 fantasy football players using Twitter data (tweepy) and nfl_data_py library. This project will extend into February when the 2022-23 NFL season ends.

## Goal

The goal of this program is to determine whether a player's fantasy performance influences public opinion surrounding the player. By comparing twitter sentiment of the player to their weekly score, we can see which players see a change in their public opinion following a good/bad performance. It will also reveal if certain players remain under/over-appreciated despite their performance.

## Sentiment Analysis

The program pulls all Tweets made from Thursday to Tuesday of a given week regarding a certain player's fantasy performance. Then, by running sentiment analysis of those tweets, a percentage of the tweets render either positive, negative, or neutral. Those percentages each week are stored in the corresponding data/*.csv file. The data is pulled weekly through GitHub actions.

## Fantasy Data

All fantasy data is pulled from the [nfl_data_py](https://github.com/cooperdff/nfl_data_py) library, which interacts with nfldata to gather information on the NFL. Most fantasy data will be pulled at the end of the year as the library has yet to include some rookies in their database.
