import pandas as pd


df = pd.read_csv('csv_data.csv')
df.columns = ['a', 'b', 'kur', 'bira']

print(df)
print(df.index)
