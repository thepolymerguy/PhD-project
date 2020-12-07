import os
import sys
import csv
import glob
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean

plt.style.use('ggplot')

def rg(paths):
    for i in paths:
        y = []
        with open (i, 'r') as ww:
            c = 0
            for ll in ww:
                c = c + 1
                ll = ll.strip().split()
                #ll = [float(k) for k in ll]                
                y.append(np.sqrt(float(ll[0])))
        return y

def rh(paths):
    for i in paths:
        y = []
        with open (i, 'r') as ww:
            c = 0
            for ll in ww:
                c = c + 1
                ll = ll.strip().split()
                #ll = [float(k) for k in ll]                
                y.append(float(ll[0]))
        return y


def plot_his2(yv, name, fc, l, delt, xl, yl):

    fig, ax = plt.subplots(1, 1, figsize =(7, 5), tight_layout = True)
    
    for i in range(len(yv)):

        dif = max(yv[i]) - min(yv[i])
        nb = dif/delt
        n_bins = int(nb)
        
        n, bins, patches = ax.hist(yv[i], bins = n_bins, facecolor=fc[i], alpha=0.8, zorder=3, label=l[i])

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

    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    legend = ax.legend(bbox_to_anchor=(1,1),loc=1, framealpha=0)
    plt.savefig('{}.png'.format(name), transparent=True, dpi=300)

#paths = glob.glob('./*lin_ext_ABA_ts_250000.dat*')
#ll = rg(paths)

#print(min(ll), max(ll))



print('Number of graphs?')
mm = int(input())

for pp in range(0, mm):
    
    print('Title of graph ', pp , ' : ')    
    fn = str(input())
    print('X axis ')    
    xa = str(input())
    
    print('Y axis ')    
    ya = str(input())

    print('Number of plots on one graph?:')

    n = int(input())

    gl = []
    leg = []
    col = []
    for i in range(0, n):
        print(' String pls: ')
        l = str(input())
        paths = glob.glob(l)
        g = rg(paths)
        gl.append(g)

        print('Legend: ')
        ll = str(input())
        leg.append(ll)

        print('Colour: ')
        cc = str(input())
        col.append(cc)

#['#34699a', '#194769']
    #function to plot graph 
    plot_his2(gl, fn, col, leg, 0.5, xa, ya)


