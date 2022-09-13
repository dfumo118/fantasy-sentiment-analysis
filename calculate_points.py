from matplotlib.pyplot import get
import nfl_data_py as nfl

def get_rosters():
    df = nfl.import_rosters([2022], 
        [
            'player_name',
            'player_id'
        ]
    )

    return df

def get_weekly():
    df = nfl.import_weekly_data([2022], 
        [
            'player_id',
            'recent_team',
            'week',
            'fantasy_points_ppr'
        ]
    )

    return df

def get_fantasy_points(player, week):
    rosters = get_rosters()
    weekly = get_weekly()

    df = weekly.merge(rosters)
    row = df.loc[df['player_name'] == player].loc[df['week'] == week]
    if row.empty:
        return 0

    return float(row['fantasy_points_ppr'])
