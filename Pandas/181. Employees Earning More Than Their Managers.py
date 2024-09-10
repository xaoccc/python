import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    result1 = pd.merge( employee, employee, right_on='id', left_on='managerId')
    result = result1.loc[result1['salary_x'] > result1['salary_y']]
    result = result[['name_x']]
    result.columns = ['Employee']

    return result