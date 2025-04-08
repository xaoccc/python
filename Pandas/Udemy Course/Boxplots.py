import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model

# Using boxplot, boxenplot, violinplot, swarmplot, catplot, scatterplot
iris = sns.load_dataset("iris")
sns.catplot(data=iris, x="species", y="sepal_length", hue="species", dodge=False, width=0.4)

# Scatterplot
ax = iris.plot.scatter(x="sepal_length", y="sepal_width", c="blue", s=10, alpha=0.5)
ax.set_title("Iris Sepal Length vs Width")
ax.set_xlabel("Sepal Length")
ax.set_ylabel("Sepal Width")
plt.show()