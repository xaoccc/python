import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer[['visited_on', 'amount']].sort_values(by='visited_on').groupby(by='visited_on', as_index=False).sum()
    customer['average_amount'] = customer['amount'].rolling(window=7, min_periods=1).mean().round(2)
    customer['amount'] = customer['amount'].rolling(window=7, min_periods=1).sum()
    return customer.iloc[6:]