import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users.loc[users['mail'].str.match(r'^[a-zA-Z]+[\w_\-.]*@leetcode\.com$')]