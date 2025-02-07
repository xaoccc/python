import pandas as pd
from IPython.display import display

# Using head(), tail(), loc[], iloc[], itertuples(), iterrows()
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
cars_csv = pd.read_csv('cars.csv', delimiter=',')
cars_csv.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
print(cars_csv.head(), f'\n{150*"-"}\n')
print(cars_csv.head(12), f'\n{150*"-"}\n')
print(cars_csv.tail(), f'\n{150*"-"}\n')
print(cars_csv.tail(15), f'\n{150*"-"}\n')


# itertuples() - slow, not recommended for big data sets
# Still faster than iterrows()

# for row in cars_csv.itertuples():
#     print(row)
#
# print(f'\n{150*"-"}\n')

# pd.set_option('display.max_rows', None)
# display(cars_csv)
# pd.reset_option('display.max_rows')

# Filter by rows, using index
print(cars_csv.iloc[5:12], f'\n{150*"-"}\n')
# Filter by columns, using index
print(cars_csv.iloc[:, 2:5], f'\n{150*"-"}\n')
# Filter by rows and columns, using index
print(cars_csv.iloc[5:12, 2:5], f'\n{150*"-"}\n')

# Rows selection, using index
print(cars_csv.iloc[[5, 17, 99]], f'\n{150*"-"}\n')
# Columns selection, using index
print(cars_csv.iloc[:, [1, 5, 7]], f'\n{150*"-"}\n')
# Rows and columns selection, using index
print(cars_csv.iloc[[5, 17, 99], [1, 5, 7]], f'\n{150*"-"}\n')

# Filter by rows, using row name
print(cars_csv.loc['Two':'Five'], f'\n{150*"-"}\n')
# Filter by columns, using column name
print(cars_csv.loc[:, 'model':'color'], f'\n{150*"-"}\n')
# Filter by rows and columns, using row and column names
print(cars_csv.loc['Two':'Five', 'model':'color'], f'\n{150*"-"}\n')

# Rows selection, using row name
print(cars_csv.loc[['Two', 'Five']], f'\n{150*"-"}\n')
# Columns selection, using column name
print(cars_csv.loc[:, ['model', 'color']], f'\n{150*"-"}\n')
# Rows and columns selection, using row and column names
print(cars_csv.loc[['Two', 'Five'], ['model', 'color']], f'\n{150*"-"}\n')

# Print rows reversed
print(cars_csv.head().loc[::-1], f'\n{150*"-"}\n')
# Print columns reversed
print(cars_csv.head().loc[:, ::-1], f'\n{150*"-"}\n')
