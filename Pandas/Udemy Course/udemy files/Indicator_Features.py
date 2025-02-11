import pandas as pd
import statsmodels.formula.api as sm  # this library will be used to demonstrate Indicator features.

# The medical costs dataset "insurance.csv" can be downloaded from Github.com and loaded into a Pandas DataFrame using this codeline. 
med_cost_DF = pd.read_csv("https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv")
# Alternatively, the medical costs dataset can be downloaded from the video lecture as a resource, moved/copied into your
# Python directory and loaded into a Pandas DataFrame with this code
# med_cost_DF = pd.read_csv("insurance_data.csv")
print(med_cost_DF)