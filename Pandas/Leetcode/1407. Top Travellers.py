import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return rides.groupby(by='user_id', as_index=False).sum()[['user_id', 'distance']].merge(users, on=None, how="right", left_on="user_id", right_on="id")[['name', 'distance']].rename(columns={'distance': 'travelled_distance'}).sort_values(by=['travelled_distance', 'name'], ascending=[False, True]).fillna(0)