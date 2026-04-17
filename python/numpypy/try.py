import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x=[20,45,70,83]
y=["Red Tape","Abross","Liberty","Killer"]
ex=[0.2,0.1,0.0,0.0]
plt.pie(x,labels=y,autopct="%0.1f%%",explode=ex,shadow=1)
plt.legend(loc=2)
plt.show()