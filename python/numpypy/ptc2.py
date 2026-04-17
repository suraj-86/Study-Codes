import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
sns.scatterplot(data=df,x="sepal_length",y="petal_length")


plt.title("sepal-petal")
plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.show()
