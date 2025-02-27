import pandas as pd

df = pd.read_excel('../../../work/FreightVerifyWorkFile.xlsx')
print(df)
df.to_csv('../../../work/FreigthVerify.csv')