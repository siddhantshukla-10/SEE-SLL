import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

tit = pd.read_csv('train.csv')

tit.head()

tit.info()
tit.describe()

tit1 = tit.drop(["SibSp","Parch"],axis=1)

tit["Embarked"] = tit["Embarked"].fillna("S")

ax = sns.countplot(data=tit, x="Pclass", hue="Survived", palette="Set1")
ax.set(title="Pclass vs Survived", xlabel="Pclass", ylabel="Total")
plt.show()