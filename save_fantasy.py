import get_data as gd
import interact_csv as ic

if __name__ == "__main__":
    df = ic.csv_to_df("data/player_fantasy_data.csv")
    players = ic.get_players(df) 
    row = [x for x in df.iloc[0] if str(x) != 'nan']
    week = len(row)

    points_df = gd.pull_fantasy_data(players, week)
    for player in players:
        df.loc[df['PLAYER_NAME'] == player, str(week)] = points_df.loc[points_df['name'] == player, 'points']

    ic.save_to_csv(df, "data/player_fantasy_data.csv")