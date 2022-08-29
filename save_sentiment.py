import get_data as gd
import interact_csv as ic

if __name__ == "__main__":
    pos_df = ic.csv_to_df("data/player_pos_data.csv")
    neu_df = ic.csv_to_df("data/player_neu_data.csv")
    neg_df = ic.csv_to_df("data/player_neg_data.csv")
    players = ic.get_players(pos_df) 
    row = [x for x in pos_df.iloc[0] if str(x) != 'nan']
    week = str(len(row))

    tweets_df = gd.pull_tweet_data(players)
    for player in players:
        pos_df.loc[pos_df['PLAYER_NAME'] == player, week] = tweets_df.loc[tweets_df['name'] == player, 'pos']
        neu_df.loc[neu_df['PLAYER_NAME'] == player, week] = tweets_df.loc[tweets_df['name'] == player, 'neu']
        neg_df.loc[neg_df['PLAYER_NAME'] == player, week] = tweets_df.loc[tweets_df['name'] == player, 'neg']

    ic.save_to_csv(pos_df, "data/player_pos_data.csv")
    ic.save_to_csv(neu_df, "data/player_neu_data.csv")
    ic.save_to_csv(neg_df, "data/player_neg_data.csv")