import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("fruit.csv")
plt.pie(x="Quantity_sold",labels="Fruit_Type",)


plt.show()
