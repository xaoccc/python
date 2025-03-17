import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    all_products = products.groupby(by='product_id', as_index=False).max()[['product_id']]
    dates = products.loc[products['change_date']<'2019-08-17'].groupby(by='product_id', as_index=False)[['product_id', 'change_date']].max()
    actual_prices = dates.merge(products, on=['product_id', 'change_date'])
    return all_products.merge(actual_prices, on='product_id', how='outer').fillna(10)[['product_id', 'new_price']].rename(columns={'new_price': 'price'})