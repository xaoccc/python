import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if employee.size < 2:
        return pd.DataFrame(data={'SecondHighestSalary': [None]})
    salaries = employee.groupby(by='salary', as_index=False).count().sort_values(by='salary', ascending=False)[['salary']].rename(columns={'salary':'SecondHighestSalary'})
    if salaries.size < 2:
        salaries.loc[1] = [None]
    return salaries.iloc[[1]]