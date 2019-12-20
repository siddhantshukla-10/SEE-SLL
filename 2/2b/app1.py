import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

stud = pd.read_csv('StudentsPerformance.csv')

print(stud.head())

print(stud.info())
print(stud.describe())

stud1 = stud.drop(["lunch","test preparation course"],axis=1)
print(stud1.head())

stud["parental level of education"] = stud["parental level of education"].fillna("high school")

ax = sns.countplot(data=stud, x="gender", hue="test preparation course", palette="Set1")
ax.set(title="Number of male and female who took test preparation course vs those who did not", xlabel="gender", ylabel="total")
plt.show()







