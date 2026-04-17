import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ageincome.csv')
sns.scatterplot(data=df,x="age",y="income",hue="gender",palette="rainbow",legend=False)

plt.title("age-income")
plt.xlabel("age")
plt.ylabel("income")
plt.show()

