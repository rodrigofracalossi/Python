#import modules
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import openpyxl

#import file and basic description of data
df = pd.read_excel("C:/Users/rodmo/Dropbox/00. Python/Climate change project/CO2_efficiency.xlsx")
df.head()
df.describe()

#general scatter plot
df.plot('co2efficiency', 'gdppercapita', kind='scatter')
    plt.show()

#line plot with selected countries
df.plot('co2efficiency', 'gdppercapita', kind='line')
    plt.ylabel('GDP per capita (US$)')
    plt.xlabel('CO2 efficiency (tons of CO2 per US$ 1 million GDP)')
    plt.title('CO2 Efficiency: 1960-2016')
    plt.show()

#plot by country (different plots)
df.groupby('country').plot(x='co2efficiency', y='gdppercapita', kind='line')

#plot by country (same plot)
fig, ax = plt.subplots()
df.groupby('country').plot(x='co2efficiency', y='gdppercapita', ax=ax, legend=False)
ax.set_yscale('log')
fig.legend(loc=7)
fig.tight_layout()
fig.subplots_adjust(right=0.88)

#com legendas por paìs
fig, ax = plt.subplots(figsize=(10, 10))
for key, grp in df.groupby(['country']):
    ax.plot(grp['co2efficiency'], grp['gdppercapita'], label=key)
ax.set_yscale('log')
fig.legend(loc=7)
fig.tight_layout()
fig.subplots_adjust(right=0.9)
plt.show()

#same figure, different subplots
grouped = df.groupby('country')
ncols=2
nrows = int(np.ceil(grouped.ngroups/ncols))
fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12,4), sharey=True)
for (key, ax) in zip(grouped.groups.keys(), axes.flatten()):
    grouped.get_group(key).plot(ax=ax)
ax.legend()
plt.show()

#o mesmo com loop
for i in df:
    fil = df[(df['country']==i)]
    fig, ax = plt.subplots
    fil.groupby('country').plot(x=['co2efficiency'],y = ['gdppercapita'],ax=ax, title = str(i))
    plt.legend(fil.country)
    plt.show()

#inspirado no modelo do curso
def plot_shinfrin(table):
    for each in table['Country'].unique():
        tab = table[table['Country'] == each]
        tab = tab.sort_values('year')
        plt.plot(tab['year'], tab['gdppercapita'], label=each)
        plt.text(tab.reset_index(drop=True).loc[len(tab) - 2]['year'],
                 tab.reset_index(drop=True).loc[len(tab) - 2]['gdppercapita'], each)
    # plt.legend(frameon=False)
    plt.show()

#github
echo "# Python" >> readme.md
git init
git add readme.md

git pull
git remote add origin
git@github.com:

git push -u origin master