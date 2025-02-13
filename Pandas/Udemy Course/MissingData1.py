import pandas as pd
from sklearn import linear_model
import numpy as np

data = { "Mercedes": [2, 4, np.nan, 4, 0, 3], "Ford": [3, 0, 0, 1, 6, 12], "Tata":[9, 3, 4, 1, 0, 0], "Renault":[12, 1, np.nan, np.nan, 3, 1]}
df = pd.DataFrame(data)
print(df)

# 1. rows
missing_data = df[df.isna().any(axis=1)]
complete_data = df.dropna()

# 2. completed - predictor/predicted groups
X = complete_data[["Ford", "Tata"]]
y = complete_data[["Mercedes", "Renault"]]

# 3. Training regression model
model = linear_model.LinearRegression()
model.fit(X, y)

# 4. Calculate the values of the missing data
X_missing = missing_data[["Ford", "Tata"]]
predicted = model.predict(X_missing)

# 5. Fill in ONLY the missing data
for i, row in missing_data.iterrows():
    # If "Mercedes" is missing, fill it with the predicted value
    if pd.isna(row["Mercedes"]):
        df.at[i, "Mercedes"] = predicted[i - missing_data.index[0], 0]
    # If "Renault" is missing, fill it with the predicted value
    if pd.isna(row["Renault"]):
        df.at[i, "Renault"] = predicted[i - missing_data.index[0], 1]

print(df.round(0))