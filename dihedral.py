import sys, math
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors 
from matplotlib.ticker import PercentFormatter 
from scipy.stats import norm
import matplotlib.mlab as mlab

# conversion from radians to degrees and vice versa
rad2deg = 180.0 / math.pi
deg2rad = 1.0 / rad2deg


acoor25 = []

with open('coor25.dat', 'r') as c:
    for l in c:
        l = l.strip().split()
        
        acoor25.append([float(l[0]), float(l[1]), float(l[2])])

acoor50 = []

with open('coor50.dat', 'r') as c:
    for l in c:
        l = l.strip().split()
        
        acoor50.append([float(l[0]), float(l[1]), float(l[2])])


i=0
coor50=[]
while i<len(acoor50):
  coor50.append(acoor50[i:i+100])
  i+=100

i=0
coor25=[]
while i<len(acoor25):
  coor25.append(acoor25[i:i+100])
  i+=100

# calculate the distance between beads 1 and 2

def g_r12(c1, c2):
    r2 = 0.0
    for p in range(3):
        r2 += (c2[p] - c1[p])**2
    r = math.sqrt(r2)
    return r

#unit vector between 2 3d coordinates

def g_u12(c1, c2):
    r12 = g_r12(c1, c2)
    u12 = [0.0 for p in range(3)]
    for p in range(3):
        u12[p] = (c2[p] - c1[p]) / r12
    return u12

# calculate dot product between two unit vectors
def g_udp(uvec1, uvec2):
    udp = 0.0
    for p in range(3):
        udp += uvec1[p] * uvec2[p]
    udp = max(min(udp, 1.0), -1.0)
    return udp


# calculate unit cross product between two unit vectors
def g_ucp(uvec1, uvec2):
    ucp = [0.0 for p in range(3)]
    cos_12 = g_udp(uvec1, uvec2)
    sin_12 = math.sqrt(1 - cos_12**2)
    ucp[0] = (uvec1[1]*uvec2[2] - uvec1[2]*uvec2[1]) / sin_12
    ucp[1] = (uvec1[2]*uvec2[0] - uvec1[0]*uvec2[2]) / sin_12
    ucp[2] = (uvec1[0]*uvec2[1] - uvec1[1]*uvec2[0]) / sin_12
    return ucp

# calculate angle between three 3-d cartesian coordinates
def g_a123(c1, c2, c3):
    u21 = g_u12(c2, c1)
    u23 = g_u12(c2, c3)
    dp2123 = g_udp(u21, u23)
    a123 = rad2deg * math.acos(dp2123)
    return a123


# calculate torsion angle between four 3-d cartesian coordinates
def g_t1234(c1, c2, c3, c4):
    u21 = g_u12(c2, c1)
    u23 = g_u12(c2, c3)
    u32 = g_u12(c3, c2)
    u34 = g_u12(c3, c4)
    u21c23 = g_ucp(u21, u23)
    u32c34 = g_ucp(u32, u34)
    dp = g_udp(u21c23, u32c34)
    sign = 2 * float(g_udp(u21c23, u34) < 0) - 1
    t1234 = rad2deg * sign * math.acos(dp)
    return t1234

d_ang1 = []

for i in range(0, len(coor25)):
    for j in range(0, 97):
        ang = (g_t1234(coor25[i][j], coor25[i][j+1], coor25[i][j+2], coor25[i][j+3]))
        d_ang1.append(ang)

d_ang2 = []

for i in range(0, len(coor50)):
    for j in range(0, 97):
        ang = (g_t1234(coor50[i][j], coor50[i][j+1], coor50[i][j+2], coor50[i][j+3]))
        d_ang2.append(ang)

#for i in range(0, (97*(101-3))):
#    if i%97 == 0:
#        print('skipping ', i)
#    else:
#        ang = ((g_t1234(acoor50[i], acoor50[i+1], acoor50[i+2], acoor50[i+3])))
#        d_ang2.append(ang)


def plot_his(x1, name):
    n_bins = 18
    #fig, ax = plt.subplots(1, 1, figsize =(10, 7), tight_layout = True)
    
    n, bins, patches = plt.hist(x1, bins = n_bins, facecolor='green')
    plt.xlabel('Diheral angle (degrees)')
    plt.ylabel('Frequency')
    plt.savefig('{}.png'.format(name))

plot_his(d_ang1, 'aij_25')

plot_his(d_ang2, 'aij_50')














