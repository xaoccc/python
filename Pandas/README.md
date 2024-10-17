## Pandas notes
### Data Types

##### Creating a DataFrame:
- pd.DataFrame(list or dict) - converts python list to data frame (table)
- df = pd.DataFrame(list, columns=['student_id', 'age']) - gives names to the columns
- df = pd.DataFrame(list, index=['mon', 'tue', 'wen']) - gives names(custom indexes) to the rows

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

### Export 
`df.to_csv()` - converts df to csv
`df.to_json()` - converts df to json

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

### Merge Data
`pd.concat([df1, df2])` - merges two data frames. By default, it merges by rows. If axis=1 is given, it merges by columns
`df1.merge(df2, on='employee_id')` - merges two data frames by a common column. Identical to SQL join.

### Group Data
`df.groupby('column_name')` - groups data by a column. For example, we have a column 'age' and we want to group data by age values.

### Rename Columns
`df.rename(columns={'old_name': 'new_name'})` - renames a column. If inplace=True is given, it updates the existing df

### Round and Format Data
`df['column_name'].round(2)` - rounds all data to 2 decimal points
`df['column_name'].round({column_56: 2})` - formats the data of column_56 to 2 decimal points
`df.map('{:.Nf}'.format)` - formats all data to N decimal points
`df['column_56'] = df['column_56'].map('{:.Nf}'.format)` - formats the data of column_56 to N decimal points