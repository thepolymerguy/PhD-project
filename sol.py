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


def sol():
    lall = []
    for i in paths:
        x = []
        y = []
        with open (i, 'r') as ww:
            for ll in ww:
                ll = ll.strip().split()
                ll = [float(k) for k in ll]
                #ll = float(ll)
                wid = set(ll)
                wid = list(wid)
                wid.remove(0)
                print(wid)
    #print(lall)
    avm = [float(sum(col))/len(col) for col in zip(*lall)]

paths = glob.glob('./*count*')
sol()
