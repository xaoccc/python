import pandas as pd

# Using
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
cars_csv = pd.read_csv('cars.csv', delimiter=',')