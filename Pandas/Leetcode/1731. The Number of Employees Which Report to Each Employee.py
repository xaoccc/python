import pandas as pd


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    managers = employees.loc[employees['employee_id'].isin(employees['reports_to'])]
    reports_count = employees[['employee_id', 'reports_to', 'age']].groupby(by='reports_to', as_index=False).count()[['reports_to', 'employee_id']].rename(columns={'reports_to': 'employee_id',  'employee_id': 'reports_count'})
    age = employees[['reports_to', 'age']].groupby(by='reports_to', as_index=False).mean().rename(columns={'reports_to': 'employee_id'})

    fix_round = lambda x: x + 1e-9
    managers = managers.merge(reports_count, on='employee_id', how='right')
    managers = managers.merge(age, on='employee_id', how='right')[['employee_id', 'name',  'reports_count', 'age_y']].rename(columns={'age_y': 'average_age'})
    managers.average_age = managers.average_age.apply(fix_round).round().astype(int)
    return managers
