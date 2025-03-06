import pandas as pd

# Solution 1
def find_customers1(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    filtered = visits.merge(transactions, on='visit_id', how='left').fillna(0)
    return filtered.loc[filtered['transaction_id'] == 0].groupby(by=['customer_id'], as_index=False).count()[['customer_id', 'transaction_id']].rename(columns={'transaction_id': 'count_no_trans'})

# Solution 2
def find_customers2(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    filtered = visits.merge(transactions, on='visit_id', how='left')
    return filtered.loc[filtered['transaction_id'].isna()].groupby(by=['customer_id'], as_index=False).size().rename(columns={'size': 'count_no_trans'})