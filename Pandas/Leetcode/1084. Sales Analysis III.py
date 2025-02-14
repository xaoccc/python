import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales.drop_duplicates(subset=['product_id'], keep='last', inplace=True)
    sales_filtered = sales.loc[(sales['sale_date'] <= '2019-03-31') & (sales['sale_date'] >= '2019-01-01'), ['product_id']]
    return product.loc[product['product_id'].isin(sales_filtered['product_id']) ,['product_id', 'product_name']]