import pandas as pd
from IPython.display import display

# Using head(), tail(), iloc[], itertuples(), iterrows()
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
cars_csv = pd.read_csv('cars.csv', delimiter=',')
print(cars_csv.head(), f'\n{150*"-"}\n')
print(cars_csv.head(12), f'\n{150*"-"}\n')
print(cars_csv.tail(), f'\n{150*"-"}\n')
print(cars_csv.tail(15), f'\n{150*"-"}\n')
print(cars_csv.iloc[5:17], f'\n{150*"-"}\n')

# itertuples() - slow, not recommended for big data sets
# Still faster than iterrows()
for row in cars_csv.itertuples():
    print(row)

print(f'\n{150*"-"}\n')

pd.set_option('display.max_rows', None)
display(cars_csv)
# pd.reset_option('display.max_rows')