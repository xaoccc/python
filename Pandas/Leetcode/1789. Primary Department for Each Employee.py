import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    one_dep = employee.drop_duplicates(subset=['employee_id'], keep=False)
    more_dep = employee[employee['primary_flag'] == 'Y']
    result = pd.concat([one_dep, more_dep])
    return result[['employee_id', 'department_id']]