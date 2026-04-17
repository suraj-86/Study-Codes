import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('iris.csv')
col=['sepal_length','sepal_width','petal_length','petal_width']
sns.heatmap(data=df[col],cmap="rainbow")
plt.show()


