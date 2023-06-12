import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.path.join(os.getcwd(), 'output')
file = os.path.join(path, 'output6_1.dat')

# read the file as a dataframe
df = pd.read_csv(file, sep=',', header=None)
df.columns = ['size', 'p', 'r', 'time']

# group df by n and p and get the minimum time
df = df.groupby(['p']).min().reset_index()

plt.plot(df['p'], df['time'])

plt.suptitle('Running time for exercise 6.2')
# plt.set_xlabel('Number of cores')
# plt.set_ylabel('Running time (s)')
plt.tight_layout()

plt.show()
