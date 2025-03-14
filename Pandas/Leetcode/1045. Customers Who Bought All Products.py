import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customers = customer.drop_duplicates(subset=['customer_id', 'product_key']).groupby(by='customer_id', as_index=False).count()
    return customers.loc[customers['product_key'] == len(product)][['customer_id']]