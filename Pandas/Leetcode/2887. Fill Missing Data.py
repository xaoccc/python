import pandas as pd
import numpy as np

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.replace({'quantity': np.nan}, 0)
