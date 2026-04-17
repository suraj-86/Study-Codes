import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("fruit.csv")
sns.histplot(data=df,x="Fruit_Type",y="Quantity_sold",hue="Shop",palette="rainbow",legend=True)

plt.xlabel("fruit")
plt.ylabel("quantity sold")
plt.show()