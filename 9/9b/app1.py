import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

black = pd.read_csv('blackfri.csv')

black.head()
black.info()
black.describe()

black["City_Category"] = black["City_Category"].fillna("A")

black["City_Category"] = black["City_Category"].map({
  "A":"Metro Cities",
  "B":"Small Towns",
  "C":"Villages"
})

print(black.head())

ax = sns.countplot(data=black, x="City_Category", hue="Gender", palette="Set1")
ax.set(title="City Category vs Gender",xlabel="City_Category", ylabel="Total")
plt.show()
