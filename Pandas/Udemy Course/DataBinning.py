# Some Seaborn functions raise Pandas 3 future warnings, but there is a way to hide them
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

geyser = sns.load_dataset('geyser')
pd.set_option('display.max_rows', None)


# Use a simple histogram to show the distribution of variables
sns.histplot(data=geyser, x='duration', bins=100, hue='kind', palette="coolwarm", edgecolor='white', binwidth=2)

sns.histplot(data=geyser, x='waiting', bins=100, hue='kind', palette="coolwarm", edgecolor='white', binwidth=2)
# plt.show()

# Use Pandas quantile cut binning algorithm to define a new set of binnings with the qcut() function

geyser['qcut_dur_2'] = pd.qcut(geyser.duration, q=2, labels=['short', 'long'])
geyser['qcut_dur_3'] = pd.qcut(geyser.duration, q=3, labels=['short', 'medium', 'long'])
print(geyser)


fig, ((h_dur, qc_dur2, qc_dur3), (h_dur2, cut2, cut3), (h_dur3, sel_cut2, sel_cut3)) = plt.subplots(3, 3)
sns.histplot(data=geyser, x='duration', bins=25, ax=h_dur, hue='kind', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=qc_dur2, hue='qcut_dur_2', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=qc_dur3, hue='qcut_dur_3', palette="coolwarm", edgecolor='white')

geyser['cut_dur_2'] = pd.cut(geyser.duration, bins=2, labels=['short', 'long'])
geyser['cut_dur_3'] = pd.cut(geyser.duration, bins=3, labels=['short', 'medium', 'long'])

sns.histplot(data=geyser, x='duration', bins=25, ax=h_dur2, hue='kind', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=cut2, hue='cut_dur_2', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=cut3, hue='cut_dur_3', palette="coolwarm", edgecolor='white')


# Define custom binnings range
geyser['sel_cut_dur_2'] = pd.cut(geyser.duration, bins=[0, 2, 100], labels=['short', 'long'])
geyser['sel_cut_dur_3'] = pd.cut(geyser.duration, bins=[0, 2, 4, 100], labels=['short', 'medium', 'long'])

sns.histplot(data=geyser, x='duration', bins=25, ax=h_dur3, hue='kind', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=sel_cut2, hue='sel_cut_dur_2', palette="coolwarm", edgecolor='white')
sns.histplot(data=geyser, x='duration', bins=25, ax=sel_cut3, hue='sel_cut_dur_3', palette="coolwarm", edgecolor='white')

plt.show()

# This can be used in image recognition
# bins can be defined easily using prediction models, so the bins distribution data can be authomatically filled in