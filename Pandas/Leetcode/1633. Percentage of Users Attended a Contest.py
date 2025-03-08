import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    contest_users = register.merge(users, how='left', on='user_id').drop(columns=['user_name']).groupby(by='contest_id', as_index=False).count().rename(columns={'user_id': 'percentage'})
    users_num = users.shape[0]
    contest_users['percentage'] = ((contest_users['percentage'] / users_num)*100).round(2)
    return contest_users.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])