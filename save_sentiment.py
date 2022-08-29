import get_data as gd
import interact_csv as ic

if __name__ == "__main__":
    pos_df = ic.csv_to_df("data/player_pos_data.csv")
    neu_df = ic.csv_to_df("data/player_neu_data.csv")
    neg_df = ic.csv_to_df("data/player_neg_data.csv")
    players = ic.get_players(pos_df) 
    row = [x for x in pos_df.iloc[0] if str(x) != 'nan']

    # tweets_df = gd.pull_tweet_data(players)
    print(pos_df)