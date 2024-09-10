## Pandas notes
### Data Types
- pd.DataFrame(dict) - converts python dictionary to data frame (table)
- pd.Series(string, list or dict) - converts python data to series (column)
- when dict is given, df dict values must be lists, series accept everything
- series is one column, dict key is the index, dict value is the value in the column
- df is multiple columns, dict key is the label, dict value is the row value
- Filter data :
```
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
filtered_data = df.loc([['b', 'c']])
```
`df.index = [...]` - assign the index values (rows labels)
`df.columns = [...]` - assign the columns labels
- each of these lists should have the exact length as the row/columns

### Import 
`pd.read_csv('data.csv')` - reads csv data
`pd.read_json('data.json')` - reads json data

### Analyzing DataFrames
`df.head()` - first 5 rows if not specified  
`df.tail()` - last 5 rows if not specified  
`df.info()` - detailed info about the df  
`df.size` - shows the total number of cells

### Data Cleaning
`df.dropna()` - converts missing values to NaN. Creates a new df  
`df.dropna(inplace = True)` - updates the existing df 
`df.dropna(axis=0)` - removes empty rows  
`df.dropna(axis=1)` - removes empty columns  
`df.dropna(how='any')` - removes data if any of the values is missing  
`df.dropna(how='all')` - removes data if all the values is missing  
`df.dropna(thresh=n)` - n is an integer showing how many values should be non-empty in order to remove data. Cannot be used with how=  

### Filter Data
`df.loc[(df['Pulse'] < 100) & (df['Calories'] > 300)]` - using loc[], data can be filtered by rows and columns values very easily, using logical operators

