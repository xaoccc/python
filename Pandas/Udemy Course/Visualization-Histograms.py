import warnings
warnings.filterwarnings('ignore', 'use_inf_as_na')

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

geyser = sns.load_dataset('iris')
pd.set_option('display.max_rows', None)

print(geyser)
# For one column
hist = geyser['sepal_length'].hist(bins=20)
hist.set_title('Graph')
hist.set_xlabel('Duration')
hist.set_ylabel('Occurence')
# Using Seaborn:
sns.histplot(data=geyser, x='sepal_length', bins=20)

# Whole DataFrame
hist1 = geyser.hist(bins=20)

# Advanced histogram for one column
fig, ax = plt.subplots()
colors = {'setosa': 'Red', 'versicolor': 'Blue', 'virginica': 'Orange'}

for Species, data in geyser.groupby('species'):
    data.plot(kind='hist', ax=ax, column='sepal_length', bins=30, alpha=0.5, color=colors[Species])

ax.set_title('Iris Sepal Length')
ax.set_xlabel('Sepal Length')
ax.legend(colors.keys())


# Using Seaborn:
sns.histplot(data=geyser, x='sepal_length', bins=20, hue='species')

# 2D diagram:
ax.set_ylabel('Sepal Width')
sns.histplot(data=geyser, x='sepal_length', y='sepal_width', bins=20, hue='species')

plt.show()

