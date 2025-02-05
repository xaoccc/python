import pandas as pd

# Adjust display settings
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Adjust width to prevent line breaks

# Create DataFrames and Series

# 1. Using lists
cars_list = ['Audi', 'Volvo', 'Renault']
# Here we have a DataFrame with 1 index column and 1 data column (the list), the data column has an index
cars_df_0 = pd.DataFrame(cars_list)
# Here we have a Series with 1 index column and 1 data column (the list), the data column does not have an index
cars_series = pd.Series(cars_list)

# 2. Using nested lists
cars_nested_lists = [['Audi', 'Volvo', 'Renault'], [12, 13]]
# Here we have a DataFrame with 1 index column and many data columns (the nested lists), each data column has an index
cars_df_1 = pd.DataFrame(cars_nested_lists)
# Here we have a Series with 1 index column and 1 data column - each nested list, the data column does not have an index
cars_series_1 = pd.Series(cars_nested_lists)

# 3. Using dictionaries
cars_dict= {'Audi': [2005, 150, 'green'], 'Volvo': [2018, 112, 'gray'], 'Renault': [2014, 136, 'yellow']}
# Here we have a DataFrame with columns' names the keys and values - the values
# Each values list is a column
# The index column is the default. It contains the indexes of the rows.
cars_df_2 = pd.DataFrame(cars_dict)
# Here we have a Series with 1 index column and 1 data column - each nested list, the data column does not have an index
# The index column contains the names of each row (the dictionary keys), instead if indexes
cars_series_2 = pd.Series(cars_dict)

# 4. Create DataFrame from a csv file
cars_csv = pd.read_csv('cars.csv', delimiter=',')

# Rename index column
cars_csv.index.rename('indexes', inplace=True)

# Rename indexes (not recommended)
cars_csv.rename(index={0: 'zero', 1: 'one'}, inplace=True)

# Get a specific row as a Series object
print(cars_csv.loc[3])

# Create new row
# index is a necessary parameter
# index must be an iterable
# We can add this data in many rows
new_car = pd.DataFrame({'id': 1001, 'make': 'Dacia', 'model': 'Logan', 'color': 'Black', 'fuel_consumtion': 7}, index=[1000,1001])
cars_csv = pd.concat([cars_csv, new_car])

# Create new column as last column
fuel = ['diesel'] * 1002
cars_csv['fuel_type'] = fuel
print(cars_csv)

# Create new column at specific position
power = ['102hp'] * 1002
cars_csv.insert(loc=1, column='power', value=power)
print(cars_csv)

# 5. Create a new DataFrame from separate lists, using zip()
Cars_new = pd.DataFrame(list(zip(fuel, power)), columns=['fuel', 'power'])
print(Cars_new)

# Save the data to excel and csv. We create a new csv file, so we can have a clean input data each time we run this code
cars_csv.to_csv('cars_db.csv')
cars_csv.to_excel('cars_db.xlsx')

# Delete a DataFrame
del(Cars_new)
