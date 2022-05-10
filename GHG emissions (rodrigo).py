# import modules
import matplotlib.pyplot as plt
import pandas as pd
from cycler import cycler

# Graph, consumption-based emissions
default_cycler = (cycler(color=['forestgreen', 'red', 'black', 'darkgray', 'chocolate', 'y', 'dodgerblue']) +
                  cycler(linestyle=['--', '--', '--', '--', '--', '--', '--']))
markers_on1 = [1]
markers_on2 = [27]


def plot(df, col1='co2effic_consumption_mov_av2', col2='gdppercapita'):
    fig, ax = plt.subplots(figsize=(7, 9))
    for m, fz in zip([[1], [27]], ['w', None]):
        for key, grp in df.groupby(['country']):
            ax.plot(grp[col1], grp[col2], lw=2, label=key,
                    marker="o", markersize=8, markevery=m, mfc=fz)
            ax.set_yscale('log')
            ax.set_xscale('log')
    plt.ylabel('GDP per capita, US$ 1,000', fontsize=14)
    plt.xlabel('US$ million of GDP per ton of emitted CO2 (consumption-based)', fontsize=14)
    plt.title('Efficiency of CO2 emissions (consumption-based) and GDP per capita: 1991-2017', fontsize=16)
    fig.tight_layout()
    plt.yticks([1500, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000],
               [1.5, 2, 3, 5, 10, 20, 30, 40, 50, 60])
    plt.xticks([1, 1.5, 2, 3, 4, 5, 6, 7], [1, 1.5, 2, 3, 4, 5, 6, 7])
    plt.rc('axes', prop_cycle=default_cycler)
    lines = ax.get_lines()
    legend1 = plt.legend([lines[i] for i in [0, 1, 3, 4, 5, 2, 6]],
                         ['Brazil', 'China', 'India', 'Russia', 'South Africa', 'Germany', 'United States'],
                         loc=1, frameon=False)
    legend2 = plt.legend([lines[i] for i in [2, 9]], ["1991", "2017"], loc=4, frameon=False)
    ax.add_artist(legend1)
    ax.add_artist(legend2)

    plt.savefig('minha_primeira_figura.svg', format='svg', dpi=200)
    plt.show()


if __name__ == '__main__':
    d = pd.read_excel("co2_efficiency.xlsx")
    # import file and basic description of data
    # d.head()
    # d.describe()
    # d.columns

    # DRY: don't repeat yourself
    # dropping observations from certain countries

    countries_to_remove = ['Saudi Arabia', 'Mexico', 'Australia', 'Turkey',
                           'Indonesia', 'South Korea', 'Argentina', 'Italy',
                           'Canada', 'Japan', 'France', 'United Kingdom']

    countries_to_include = ['Brazil', 'United States', 'China']
    # for country in d.country.unique():
    #     if country not in countries_to_include:
    #         d.drop(d[d['country'] == country].index, inplace=True)

    for country in countries_to_remove:
        d.drop(d[d['country'] == country].index, inplace=True)

    d.drop(d[d['year'] < 1990].index, inplace=True)
    plot(d)
