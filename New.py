import plotly.offline as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
py.init_notebook_mode()

laser_cols=['NIS']
with open('ProjectUKF/laser_nis.txt') as f:
    df = pd.read_table(f, sep='\t', header=None, names=laser_cols, lineterminator='\n')

x = np.arange(len(df)+1)
y = np.arange(len(df)+1)

for i in range(len(x) - 1):
    y[i] = df['NIS'][i]

df.plot()
plt.xlabel('Measurement Index')
plt.title('Laser')
plt.axhline( y=5.99
        , color='r'
        , linestyle='-'
        , label='95% confidence')
plt.legend( prop={'size':20} )
plt.show()

radar_cols=['NIS']
with open('ProjectUKF/radar_nis.txt') as f:
    df = pd.read_table(f, sep='\t', header=None, names=radar_cols, lineterminator='\n')

x = np.arange(len(df)+1)
y = np.arange(len(df)+1)

for i in range(len(x) - 1):
    y[i] = df['NIS'][i]

df.plot()
plt.xlabel('Measurement Index')
plt.title('Radar')
plt.axhline( y=7.815
        , color='r'
        , linestyle='-'
        , label='95% confidence')
plt.legend( prop={'size':20} )
plt.show()