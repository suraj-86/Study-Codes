import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('tips')

sns.displot(df['tip'])
plt.show()