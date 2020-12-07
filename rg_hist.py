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

#path1 = glob.glob('./*all_rg_N_301_lin_a_25*')
#his_lin25 = rg(path1)
#path2 = glob.glob('./*all_rg_N_301_star_a_25*')
#his_star25 = rg(path2)
path3 = glob.glob('./*all_rg_N_301_lin_a_50*')
his_lin50 = rg(path3)
#path4 = glob.glob('./*all_rg_N_301_star_a_50*')
#his_star50 = rg(path4)
#path5 = glob.glob('./*all_rg_N_151_lin_a_25*')
#his_151lin25 = rg(path5)
#path6 = glob.glob('./*all_rg_N_151_lin_a_50*')
#his_151lin50 = rg(path6)
#path7 = glob.glob('./*all_rg_N_151_star_a_25*')
#his_151star25 = rg(path7)
#path8 = glob.glob('./*all_rg_N_151_star_a_50*')
#his_151star50 = rg(path8)
#path9 = glob.glob('./*all_rg_N_301_lin_aba*')
#path10 = glob.glob('./*all_rg_N_301_lin_bab*')
#
#aba = rg(path9)
#bab = rg(path10)
#
#p11 = glob.glob('./*rh_N_301_lin_a_25*')
#p12 = glob.glob('./*rh_N_301_lin_a_50*')
#p13 = glob.glob('./*rh_N_301_star_a_25*')
#p14 = glob.glob('./*rh_N_301_star_a_50*')
#
#rhlin25 = rh(p11)
#rhlin50 = rh(p12)
#rhstar25 = rh(p13)
#rhstar50 = rh(p14)
#
#p15 = glob.glob('./*rh_N_301_lin_aba*')
#p16 = glob.glob('./*rh_N_301_lin_bab*')
#
#rhaba = rh(p15)
#rhbab = rh(p16)
#
#p18 = glob.glob('./*lin_aij_50_ts_15000*')
#p20 = glob.glob('./*lin_aij_50_ts_130000*')
#
#ts15000 = rg(p18)
#ts130000 = rg(p20)
#
#p21 = glob.glob('./*lin_aij_25_ts_15000*')
#p22 = glob.glob('./*lin_aij_25_ts_130000*')

#p23 = glob.glob('./*lin_aij_50_ts_200000*')

#ts200000 = rg(p23)
#print(ts200000)

p29 = glob.glob('./*all_rg_N_301_lin_a_100*')
a100 = rg(p29)

def plot_his2(yv, name, fc, l, nbin, xl):
    n_bins = nbin
    fig, ax = plt.subplots(1, 1, figsize =(7, 5), tight_layout = True)
    
    
    for i in range(len(yv)):
        w = np.ones_like(yv[i])/len(yv[i])
        n, bins, patches = ax.hist(yv[i], bins = n_bins, weights = w, facecolor=fc[i], alpha=0.8, zorder=3, label=l[i])

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
    ax.set_ylabel('Probability')
    legend = ax.legend(bbox_to_anchor=(1,1),loc=1, framealpha=0)
    plt.savefig('{}.png'.format(name), transparent=True, dpi=300)


#yv = [his_lin50, his_star50, aba, bab]
fc = ['#0f4c75', '#3282b8', '#878ecd', '#b9bbdf']
l = ['Linear - aij = 50', 'Star - aij = 50','Linear - ABA', 'Linear - BAB']

#plot_his2(yv, 'RG_dist_whatdoitbedoe', fc, l, 10, 'Radius of Gyration')


#plot_his2([his_lin25, his_star25], 'RG_dist_25_N_301', ['#34699a','#194769'], ['Linear', 'Star'], 10, 'Radius of Gyration')
#plot_his2([his_lin50, his_star50], 'RG_dist_50_N_301', ['#34699a','#194769'], ['Linear', 'Star'], 10, 'Radius of Gyration')

#plot_his2([rhlin25, rhstar25], 'RH_dist_25', ['#34699a','#194769'], ['Linear', 'Star'], 10, 'Hydrodynamic Radius')
#plot_his2([rhlin50, rhstar50], 'RH_dist_50', ['#34699a','#194769'], ['Linear', 'Star'], 8, 'Hydrodynamic Radius')

#plot_his2([aba, bab], 'RG_dist_AB', ['#34699a','#194769'], ['ABA', 'BAB'], 10, 'Radius of Gyration')
#plot_his2([rhaba, rhbab], 'RH_dist_AB', ['#34699a','#194769'], ['ABA', 'BAB'], 10, 'Hydrodynamic Radius')

#plot_his2([ts15000], 'RG_ts_15000_lin_aij_50', ['#194769'], ['Timestep = 15,000'], 8, 'Radius of Gyration')
#plot_his2([ts130000], 'RG_ts_130000_lin_aij_50', ['#194769'], ['Timestep = 130,000'], 8, 'Radius of Gyration')

#plot_his2([ts15000_1], 'RG_ts_15000_lin_aij_25', ['#194769'], ['Timestep = 15,000'], 8, 'Radius of Gyration')
#plot_his2([ts130000_1], 'RG_ts_130000_lin_aij_25', ['#194769'], ['Timestep = 130,000'], 8, 'Radius of Gyration')

#plot_his2([ts200000], 'RG_ts_250000_lin_aij_50', ['#194769'], ['Timestep = 250,000'], 8, 'Radius of Gyration')
plot_his2([his_lin50, a100], 'RG_ps', ['#34699a', '#194769'], ['aij = 50','aij = 100'], 10, 'Radius of Gyration')
