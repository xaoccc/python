# Import Pandas library
import pandas as pd

# Create four Pandas DataFrames

# This is the basic Carsales DataFrame
Cardata = {
    "Mercedes": [2, 4, 0, 4, 0, 3],
    "Ford": [3, 0, 0, 1, 6, 12],
    "Tata": [9, 3, 4, 1, 0, 0],
    "Renault": [12, 1, 0, 0, 3, 1]
}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
Carsales.insert(0,
                "Sales_place_name",
                ["Europe 1", "Australia 1", "USA 1", "Asia 1", "Africa 1", "South America 1"],
                allow_duplicates=False)
print(Carsales, f'\n{"-"*150}')

# This DataFrame may add two Salesplaces to our DataFrame, vertically.
Carsales2 = pd.DataFrame({
    "Sales_place_name": ["South America 1", "Asia 1"],
    "Mercedes": [3, 4],
    "Ford": [2, 1],
    "Tata": [1, 1],
    "Renault": [1, 0]
})
Carsales2.rename(index={0: "Seven", 1: "Eight"}, inplace=True)
print(Carsales2, f'\n{"-"*150}')

# This DataFrame contains two Carbrands columns which can be added to the Carsales DataFrame, horizontally.
Carsales3 = pd.DataFrame({"Volvo": [3, 4, 0, 0, 1], "Tesla": [2, 8, 0, 1, 1], "Tata": [6, 6, 6, 6, 6]})
Carsales3.rename(index={0: "One", 1: "Nine", 2: "Three", 3: "Six", 4: "Seven", 5: "Eight"}, inplace=True)
print(Carsales3, f'\n{"-"*150}')

# This DataFrame may be used display the .concat functions handling of duplicates.
Carsales4 = pd.DataFrame({
    "Sales_place_name": ["Europe 1", "Australia 1"],
    "Mercedes": [2, 4],
    "Ford": [3, 0],
    "Tata": [9, 3],
    "Renault": [12, 1]
})
Carsales4.rename(index={0: "One", 1: "Two"}, inplace=True)
print(Carsales4, f'\n{"-"*150}')

# Add each Dataframe below the previous one
new_df = pd.concat([Carsales, Carsales2])
print(new_df, f'\n{"-"*150}')

# Add each Dataframe next the previous one
new_df = pd.concat([new_df, Carsales3], axis=1)
print(new_df, f'\n{"-"*150}')

# Concat Dataframes with duplicate index labels
new_df = pd.concat([Carsales, Carsales4])
print(new_df, f'\n{"-"*150}')

# Show that the DataFrame contains several DataFrames using multilevel indexing
# Both of the Dataframes have indexes, also the new one has indexes
new_df = pd.concat([Carsales, Carsales4], keys=['Carsales', 'Carsales4'], names=['DataFrame', 'Sales Price'])
print(new_df, f'\n{"-"*150}')
print(new_df.info())
# Using iloc[] will use the 8-indexes DataFrame, BUT
# Using loc[] will use multilevel accessing to the data, similar to nested lists
print(new_df.iloc[0:7])
print(new_df.loc['Carsales'])
print(new_df.loc['Carsales'].loc['One'])