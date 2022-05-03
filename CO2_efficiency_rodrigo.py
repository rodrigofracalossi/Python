#import modules
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

#import file and basic description of data
df = pd.read_excel("C:/Users/rodmo/Dropbox/00. Python/Climate change project/CO2_efficiency.xlsx")
df.head()
df.describe()

#general scatter plot
df.plot('co2efficiency', 'gdppercapita', kind='scatter')
    plt.show()

#1. com legendas por paìs
fig, ax = plt.subplots(figsize=(9, 9))
for key, grp in df.groupby(['country']):
    ax.plot(grp['co2efficiency'], grp['gdppercapita'], label=key,
            marker=".", linestyle='--')
    ax.set_yscale('log')
plt.ylabel('GDP per capita (US$)')
plt.xlabel('CO2 efficiency (tons of CO2 per US$ 1 million GDP)')
plt.title('CO2 Efficiency: 1960-2016')
fig.legend(loc=7)
fig.tight_layout()
fig.subplots_adjust(right=0.85)
plt.show()

#2. plot by country (same plot)
fig, ax = plt.subplots()
df.groupby('country').plot(x='co2efficiency', y='gdppercapita', ax=ax, legend=False)
plt.ylabel('GDP per capita (US$)')
plt.xlabel('CO2 efficiency (tons of CO2 per US$ 1 million GDP)')
plt.title('CO2 Efficiency: 1960-2016')
ax.set_yscale('log')
fig.legend(loc=7)
fig.tight_layout()
fig.subplots_adjust(right=0.88)

