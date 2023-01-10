import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.tsv', sep='\t')
sns.heatmap(data, x='sample1', y='sample2', cmap='YlGnBu')
plt.show()
