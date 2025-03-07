import pandas as pd
data = [[1, 'aLice'], [2, 'bOB']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    fix_name = lambda x: x.capitalize()
    users.name = users.name.apply(fix_name)
    return users.sort_values(by=['user_id'])

print(fix_names(users))