import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

iri = pd.read_csv('iris.csv')

iri.head()
iri.info()
iri.describe()

iri.drop(["Sepal_Length"],inplace=True,axis=1)

ndf = iri[['Class','Petal_Width']]
print(ndf.groupby(['Class'], as_index=False).mean())

plt.figure(figsize=[12,6])
ax = sns.countplot(data=iri, x="Sepal_Width", hue="Class", palette="Set1")
ax.set(title="Sepal Width against Class", xlabel="Sepal_Width", ylabel="Total")
plt.tight_layout()
plt.show()

