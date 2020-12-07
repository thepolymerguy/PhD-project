import os
import sys
import csv
import glob
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean


mol = []
nei = []
with open ('/home/amran/PHD/AIJ_ana/N_301_arch_aij/AB_agg/L_30_N_100_neigh.dat', 'r') as nl:
    for l in nl:
        l = l.strip().split()
        mol.append(l[0])
        nei.append(l[1])

#print(mol, nei)

smol = set(mol) #to get rid of dupes
umol = list(smol) #to make list again

cneigh = {}

only1 = []
only2 = []
only3 = []
more3 = []

dislens = []

for j in umol:
    neil = []
    for i in range(0,len(mol)):
        if j == mol[i]:
            neil.append(nei[i])
    neil = list(set(neil))
    if len(neil) == 1:
        only1.append(j)
        print('Neighbor: ', j, ' is: ', neil)
    if len(neil) == 2:
        only2.append(j)
    if len(neil) == 3:
        only3.append(j)
    if len(neil) > 3:
        more3.append(j)
        print('Neighbor: ', j, ' is: ', neil)
    cneigh[j] = neil
    dislens.append(len(neil))

#print('Neighbor 41: ', cneigh['41'])
#print('Neighbor 25: ', cneigh['25'])
#print('Neighbor 40: ', cneigh['40'])
#print('Neighbor 24: ', cneigh['24'])


print('Number of polymers with 1 or more neighbors = ', len(umol))
print('Number of polymers with only 1 is = ', len(only1))
print('Number of polymers with only 2 is = ', len(only2))
print('Number of polymers with only 3 is = ', len(only3))
print('Number of polymers with more than 3 = ', len(more3))


'''
fig, ax = plt.subplots(1, 1, figsize =(7, 5), tight_layout = True)
n, bins, patches = ax.hist(dislens, bins = 4, facecolor='#d5a4cf', alpha=0.8, zorder=3, label='Number of neighbours')

plt.grid(b=True, which='major', color='#666666', linestyle='--')

plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.2)

ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['left'].set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')
ax.yaxis.label.set_color('black')
ax.xaxis.label.set_color('black')

ax.set_xlabel('Neighbours')
ax.set_ylabel('Count')
legend = ax.legend(bbox_to_anchor=(1,1),loc=1, framealpha=0)
#plt.savefig('{}.png'.format(name), transparent=True, dpi=300)
plt.show()
'''
