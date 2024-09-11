import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(person, address, on='personId', how="left")
    return data.loc[:, ['firstName', 'lastName', 'city', 'state']]