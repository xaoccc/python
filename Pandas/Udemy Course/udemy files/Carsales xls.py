# This Python file creates a "Carsales.csv" file.
import pandas as pd

Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
# Save the DataFrame to a .csv file
Carsales.to_excel("Carsales.xlsx")
del(Carsales)
Carsales = pd.read_excel("Carsales.xlsx")

# Write each column from the DataFrame to a new Excel sheet, as indexes and headers are written as well
# header=True, index=True are default attributes of to_excel()
with pd.ExcelWriter("Carsales2.xlsx") as writer:
    for column in Carsales.columns:
        Carsales[column].to_excel(writer, sheet_name=column)

# We get the data from every sheet that we need (sheet_name=...)
Carsales2 = pd.read_excel("Carsales2.xlsx", index_col=0, sheet_name=["Mercedes", "Ford", "Tata", "Renault"])
# Note that Carsales2 is a dictionary, where the keys are the names of the sheets
# And the values are the data in each sheet as DataFrame format

# In order to convert this dictionary to DataFrame, we should follow these steps:
# 1. Create an empty DataFrame
Carsales3 = pd.DataFrame()
# 2. Get the values from the dictionary
for car_data in Carsales2.values():
    Carsales3 = pd.concat([Carsales3, car_data], axis=1)

print(Carsales3)