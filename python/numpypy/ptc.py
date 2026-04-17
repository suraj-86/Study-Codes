import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('indian population new.csv')
sns.lineplot(data=df,x="Year",y="% Increase in Population",palette="rainbow")

plt.xlim(2000,2020)
plt.title("population growth")
plt.xlabel("year")
plt.ylabel("population growth percent")
plt.show()
