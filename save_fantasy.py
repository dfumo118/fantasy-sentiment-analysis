import get_data as gd
import interact_csv as ic

if __name__ == "__main__":
    df = ic.csv_to_df("player_fantasy_data.csv")
    players = ic.get_players(df) 
    row = [x for x in df.iloc[0] if str(x) != 'nan']
    week = len(row) + 1

    points_df = gd.pull_fantasy_data(players, week)