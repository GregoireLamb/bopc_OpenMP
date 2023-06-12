import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.path.join(os.getcwd(), 'output')
file = os.path.join(path, 'output5_2.dat')

# read the file as a dataframe
df = pd.read_csv(file, sep=',', header=None)
df.columns = ['n', 'p', 'time']

# group df by n and p and get the minimum time
df = df.groupby(['n', 'p']).min().reset_index()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(df[df['n'] == 80]['p'], df[df['n'] == 80]['time'])
ax2.plot(df[df['n'] == 1200]['p'], df[df['n'] == 1200]['time'])

fig.suptitle('Running time for exercise 5.2')
ax1.set_title('n = 80')
ax2.set_title('n = 1200')
ax1.set_xlabel('Number of cores')
ax2.set_xlabel('Number of cores')
ax1.set_ylabel('Running time (s)')
ax2.set_ylabel('Running time (s)')
plt.tight_layout()

plt.show()
