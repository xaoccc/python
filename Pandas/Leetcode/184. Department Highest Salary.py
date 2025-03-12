import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    all_data = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    max_salaries = all_data[['salary', 'departmentId']].groupby(by='departmentId', as_index=False).max()
    return all_data.merge(max_salaries, on=['departmentId', 'salary'], how='inner')[['name_y', 'name_x', 'salary']].rename(columns={'name_y': 'Department',  'name_x':'Employee', 'salary': 'Salary'})