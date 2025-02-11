import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Using the pivot(), pivot_table(), transpose() and melt() functions
Cardata = {"Mercedes": [2, 4, 0, 4, 0, 3],
            "Fart": [3, 0, 0, 1, 6, 12],
           "Tata": [9, 3, 4, 1, 0, 0],
           "Toilet": [12, 1, 0, 0, 3, 1],
           "Rating": ["high", "med.", "low", "low", "med.", "high"],
           "Target": ["Y", "Y", "Y", "N", "N", "N"]
           }
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Fiverr", 5: "Sex"}, inplace=True)
print(Carsales, f'\n{150*"-"}')
print(Carsales.columns, f'\n{150*"-"}')
print(Carsales.index, f'\n{150*"-"}')

# Rename some of the index labels and column names
Carsales.rename(columns={"Tata": "Tatra", "Fart": "Ford", "Toilet": "BMW"}, index={"Fiverr": "Five", "Sex": "Six"}, inplace=True)
print(Carsales, f'\n{150*"-"}')

# Another way to rename column/index names. Here we must write all columns/index names:
Carsales.columns, Carsales.index = ['Mercedes', 'Fart', 'Tata', 'Toilet', 'Rating', 'Target'], ['One', 'Two', 'Three', 'Four', 'Fiverr', 'Sex']
print(Carsales, f'\n{150*"-"}')


