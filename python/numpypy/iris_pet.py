import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
sns.lineplot(data=df,x="sepal_length",y="sepal_width",palette="coolwarm")

plt.title("sepal")
plt.xlabel("length")
plt.ylabel("width")
plt.show()
