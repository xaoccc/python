# Pandas functions sort_values(), sort_index(), idxmax(), idxmin(), nlargest(), nsmallest(), rank()
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


cars_df = pd.read_csv('cars.csv')

# Execute commands in python terminal
# Sort by one column in descending order
print(cars_df.sort_values(by=['year'], ascending=False))

# Sort by two columns in descending order
print(cars_df.sort_values(by=['year', 'model'], ascending=False))

# Sort by index
print(cars_df.sort_index(ascending=False))

# Find the rows with the largest value by column. If there are more than one max values, it takes the first one
# Returns a SERIES object, which shows the index of the biggest value for each column
print(cars_df.idxmax())
# If we choose to do this by rows, it will throw an error message,
# because all values by row must be of the same type(int, str, etc...)
# print(cars_df.idxmax(axis='columns'))
# Respectively the smallest values:
print(cars_df.idxmin())

# nlargest(n, column_name) takes the first n largest values from a column
# keep='all' shows all duplicates, of these values, so the result might be a DataFrame with rows number bigger than n
# keep='first' and keep='last' make sure that n number of rows are displayed
# keep='first' is the default behavior if the keep argument is not defined
print(cars_df.nlargest(3, 'year'))

# The same logis is with nsmallest, so we can see that with no keep argument, we get 3 rows
# With keep='all' we get 5 more rows (the duplicates of value 1964)
print(cars_df.nsmallest(3, 'year'))

# rank() is calculating a rank (from 0 to n, where n is the number of rows) for each value in each column
# the highest value, the highest the rank, each duplicate value decreases the rank by 0.5,
# so 6 duplicate values decrease the rank by 3.0
print(cars_df.sort_values(by=['year'], ascending=False).rank())