import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.sort_values(by='event_date', ascending=True, inplace=False).drop_duplicates(subset=['player_id'])
    return df.loc[:, ['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})