


# Create Pandas DataFrames

# This code will become the Carsales DataFrame extended with two more Sales places plus the "Rating" and "Target" columns.
Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1], "Rating":["high", "med.", "low", "low", "med.", "high"], "Target":["Y", "Y", "Y", "N", "N", "N"]}
Carsales = pd.DataFrame(Cardata)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0, "Sales_place_name", ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], allow_duplicates=True)
Carsales2 = pd.DataFrame({"Sales_place_name": ["South America 1", "Asia 1"], "Mercedes": [3, 4], "Ford": [2, 1], "Tata": [1, 1], "Renault": [1, 0], "Rating": ["low", "low"], "Target":["N", "N"]})
Carsales2.rename(index={0: "Seven", 1: "Eight"}, inplace=True)
Carsales3 = pd.concat([Carsales, Carsales2])
Carsales3.index.rename("Sales place", inplace=True)
print(Carsales)
print(Carsales3)
