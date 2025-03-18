import pandas as pd

data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})

pd.set_option('display.width', False)
def monthly_transactions(transactions):
    transactions['month'] = pd.to_datetime(transactions['trans_date']).dt.strftime('%Y-%m')
    transactions['approved_count'] = transactions['state'].apply(lambda x: 1 if x == 'approved' else 0)
    transactions['approved_total_amount'] = (transactions.approved_count * transactions.amount).astype(int)
    transactions['trans_count'] = transactions.amount.apply(lambda x: 1 if x > 0 else 0)
    return transactions.groupby(by=['month', 'country'], as_index=False, dropna=False)[['trans_count', 'approved_count', 'amount', 'approved_total_amount']].sum().rename(columns={'amount': 'trans_total_amount'})


print(monthly_transactions(transactions))