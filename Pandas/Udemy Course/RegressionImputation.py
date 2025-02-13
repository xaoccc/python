import pandas as pd
import numpy as np
from sklearn import linear_model

data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Experience': [2, 5, 7, 10, 12, 15, 18, 20, 25, 30],
    'Salary': [40000, 50000, 60000, np.nan, 80000, 90000, np.nan, 110000, 120000, 130000]
}

# Regression Imputation is a method of creating data to fill the missing values, using a regression model
# This model is using specific algorithms to calculate the most appropriate value for each empty cell

employee_data = pd.DataFrame(data)
# Print initial data
print(employee_data)

# 1. Get the rows with missing data and the rows with complete data
# df.isna().any(axis=1) gets all data from all rows where we have missing data
missing_data = employee_data[employee_data.isna().any(axis=1)]
complete_data = employee_data.dropna()

# 2. Divide the columns from the complete data into 2 groups:
# - Data to be used for prediction(predictors) - X
# - Data to be predicted - y
X = complete_data[['Age', 'Experience']]
y = complete_data[['Salary']]

# 3. Train a regression model, in this case using LinearRegression() and fit()
# Here we create a pattern based on the complete_data groups and how does X correlate to y
# Using this information, we can fill the missing data
model = linear_model.LinearRegression()
model.fit(X, y)

# 4. Calculate the values of the missing data, using predict()
# We get the predictors from the missing_data DataFrame
X_missing = missing_data[['Age', 'Experience']]
# And use them to fill the missing data in missing_data DataFrame
# Here we only get the data as a list, but we don't know where to put it
predicted_salaries = model.predict(X_missing)

# 5. Fill in the missing data
# The filtered DataFrame and the list must have the same size!!!
# Otherwise, this will not work
employee_data.loc[employee_data['Salary'].isna(), 'Salary'] = predicted_salaries

# Print final data
print(employee_data)


