import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Using pure python
my_data = [7, 10, 50, 234,  943]
zero_one_normalization = [(num - my_data[0]) / (my_data[-1] - my_data[0]) for num in my_data]
print(zero_one_normalization)

# Using numpy
# Convert the list to numpy.ndarray object
np_data = np.array(my_data)
zero_one_normalized_np_data = (np_data - np_data.min()) / (np_data.max() - np_data.min())
# Convert it again to python list of float numbers
print(list(float(num) for num in zero_one_normalized_np_data))

# Using pandas
# Convert the list to pandas Series object
data = pd.Series(my_data)
zero_one_normalized_pandas_data = (data - data.min()) / (data.max() - data.min())
# Convert it again to python list of float numbers
print(list(float(num) for num in zero_one_normalized_pandas_data), f'\n{"-"*150}')

# Load dataset from seaborn
dataset = sns.load_dataset('geyser')

# Create mean corrected (mc) data (the mean becomes zero) columns in this dataset
dataset['duration_mc'] = dataset['duration'] - dataset['duration'].mean()
dataset['waiting_mc'] = dataset['waiting'] - dataset['waiting'].mean()
print(dataset, f'\n{"-"*150}')

# Create normalized data columns in this dataset
# We use Z-normalization: transform the data so that the resulting values have a mean of 0 and a standard deviation of 1
dataset['duration_norm1'] = (dataset['duration'] - dataset['duration'].mean()) / dataset['duration'].std()
dataset['waiting_norm1'] = (dataset['waiting'] - dataset['waiting'].mean()) / dataset['waiting'].std()
print(dataset, f'\n{"-"*150}')

# With Min-Max Normalization (0-1 unity based normalization):
dataset['duration_norm2'] = (dataset['duration'] - dataset['duration'].min()) / (dataset['duration'].max() - dataset['duration'].min())
dataset['waiting_norm2'] = (dataset['waiting'] - dataset['waiting'].min()) / (dataset['waiting'].max() - dataset['waiting'].min())
print(dataset, f'\n{"-"*150}')

# Show the graphical display of the data in four graphs
fig, ((orig, mc), (Z_norm, zero_one)) = plt.subplots(2, 2)
dataset.plot('duration', 'waiting', kind='scatter', ax=orig, color='purple', linewidth=0, marker='h')
dataset.plot('duration_mc', 'waiting_mc', kind='scatter', ax=mc, color='blue', linewidth=0, marker='h')
dataset.plot('duration_norm1', 'waiting_norm1', kind='scatter', ax=Z_norm, color='green', linewidth=0, marker='h')
dataset.plot('duration_norm2', 'waiting_norm2', kind='scatter', ax=zero_one, color='red', linewidth=0, marker='h')
plt.show()