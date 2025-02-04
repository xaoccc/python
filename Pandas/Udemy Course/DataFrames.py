import pandas as pd

# Adjust display settings
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Adjust width to prevent line breaks

# Get the input data from a csv file
Cars = pd.read_csv('cars.csv', delimiter=',')

# Rename index column
Cars.index.rename('indexes', inplace=True)

# Rename indexes (not recommended)
Cars.rename(index={0: 'zero', 1: 'one'}, inplace=True)

# Get a specific row as a Series object
print(Cars.loc[3])

# Create new row
# index is a necessary parameter
# index must be an iterable
# We can add this data in many rows
new_car = pd.DataFrame({'id': 1001, 'make': 'Dacia', 'model': 'Logan', 'color': 'Black', 'fuel_consumtion': 7}, index=[1000,1001])
Cars = pd.concat([Cars, new_car])

# Create new column as last column
fuel = ['diesel'] * 1002
Cars['fuel_type'] = fuel
print(Cars)

# Create new column at specific position
power = value=['102hp'] * 1002
Cars.insert(loc=1, column='power', value=power)
print(Cars)

# Create a new DataFrame from lists, ising zip()
Cars_new = pd.DataFrame(list(zip(fuel, power)), columns=['fuel', 'power'])
print(Cars_new)

# Save the data to excel and csv. We create a new csv file, so we can have a clean input data each time we run this code
Cars.to_csv('cars_db.csv')
Cars.to_excel('cars_db.xlsx')

# Delete a DataFrame
del(Cars_new)
