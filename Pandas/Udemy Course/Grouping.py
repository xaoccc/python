import pandas as pd

# Using groupby(), crosstab()
cars_df = pd.read_csv('cars.csv')

pd.set_option('display.max_columns', False)
pd.set_option('display.width', False)


def check_economy(fc):
    if fc < 6:
        return 'eco'
    elif fc < 11:
        return 'normal'
    else:
        return 'gas guzzler'
cars_df['fuel_class'] = cars_df['fuel_consumtion'].apply(check_economy)

print(cars_df, f'\n{"-"*150}')

# Using crosstab()
print(pd.crosstab(cars_df['make'], cars_df['year']), f'\n{"-"*150}')

# With normalize=True/normalize='columns' we can normalize the data (the whole table or by columns)
# print(pd.crosstab(cars_df['make'], cars_df['year'], normalize=True))

# Using groupby()
# Here we show the number of cars per year
print(cars_df.groupby(by=['year']).count()[['make']], f'\n{"-"*150}')

