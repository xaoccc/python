import pandas as pd

df = pd.read_csv('../../../work/FreigthVerify.csv')
print(df)
df.to_excel('../../../work/FreightVerifyWorkFile.xlsx')

