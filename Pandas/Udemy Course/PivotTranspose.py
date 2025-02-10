import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Using the pivot(), pivot_table(), transpose() and melt() functions
Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, 0, 0, 3, 1], "Rating":["high", "med.", "low", "low", "med.", "high"], "Target":["Y", "Y", "Y", "N", "N", "N"]}
Carsales = pd.DataFrame(Cardata)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0, "Sales_place_name", ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"], allow_duplicates=True)
Carsales2 = pd.DataFrame({"Sales_place_name": ["South America 1", "Asia 1"], "Mercedes": [3, 4], "Ford": [2, 1], "Tata": [1, 1], "Renault": [1, 0], "Rating": ["low", "low"], "Target":["N", "N"]})
Carsales2.rename(index={0: "Seven", 1: "Eight"}, inplace=True)
Carsales3 = pd.concat([Carsales, Carsales2])
Carsales3.index.rename("Sales place", inplace=True)
print(Carsales, f'\n{150*"-"}\n')
print(Carsales3, f'\n{150*"-"}\n')
Carsales_Transposed = Carsales.transpose()
print(Carsales_Transposed, f'\n{150*"-"}\n')
# pivot() takes the values of columns attribute and create rows with the specified columns names,
# Each row contains the values of the specified column
# The number of the columns is equal to all combinations of the values.
# The default index takes the indexes "One", "Two", "Three"..., we will change this to column "Sales_place_name"
# Example:
Carsales_Pivot = Carsales.pivot(index="Sales_place_name", columns=["Rating", "Target"], values=["Mercedes"])
print(Carsales_Pivot, f'\n{150*"-"}\n')
# The result is a table, showing the target markets, ratings and sales numbers for the specific brand "Mercedes"
# If we add one more column to values list, we would get this info for one more brand
Carsales_Pivot = Carsales.pivot(index="Sales_place_name", columns=["Rating", "Target"], values=["Mercedes", "Ford"])
print(Carsales_Pivot, f'\n{150*"-"}\n')

# pivot() does not tolerate duplicate values on columns and index column values
# If we use Carsales3, instead of Carsales, it will throw an error
Carsales_Pivot = Carsales.pivot(index="Target", columns=["Rating"], values="Mercedes")
print(Carsales_Pivot, f'\n{150*"-"}\n')

# The key difference between pivot() and pivot_table() is the aggfunc parameter, which handles duplicates and
# Its default value is "mean", as written below just for information
Carsales_Pivot_Table = Carsales3.pivot_table(index="Target", columns=["Rating"], values=["Mercedes", "Ford", "Tata", "Renault"], aggfunc="mean").round(2)
print(Carsales_Pivot_Table, f'\n{150*"-"}\n')

# Using melt()
Carsales_Melt = pd.melt(Carsales_Pivot, value_vars=["high", "low", "med."], value_name="Mercedes")
print(Carsales_Melt, f'\n{150*"-"}\n')

# Add id_vars parameter and reset the index of the DataFrame Carsales_Pivot
Carsales_Pivot.reset_index(inplace=True)
Carsales_Melt = pd.melt(Carsales_Pivot, id_vars=["Target"], value_vars=["high", "low", "med."], value_name="Mercedes")
print(Carsales_Melt, f'\n{150*"-"}\n')
# As we can see, the original DataFrame could be restored by many operation, so better keep it if you will need it again