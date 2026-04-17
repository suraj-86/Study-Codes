import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('SMART_Bus_Stops.csv')
sns.scatterplot(data=df,x="stop_lon",y="stop_lat",hue="stop_id",palette="coolwarm",legend=False)

plt.title("bus stop density")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.show()
