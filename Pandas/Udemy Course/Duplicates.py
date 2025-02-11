import pandas as pd

# Using functions duplicate(), drop_duplicates()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

cars_csv = pd.read_csv('cars.csv')
print(cars_csv.duplicated(subset=['make', 'model', 'year']))
print(cars_csv.duplicated(subset=['make', 'model', 'year'], keep='last'))

# Here we find the 2 cars with the same make, model, year and color out of 1000 cars
cars_csv['duplicated'] = cars_csv.duplicated(subset=['make', 'model', 'year', 'color'], keep='last')
# Show just these 2 cars without the system column 'duplicated'
print(cars_csv[cars_csv['duplicated'] == True].iloc[:, :8])

pd.set_option('display.max_rows', None)
# Show just the first row of each make
print(cars_csv.drop_duplicates(subset=['make'], keep='first'))