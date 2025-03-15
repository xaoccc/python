import pandas as pd


def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders.loc[(orders['order_date'] < '2020-01-01') & (orders['order_date'] > '2018-12-31')]
    orders_count = orders.groupby(by='buyer_id', as_index=False).count()[['buyer_id', 'seller_id']].rename(
        columns={'buyer_id': 'user_id', 'seller_id': 'orders_in_2019'})
    return orders_count.merge(users, on='user_id', how='outer').fillna(0)[
        ['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id': 'buyer_id'})
