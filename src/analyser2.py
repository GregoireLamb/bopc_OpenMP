import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.path.join(os.getcwd(), 'output')
file_names=["output5_static.dat", "output5_static1.dat", "output5_dynamic1.dat", "output5_guided10.dat"]
files = [os.path.join(path, name) for name in file_names]


df = pd.DataFrame()

for file in files:
    temp_df = pd.read_csv(file, sep=',', header=None)
    temp_df['strategy'] = str(file).removeprefix(path).removeprefix('\\output5_').removesuffix('.dat')
    df = df.append(temp_df, ignore_index=True)

df.columns = ['n', 'p', 'time', 'strategy']

# # group df by n and p and get the minimum time
df = df.groupby(['strategy']).min().reset_index()

# plot the time against the strategy 
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="strategy", y="time", data=df)
ax.set(xlabel='Strategy', ylabel='Running time (s)')
ax.set_title('Running time for exercise 5.3')
plt.show()

