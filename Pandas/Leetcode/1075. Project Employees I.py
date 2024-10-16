import pandas as pd

project = pd.DataFrame({ 'project_id': [1, 1, 1, 2, 2], 'employee_id': [1, 2, 3, 1, 4] })
employee = pd.DataFrame({ 'employee_id': [1, 2, 3, 4], 'name': ['Khaled', 'Ali', 'John', 'Doe'], 'experience_years': [3, 2, 1, 2] })
def project_employees_i(project, employee):
    project = project['project_id'].value_counts().reset_index()
    print(project)
    print(employee)
    return

project_employees_i(project, employee)