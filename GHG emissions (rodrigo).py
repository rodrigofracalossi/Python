#import modules
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import seaborn as sns
from cycler import cycler


#import file and basic description of data
df = pd.read_excel("C:/Users/rodmo/Dropbox/00. Python/Climate change project/CO2_efficiency_complete, only values (long-term).xlsx")
df.head()
df.describe()
df.columns


#dropping observations from certain countries
df.drop(df[df['country'] == 'Saudi Arabia'].index, inplace = True)
df.drop(df[df['country'] == 'Mexico'].index, inplace = True)
df.drop(df[df['country'] == 'Australia'].index, inplace = True)
df.drop(df[df['country'] == 'Turkey'].index, inplace = True)
df.drop(df[df['country'] == 'Indonesia'].index, inplace = True)
df.drop(df[df['country'] == 'South Korea'].index, inplace = True)
df.drop(df[df['country'] == 'Argentina'].index, inplace = True)
df.drop(df[df['country'] == 'Italy'].index, inplace = True)
df.drop(df[df['country'] == 'Canada'].index, inplace = True)
df.drop(df[df['country'] == 'Japan'].index, inplace = True)
df.drop(df[df['country'] == 'France'].index, inplace = True)
df.drop(df[df['country'] == 'United Kingdom'].index, inplace = True)

df.drop(df[df['year'] < 1990].index, inplace = True)

#Graph, consumption-based emissions
default_cycler = (cycler(color=['forestgreen', 'red', 'black', 'darkgray', 'chocolate', 'y', 'dodgerblue']) +
                  cycler(linestyle=['--', '--', '--', '--', '--', '--', '--']))
markers_on1 = [1]
markers_on2 = [27]


fig, ax = plt.subplots(figsize=(12, 18))
for key, grp in df.groupby(['country']):
    ax.plot(grp['co2effic_consumption_mov_av2'], grp['gdppercapita'], lw=2, label=key,
            marker="o", markersize=8, markevery=markers_on2)
    ax.set_yscale('log')
    ax.set_xscale('log')
for key, grp in df.groupby(['country']):
    ax.plot(grp['co2effic_consumption_mov_av2'], grp['gdppercapita'], lw=2,
            marker="o", markersize=8, mfc='w', markevery=markers_on1)
    ax.set_yscale('log')
    ax.set_xscale('log')
plt.ylabel('GDP per capita, US$ 1,000', fontsize=14)
plt.xlabel('US$ million of GDP per ton of emitted CO2 (consumption-based)', fontsize=14)
plt.title('Efficiency of CO2 emissions (consumption-based) and GDP per capita: 1991-2017', fontsize=16)
fig.tight_layout()
plt.yticks([1500, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000],[1.5, 2, 3, 5, 10, 20, 30, 40, 50, 60])
plt.xticks([1,1.5, 2, 3, 4, 5, 6, 7],[1,1.5, 2, 3, 4, 5, 6, 7])
plt.rc('axes', prop_cycle=default_cycler)
lines = ax.get_lines()
legend1 = plt.legend([lines[i] for i in [0,1,3,4,5,2,6]], ['Brazil', 'China', 'India', 'Russia', 'South Africa', 'Germany','United States'], loc=1)
legend2 = plt.legend([lines[i] for i in [2,9]], ["2017", "1991"], loc=4)
ax.add_artist(legend1)
ax.add_artist(legend2)
plt.show()


