import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('students.csv')

sns.barplot(data=df,x="Stream",y="Marks",estimator="mean",palette="viridis")
#plt.bar(data=df,x="Name",height="Marks")
plt.ylabel("avg marks")
plt.title("marks")
plt.show()
