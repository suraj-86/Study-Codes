import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('students.csv')



gen=df["Gender"].value_counts()
plt.pie(gen)
plt.title("gender")
plt.show()
