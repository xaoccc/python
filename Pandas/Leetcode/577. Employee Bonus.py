import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employee, bonus, on='empId', how='left')
    return result.loc[(result['bonus'] < 1000) | (result['bonus'].isna()), ['name', 'bonus']]