import pandas as pd

# Using between(), isin(), tolist() and loc[]
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
cars_csv = pd.read_csv('cars.csv', delimiter=',')
# cars_csv.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
# print(cars_csv)

# Rows filter on single condition
print(cars_csv.loc[cars_csv.make == 'Mazda'], f'\n{150*"-"}\n')
# Rows filter on many conditions. Here we find the economic Ford cars
print(cars_csv.loc[(cars_csv.fuel_consumtion > 4) & (cars_csv.fuel_consumtion < 6) & (cars_csv.make == 'Ford')], f'\n{150*"-"}\n')
# Another way to do this, using between() method
print(cars_csv.loc[cars_csv['fuel_consumtion'].between(4, 6) & (cars_csv.make == 'Ford')], f'\n{150*"-"}\n')

# Rows filter, using isin() method
print(cars_csv.loc[cars_csv.index.isin([22, 33, 44])], f'\n{150*"-"}\n')
# We get all indexes, using df.index.isin() and df.index.tolist() and filter indexed by several conditions
print(cars_csv.loc[cars_csv.index.isin([i for i in cars_csv.index.tolist() if ((i % 51 == 0) & (i < 700))])], f'\n{150*"-"}\n')
# We can even combine filter by indexes and by columns contents
print(cars_csv.loc[(cars_csv.index.isin([i for i in cars_csv.index.tolist() if ((i % 51 == 0) & (i < 700))])) & (cars_csv.make == 'Ford')], f'\n{150*"-"}\n')

# Columns and rows filter
print(cars_csv.loc[(cars_csv.fuel_consumtion < 7) & (cars_csv.make == 'Ford'), ['model', 'fuel_consumtion']], f'\n{150*"-"}\n')


