import pandas as pd
import matplotlib.pyplot as plt
# Seaborns geyser dataset will be used to show regression imputation
import seaborn as sns
# Scikit-learns liner_model will be used for regression imputation
from sklearn import linear_model

# Using functions dropna(), isna(), fillna(), sum(), mean()

# The Carsales dataframe will be modified with missing values
Cardata = { "Mercedes": [2, 4, None, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, None, None, 3, 1]}
Carsales_mv = pd.DataFrame(Cardata)
Carsales_mv.index.rename("Sales place", inplace=True)
Carsales_mv.rename(index={0: "One", 1: "Two", 2: "Three", 3: "Four", 4: "Five", 5: "Six"}, inplace=True)
print(Carsales_mv, f'\n{150*"-"}\n')

# Descriptive statistics for missing values
Carsales_mv_isnull = Carsales_mv.isnull()
print(Carsales_mv_isnull, f'\n{150*"-"}\n')
print("Statistics over missing values per column")
print(Carsales_mv.isnull().sum(), f'\n{150*"-"}\n')

# Decriptive statistics without missing values. Note that the missing values are dropped on a column basis.
print(Carsales_mv.describe(), f'\n{150*"-"}\n')

# Drop missing values either by rows or columns, meaning that we drop entire rows or columns if a missing value exists
Carsales_2 = Carsales_mv.dropna()
Carsales_3 = Carsales_mv.dropna(axis=1)
print(Carsales_2, f'\n{150*"-"}\n')
print(Carsales_3, f'\n{150*"-"}\n')


# Imputation: Zeroes replace the missing values
Carsales_zfill = Carsales_mv.fillna(0, inplace=False)
print(Carsales_zfill, f'\n{150*"-"}\n')

# Imputation: Average/Means replace the missing values
# Carsales_mean is a Pandas Series, containing the mean for each column by columns
Carsales_mean = Carsales_mv.mean()  # Pandas mean() don't include null values in its calculation (it divides by 5 not 6).

Carsales_mfill = Carsales_mv.fillna(Carsales_mean, inplace=False)
print(Carsales_mfill, f'\n{150*"-"}\n')


# Imputation: Regression imputation. Let's load the geyser dataset and make a copy of it.
geyser = sns.load_dataset("geyser")
print(geyser, f'\n{150*"-"}\n')
geyser2=geyser.copy(deep=True)

# Design some missing values in the geyser data.
nlist1= [4, 34, 35, 36, 67, 89, 94, 192, 204]
nlist2= [5, 22, 73, 154, 264]
for n in nlist1:
    geyser2.loc[n, "duration"] = None

for n in nlist2:
    geyser2.loc[n, "waiting"] = None

# print and make another copy.
print(geyser2, f'\n{150*"-"}\n')
print(geyser2.isnull().sum(), f'\n{150*"-"}\n')
geyser3=geyser2.copy(deep=True)

# Simple model based imputation: Pandas Linear interpolation is used to impute values according to some simple
# Interpolation model algorithms, we will try the linear imputation method.
geyser2["duration"] = geyser2["duration"].interpolate(method="linear")
# geyser2["duration"].interpolate(method="linear", inplace=True)
geyser2["waiting"] = geyser2["waiting"].interpolate(method="linear")
# geyser2["waiting"].interpolate(method="linear", inplace=True)

fig, ax = plt.subplots()
geyser2.plot.scatter(x="duration", y="waiting", color = "Blue", marker="x", ax=ax)
geyser.plot.scatter(x="duration", y="waiting", color = "Red", marker="+", ax=ax)
plt.show()
# The plot shows an example of that "point-click-n-forget" imputation with models may cause arbitrary results and careful
# study of data is needed for useful imputation.

# Show some ordinary model based imputation. Use a dual simple linear regression model to estimate
# the missing values on a new copy of the geyser dataframe with missing value rows dropped.
# Use a scikit-learn linear model on a dataframe without missing values.
geyser4_dmv = geyser3.dropna()
model_1 =linear_model.LinearRegression()
model_2 =linear_model.LinearRegression()
model_1.fit(X = geyser4_dmv[["duration"]], y=geyser4_dmv["waiting"])
model_2.fit(X = geyser4_dmv[["waiting"]], y=geyser4_dmv["duration"])

# Some limitations in scikit-learns linearmodel creates a need for modifying the null values or for making
# sub selections of isnotnull values. This code modifies the null values by setting them to extreme values.
geyser3["waiting"].fillna(10000, inplace=True)
geyser3["duration"].fillna(10000, inplace=True)
geyser3["est_duration"] = model_2.predict(geyser3[["waiting"]])
geyser3["est_waiting"] = model_1.predict(geyser3[["duration"]])
print(geyser3)

# Replace the extreme values with estimated values, the imputations
geyser3.loc[geyser3["duration"] > 5000, "duration"] = geyser3["est_duration"]
geyser3.loc[geyser3["waiting"] > 5000, "waiting"] = geyser3["est_waiting"]
print(geyser3)


# Plot the result
fig, ax = plt.subplots()
geyser3.plot.scatter(x="duration", y="waiting", color = "Blue", marker="x", ax=ax)
geyser.plot.scatter(x="duration", y="waiting", color = "Red", marker="+", ax=ax)
plt.show()