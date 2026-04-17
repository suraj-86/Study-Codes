import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('tips.csv')
sns.barplot(data=df,y="time",x="sex",palette="rainbow")

plt.title("time sex ratio")
plt.ylabel("time")
plt.xlabel("sex")
plt.show()
