import pandas as pd

# merge() extends join()
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
print(Carsales, f'\n{"-"*150}')

# This DataFrame includes Car inventory data. Unique column values for "Sales_place_name", all included in Carsales and fewer labels than in the Carsales DataFrame.
Inv_data = pd.DataFrame({"Sales_place_name": ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], "Car_inv": [132, 54, 323, 267, 183, 172]})
print(Inv_data, f'\n{"-"*150}')

# This DataFrame includes Car inventory data. Non-unique Column values for "Sales_place_name", some included in Carsales and more labels than in the Carsales DataFrame.
Inv_data2 = pd.DataFrame({"Sales_place_name": ["Europe 1", "Europe 1", "Australia 1", "USA 1", "Asia 1", "Canada 1", "Africa 1", "South America 1", "South America 2"], "Car_inv": [132, 131, 54, 323, 267, 45, 183, 172, 144]})
print(Inv_data2, f'\n{"-"*150}')

# Inner join merge
print(Carsales.merge(Inv_data, on=None, how="inner", left_on="Sales_place_name", right_on="Sales_place_name"), f'\n{"-"*150}')
# You see that using concat(), the column name is duplicated, but the merge() method works this out
print(pd.concat([Carsales, Inv_data], axis=1), f'\n{"-"*150}')
# Using Inv_data2 instead, there will be a duplicate row...
print(Carsales.merge(Inv_data2, on=None, how="inner", left_on="Sales_place_name", right_on="Sales_place_name"), f'\n{"-"*150}')

# Left join merge (duplicate row still exists)
print(Carsales.merge(Inv_data2, on=None, how="left", left_on="Sales_place_name", right_on="Sales_place_name"), f'\n{"-"*150}')

# Right join merge (duplicate row still exists and even 2 more rows added from Inv_data2: Canada 1 and South America 2)
print(Carsales.merge(Inv_data2, on=None, how="right", left_on="Sales_place_name", right_on="Sales_place_name"), f'\n{"-"*150}')

# Outer join merge (duplicate row still exists and even 2 more rows added from Inv_data2: Canada 1 and South America 2)
print(Carsales.merge(Inv_data2, on=None, how="outer", left_on="Sales_place_name", right_on="Sales_place_name"), f'\n{"-"*150}')


# We can fix the duplicate row by summing the Car_inv values in Inv_data2, then merge with Carsales and
# then sum the duplicate values of the columns  Mercedes, Tata, Ford and Renault
# OR get the first/last  value (depends on what do we want)
inv_merged = Inv_data2.groupby('Sales_place_name', as_index=False).agg({
    'Car_inv': 'sum',
})

Carsales3 = Carsales.merge(inv_merged, on=None, how="inner", left_on="Sales_place_name", right_on="Sales_place_name")

Carsales_merged = Carsales3.groupby('Sales_place_name', as_index=False).agg({
    'Car_inv': 'first',
    'Mercedes': 'sum',
    'Ford': 'sum',
    'Tata': 'sum',
    'Renault': 'sum',
    'Sales place': 'first'
})
print(Carsales_merged)