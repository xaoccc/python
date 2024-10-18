import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_data = products.merge(orders, on='product_id')
    result = merged_data.loc[((merged_data['order_date'] >= '2020-02-01') & (merged_data['order_date'] < '2020-03-01')), ['product_name', 'unit']].groupby('product_name', as_index=False).sum()


    return result.loc[result['unit'] >= 100, :]