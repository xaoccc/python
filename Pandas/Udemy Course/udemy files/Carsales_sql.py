# This Python file creates a "Carsales.csv" file.
import pandas as pd
import sqlite3

Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
# Save the DataFrame to a .csv file
Carsales.to_csv("Carsales.csv")

# Write DataFrame to database
conn = sqlite3.connect('Cars.db')
Carsales.to_sql('Carsales_Table', conn, if_exists='replace')
del(Carsales)

# Read DataFrame from database
Carsales = pd.read_sql_query('SELECT * FROM Carsales_Table', conn)
print(Carsales)

Carsales = pd.read_sql_query('SELECT Mercedes FROM Carsales_Table', conn)
print(Carsales)

Carsales = pd.read_sql_query('SELECT Mercedes, Ford FROM Carsales_Table', conn)
print(Carsales)