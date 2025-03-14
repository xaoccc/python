import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    valid_sales = sales.merge(product, on='product_id')[['product_id', 'year', 'quantity', 'price']]
    find_min_year = sales.drop_duplicates(subset=['product_id', 'year'])[['product_id', 'year']].groupby(by=['product_id'], as_index=False).min()
    return valid_sales.merge(find_min_year, on=['product_id', 'year']).rename(columns={'year': 'first_year'})