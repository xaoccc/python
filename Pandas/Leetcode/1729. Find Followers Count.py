import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return followers.groupby(by='user_id', as_index=False).count().rename(columns={'follower_id': 'followers_count'})