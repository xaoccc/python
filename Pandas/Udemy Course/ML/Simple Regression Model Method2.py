# Use numpy for its random numbers generator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.formula.api as smf

# Create a DataFrame with random data
x, y = [], []

# scale is defining the deviation from the exact pattern
# loc is defining the center of the normal distribution, the start of the coordinates
# The greater the scale, the more deviation we have from the exact pattern
# (i*1.5)**2 is the exact pattern. In this case we use the square function
for i in range(1, 200):
    x.append(i + np.random.normal(loc=0.0, scale=2.0))
    y.append(i*1.5 + np.random.normal(loc=0.0, scale=2.0))
Regr_data = pd.DataFrame(list(zip(x, y)), columns=['x', 'y'])
print(Regr_data)
Regr_data.plot(x='x', y='y', kind='scatter', s=5)

# Now we have our data in a DataFrame and visualized it
# Transform DataFrame to a list can be used by sklearn
X = Regr_data.iloc[:, 0].values.reshape(-1, 1)
Y = Regr_data.iloc[:, 1].values.reshape(-1, 1)

# Create a linear regression model using sklearn
reg = linear_model.LinearRegression()
reg.fit(X, Y)
Regr_data['y_pred'] = reg.predict(X)

print(Regr_data)
ax = Regr_data.plot(x='x', y='y_pred', kind='line', color='red')
plt.show()
