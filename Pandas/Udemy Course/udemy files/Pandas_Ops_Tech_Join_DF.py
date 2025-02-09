


# Create three Pandas DataFrames

# This is the basic Carsales DataFrame
Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0, "Sales_place_name", ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], allow_duplicates=False)
print(Carsales)

# This DataFrame contains two Carbrands columns which can be joined to the Carsales DataFrame, horizontally. 
Carsales2 = pd.DataFrame({"Volvo": [3, 4, 0, 0, 1, 3], "Tesla": [2, 8, 0, 1, 1, 4]})
Carsales2.rename(index={0: "One", 1: "Nine", 2: "Three", 3: "Six", 4: "Seven", 5: "Eight"}, inplace=True)
print(Carsales2)

# This DataFrame contains a number of employees per sales place. It will be used to show how joins can be used for tables.
Car_emp = pd.DataFrame({"N_Employees": [12, 18, 13, 14, 8, 12, 3, 9, 4, 21]})
Car_emp.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six", 6: "Seven", 7: "Eight", 8: "Nine", 9: "Ten"}, inplace=True)
print(Car_emp)
