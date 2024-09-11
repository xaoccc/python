import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employee, employee, right_on='id', left_on='managerId')
    result = result.loc[(result['salary_x'] > result['salary_y']), ['name_x']]
    result.columns = ['Employee']
    return result
