import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    unique_nums = my_numbers.drop_duplicates(keep=False)

    if unique_nums.empty:
        return pd.DataFrame({'num': [None]})
    max_index = unique_nums['num'].idxmax()
    return unique_nums.loc[[max_index]]