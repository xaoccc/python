import pandas as pd
import statsmodels.formula.api as sm

full_medical_data = pd.read_csv('udemy files/insurance_data.csv')

pd.set_option('display.max_columns', None)
# Place dummy columns and make them with data type integer
full_medical_data1 = pd.get_dummies(full_medical_data, columns=['region'], dtype=int)
print(full_medical_data1)

# Use indicator features using a statsmodels ordinary least sqares regression model
regression_model = sm.ols(formula='charges ~ region_northeast + region_northwest + region_southeast + region_southwest', data=full_medical_data1).fit()
print(regression_model.params)
print(regression_model.summary())

medical_data_smokers = full_medical_data1.loc[full_medical_data1['smoker'] == 'yes']
regression_model_smokers = sm.ols(formula='charges ~ region_northeast + region_northwest + region_southeast + region_southwest', data=medical_data_smokers).fit()
print('\n\nSMOKERS:\n\n', regression_model_smokers.params)
print(regression_model_smokers.summary())

medical_data_non_smokers = full_medical_data1.loc[full_medical_data1['smoker'] == 'no']
regression_model_non_smokers = sm.ols(formula='charges ~ region_northeast + region_northwest + region_southeast + region_southwest', data=medical_data_non_smokers).fit()
print('\n\nNON-SMOKERS:\n\n', regression_model_non_smokers.params)
print(regression_model_non_smokers.summary())

# It is clearly visible that medical expences for smokers are way too high