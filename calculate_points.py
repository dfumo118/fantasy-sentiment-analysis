import nfl_data_py as nfl

def get_rosters():
    df = nfl.import_rosters([2021], 
        [
            'first_name',
            'last_name',
            'player_id'
        ]
    )

    return df
    # Mac Jones -> 00-0036972

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

    first, last = player.split(' ')

    return float(df.loc[df['last_name'] == last].loc[df['first_name'] == first].loc[df['week'] == week]['fantasy_points_ppr'])