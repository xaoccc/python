data1 = [[1,7], [2,12], [3,17], [4,22], [5,27], [6,32], [7,37], [8,42], [9,47]]
data2 = [[1,7], [2,12], [3,18], [4,24], [5,30], [6,36], [7,42], [8,48], [9,54]]
import pandas as pd
import statsmodels.formula.api as smf

# If we use data1, where y = 5x + 2, the next y value for x=10 should be 52 and the function calculates it exactly
# If we use data2, where y is almost the same (there is deviation e) the next y value is almost correct
# The greater deviation we have from exact pattern, the more error we have
def find_next_list(data):
    # Convert the list of lists to a DataFrame
    df = pd.DataFrame(data, columns=['x', 'y'])

    # Fit a linear regression model
    model = smf.ols('y ~ x', data=df).fit()

    print(model.params)

    # Get the coefficients
    intercept = model.params.iloc[0]
    slope = model.params.iloc[1]

    # Predict the next y value for x=10
    next_x = data[-1][0] + 1
    next_y = intercept + slope * next_x

    return next_y

print(find_next_list(data2))
