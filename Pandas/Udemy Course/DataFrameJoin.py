import pandas as pd

# Create three Pandas DataFrames

# This is the basic Carsales DataFrame
Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0, "Sales_place_name", ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], allow_duplicates=False)
print(Carsales, f'\n{"-"*150}')

# This DataFrame contains two Carbrands columns which can be joined to the Carsales DataFrame, horizontally.
Carsales2 = pd.DataFrame({"Volvo": [3, 4, 0, 0, 1, 3], "Tesla": [2, 8, 0, 1, 1, 4]})
Carsales2.rename(index={0: "One", 1: "Nine", 2: "Three", 3: "Six", 4: "Seven", 5: "Eight"}, inplace=True)
print(Carsales2, f'\n{"-"*150}')

# This DataFrame contains a number of employees per sales place. It will be used to show how joins can be used for tables.
Car_emp = pd.DataFrame({"N_Employees": [12, 18, 13, 14, 8, 12, 3, 9, 4, 21]})
Car_emp.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six", 6: "Seven", 7: "Eight", 8: "Nine", 9: "Ten"}, inplace=True)
print(Car_emp, f'\n{"-"*150}')

# Left join on indexes (on=None)
Carsales3 = Carsales.join(Carsales2, on=None, how="left")
print(Carsales3, f'\n{"-"*150}')

# Right join on indexes (on=None)
Carsales4 = Carsales.join(Carsales2, on=None, how="right")
print(Carsales4, f'\n{"-"*150}')

# This is the same DataFrame as Carsales4, just the columns order is switched
Carsales5 = Carsales2.join(Carsales, on=None, how="left")
print(Carsales5, f'\n{"-"*150}')

# Inner join on indexes (on=None)
Carsales6 = Carsales.join(Carsales2, on=None, how="inner")
print(Carsales6, f'\n{"-"*150}')

# Outer join on indexes (on=None)
Carsales7 = Carsales.join(Carsales2, on=None, how="outer")
print(Carsales7, f'\n{"-"*150}')

# Cross join on indexes (on=None)
Carsales8 = Carsales.join(Carsales2, on=None, how="cross")
print(Carsales8, f'\n{"-"*150}')

# Inner join with practical use
Carsales9 = Carsales.join(Car_emp, on=None, how="inner")
print(Carsales9, f'\n{"-"*150}')