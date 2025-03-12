import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    reports_to_managers = employee.groupby(by='managerId', as_index=False).count()
    reports_to_managers = employee.merge(reports_to_managers, left_on='id', right_on='managerId')[['name_x', 'id_y']].rename(columns={'name_x': 'name'})
    return reports_to_managers[reports_to_managers['id_y'] >= 5][['name']]