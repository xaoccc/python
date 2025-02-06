import pandas as pd

# Using type(), .info(), .loc[], .iloc[], tolist(), lo_list()

Cardata = { "Mercedes": [2, 4, 0, 4, 0, 3],
            "Ford": [3, 0, 0, 1, 16, 12],
            "Tata": [9, 3, 4, 1, 0, 0],
            "Renault": [12, 1, 0, 0, 3, 1]}
Carsales = pd.DataFrame(Cardata)
Carsales.index.rename("Sales place", inplace=True)
Carsales.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)

print(Carsales)
print(Carsales.info())
# Inspect Series object
print(Carsales['Ford'].info())
# Inspect DataFrame object
print(Carsales[['Ford']].info())

# Pandas converts int type to numpy.int64!
# loc[] is used to locate by row/row+column names, iloc[] - by indexes
print(Cardata['Ford'][4], Carsales.loc['Five', 'Ford'])
print(type(Cardata['Ford'][4]), type(Carsales.loc['Five', 'Ford']))
print(Carsales.loc['Five'])

print(Carsales.dtypes)

# to_list() and tolist()
print(Carsales.loc['Five'].tolist())
print(Carsales.loc['Five', 'Ford'].tolist())
# Return list and integer

print(Carsales.loc['Five'].to_list())
# print(Carsales.loc['Five', 'Ford'].to_list())
# Return list and AttributeError: 'numpy.int64' object has no attribute 'to_list'. Did you mean: 'tolist'?



