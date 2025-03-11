import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(salaries, on='employee_id', how='outer')
    return merged[merged.isna().any(axis=1)][['employee_id']]