import nfl_data_py as nfl

def get_rosters():
    df = nfl.import_rosters([2021], 
        [
            'player_name',
            'player_id'
        ]
    )

    return df

def get_fantasy_points(player, week):
    rosters = get_rosters()
    weekly = nfl.import_weekly_data([2021], 
        [
            'player_id',
            'recent_team',
            'week',
            'fantasy_points_ppr'
        ]
    )

    df = weekly.merge(rosters)
    row = df.loc[df['player_name'] == player].loc[df['week'] == week]
    if row.empty:
        return 0

    return float(row['fantasy_points_ppr'])
