import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby("customer_number").agg({'order_number': 'count', 'customer_number': 'max'}).sort_values(by='order_number', ascending=False).head(1).loc[:,['customer_number']]