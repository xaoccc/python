import pandas as pd

project = pd.DataFrame({ 'project_id': [1, 1, 1, 2, 2], 'employee_id': [1, 2, 3, 1, 4] })
employee = pd.DataFrame({ 'employee_id': [1, 2, 3, 4], 'name': ['Khaled', 'Ali', 'John', 'Doe'], 'experience_years': [3, 2, 1, 2] })
def project_employees_i(project, employee):


    joined = project.merge(employee, on='employee_id')
    result = joined.groupby('project_id').agg({'experience_years': 'mean'}).reset_index().rename(columns={'experience_years': 'average_years'})
    result['average_years'] = result['average_years'].map('{:.2f}'.format)

    return result

project_employees_i(project, employee)