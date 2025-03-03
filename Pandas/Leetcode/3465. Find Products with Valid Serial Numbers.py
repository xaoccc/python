import pandas as pd


def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[products['description'].str.contains(r'\bSN\d{4}-\d{4}\b', na=False)]
