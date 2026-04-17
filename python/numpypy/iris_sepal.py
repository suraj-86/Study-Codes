import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('iris.csv')
sns.swarmplot(x="sepal_width",y="species",data=df,palette="rocket")
sns.violinplot(x="sepal_width",y="species",data=df,palette="coolwarm",fill=True)

plt.title("sepal")
plt.xlabel("Width")
plt.ylabel("species")
plt.show()
