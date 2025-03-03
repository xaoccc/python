import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Using functions count(), mean(), std(), min(), max(), sum(), describe(), agg(), value_counts(), apply()
cars_df = pd.read_csv('cars.csv')

# Describe gives all stats at once, and you can see the result of each separate function on a new row
# describe() does not include sum() !!!
# 1. For the whole DataFrame
print(cars_df.describe(), f'\n{150*"-"}\n')
# 2. For one column
print(cars_df.describe().year, f'\n{150*"-"}\n')
# 3. For the selected columns
print(cars_df.describe()[['year', 'mileage']], f'\n{150*"-"}\n')

# Using agg() can show specific aggregate functions (here we can include sum() as well)
# 1. For the whole DataFrame
print(cars_df.agg(['count', 'min', 'max', 'sum']), f'\n{150*"-"}\n')
# 2. For one column. Note that this returns a DataFrame object, instead of Series as you might be expected!
print(cars_df.agg(['count', 'min', 'max', 'sum']).year, f'\n{150*"-"}\n')
# 3. For the selected columns
print(cars_df.agg(['count', 'min', 'max', 'sum'])[['year', 'mileage']], f'\n{150*"-"}\n')

# Adding a new column with aggregate data
cars_df['max_year'] = cars_df.agg(['max']).loc['max', 'year']
print(cars_df, f'\n{150*"-"}\n')

# Create custom statistics about cars' fuel consumption
print(cars_df.agg(Number=('fuel_consumtion', 'count'), Maximum=('fuel_consumtion', 'max'), Min=('fuel_consumtion', 'min')), f'\n{150*"-"}\n')

# Get the max for several columns
print(cars_df[['year', 'fuel_consumtion', 'mileage']].agg('max'), f'\n{150*"-"}\n')
# Using max in a list, returns a DataFrame object, instead of a Series
print(cars_df[['year', 'fuel_consumtion', 'mileage']].agg(['max']), f'\n{150*"-"}\n')


cardata = { "Mercedes": [2, 4, None, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, None, None, 3, 1]}
cardata = pd.DataFrame(cardata)
cardata.index.rename("Sales place", inplace=True)
cardata.rename(index={0: "Sofia", 1: "Burgas", 2: "Blagoevgrad", 3: "Ruse", 4: "Varna", 5: "Plovdiv"}, inplace=True)
print(cardata, f'\n{150*"-"}\n')

# Use agg() on rows. Here we get the total sales for all car models per sale place
print(cardata.agg('sum', axis=1), f'\n{150*"-"}\n')

# Use the above data as new column to the DataFrame object
cardata['Total sales'] = cardata.agg('sum', axis=1)
print(cardata, f'\n{150*"-"}\n')

# The same but using sum(), instead of agg()
cardata['Total sales using sum()'] = cardata[['Mercedes',  'Ford',  'Tata',  'Renault']].sum(axis=1)
print(cardata, f'\n{150*"-"}\n')

# Using value_counts()
print(cars_df[['make', 'model']].value_counts(), f'\n{150*"-"}\n')

# Using normalized value_counts()
cars_df_norm = cars_df[['make', 'model']].value_counts(normalize=True).rename('Normalize data').reset_index()
cars_df_norm2 = cars_df[['make']].value_counts(normalize=True).rename('Normalize make data').reset_index()

print(cars_df_norm, f'\n{150*"-"}\n')

# Using apply()
custom_data = lambda x: x + 100
cars_df['fuel_consumtion'] = cars_df['fuel_consumtion'].apply(custom_data)
print(cars_df, f'\n{150*"-"}\n')

# Convert decimal numbers to percentage and display them as string
# Here you can see both columns before and after apply()
percentage = lambda x: f'{(x * 100):.1f}%'
cars_df_norm2['Normalize data'] = cars_df_norm2['Normalize make data'].apply(percentage)
print(cars_df_norm2, f'\n{150*"-"}\n')

# For more complex checks, we can use standard python functions
def test_function(x):
    if x * 100 > 5:
        return 'many cars'
    elif x * 100 > 1:
        return 'not many'
    else:
        return 'exceptional brand'


cars_df_norm2['test'] = cars_df_norm2['Normalize make data'].apply(test_function)
print(cars_df_norm2, f'\n{150*"-"}\n')


