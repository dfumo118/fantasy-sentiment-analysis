import pandas as pd

def csv_to_df(file):
    data = pd.read_csv(file)
    return data

def get_players(df):
    return df['PLAYER_NAME'].to_list()

def save_to_csv(df):
    df.to_csv("player_data.csv", index=False)

