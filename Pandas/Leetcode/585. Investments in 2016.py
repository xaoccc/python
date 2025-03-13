import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    filter_ph = insurance.drop_duplicates(subset=['lat', 'lon'], keep=False)
    filter_tiv_2015 = insurance[insurance.duplicated(subset=['tiv_2015'], keep=False)]
    return pd.DataFrame({'tiv_2016': filter_ph.merge(filter_tiv_2015, on='pid')[['tiv_2016_x']].sum()}).reset_index().round(2)[['tiv_2016']]