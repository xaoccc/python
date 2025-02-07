import numpy as np
import pandas as pd

# Using pure python
my_data = [7, 10, 50, 234,  943]
zero_one_normalization = [(num - my_data[0]) / (my_data[-1] - my_data[0]) for num in my_data]
print(zero_one_normalization)

# Using numpy
# Convert the list to numpy.ndarray object
np_data = np.array(my_data)
normalized_np_data = (np_data - np_data.min()) / (np_data.max() - np_data.min())
# Convert it again to python list of float numbers
print(list(float(num) for num in normalized_np_data))

# Using pandas
# Convert the list to pandas Series object
data = pd.Series(my_data)
normalized_pandas_data = (data - data.min()) / (data.max() - data.min())
# Convert it again to python list of float numbers
print(list(float(num) for num in normalized_pandas_data))