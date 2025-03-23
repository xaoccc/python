import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[(employees.salary < 30000) & (employees.manager_id.isin(employees.employee_id) == False) & (employees.manager_id.notnull())][['employee_id']].sort_values(by='employee_id')