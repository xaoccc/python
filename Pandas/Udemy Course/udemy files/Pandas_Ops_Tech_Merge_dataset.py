# Create three Pandas DataFrames

# This is the basic Carsales DataFrame extended with two more Sales places plus the index column transformed to a feature column.
Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0, "Sales_place_name", ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], allow_duplicates=True)
Carsales2 = pd.DataFrame({"Sales_place_name": ["South America 1", "Asia 1"], "Mercedes": [3, 4], "Ford": [2, 1], "Tata": [1, 1], "Renault": [1, 0]})
Carsales2.rename(index={0: "Seven", 1: "Eight"}, inplace=True)
Carsales = pd.concat([Carsales, Carsales2])
Carsales.index.rename("Sales place", inplace=True)
Carsales.reset_index(inplace=True)  # Turns index column into a feature column
print(Carsales)

# This DataFrame includes Car inventory data. Unique column values for "Sales_place_name", all included in Carsales and fewer labels than in the Carsales DataFrame.
Inv_data = pd.DataFrame({"Sales_place_name": ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], "Car_inv": [132, 54, 323, 267, 183, 172]})
print(Inv_data)

# This DataFrame includes Car inventory data. Non-unique Column values for "Sales_place_name", some included in Carsales and more labels than in the Carsales DataFrame.
Inv_data2 = pd.DataFrame({"Sales_place_name": ["Europe 1", "Europe 1", "Australia 1", "USA 1", "Asia 1", "Canada 1", "Africa 1", "South America 1", "South America 2"], "Car_inv": [132, 131, 54, 323, 267, 45, 183, 172, 144]})
print(Inv_data2)