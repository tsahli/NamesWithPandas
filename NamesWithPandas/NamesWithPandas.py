import pandas as pd
import matplotlib.pyplot as plt
import os

def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group

def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

years = range(1880, 2020)
pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)
names = names.groupby(['year', 'sex']).apply(add_prop)

total_births = names.pivot_table('births', index='year', columns='name', aggfunc=sum)
names_to_search = input('Enter names separated by spaces: ')
subset = total_births[names_to_search.split(' ')]
subset.plot(subplots=False, grid=True, figsize=(12, 10), title='Births per year')
plt.show()
