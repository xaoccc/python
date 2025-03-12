import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    empty_df = pd.DataFrame(data={f'getNthHighestSalary({N})': [None]})

    if int(employee.size / 2) < N or N <= 0:
        return empty_df
    salaries = employee.groupby(by='salary', as_index=False).count().sort_values(by='salary', ascending=False)[
        ['salary']].rename(columns={'salary': f'getNthHighestSalary({N})'})

    if salaries.size < N:
        return empty_df

    return salaries.iloc[[N - 1]]