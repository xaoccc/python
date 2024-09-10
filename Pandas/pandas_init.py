import pandas as pd


df = pd.read_csv('csv_data.csv')
test = None


print(df)
print(df.loc[(df['Pulse'] < 100) & (df['Calories'] > 300)])
