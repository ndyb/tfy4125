# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

xnv = np.genfromtxt('data/xnonvacuum.txt', delimiter='\t')[558:]
tnv = np.genfromtxt('data/tnonvacuum.txt', delimiter='\t')[558:]
tnv = tnv - tnv[0]
vnv = (xnv[1:]-xnv[:-1]) / (tnv[1:]-tnv[:-1])
pnvk = np.polyfit(tnv[:-1],vnv,2)
pnv = lambda t: pnvk[0]*t**2 + pnvk[1]*t + pnvk[2]

xv = np.genfromtxt('data/xvacuum.txt', delimiter='\t')[613:]
tv = np.genfromtxt('data/tvacuum.txt', delimiter='\t')[613:]
tv = tv - tv[0]
vv =(xv[1:]-xv[:-1]) / (tv[1:]-tv[:-1])
pvk = np.polyfit(tv[:-1],vv,2)
pv = lambda t: pvk[0]*t**2 + pvk[1]*t + pvk[2]

nvfig = plt.figure()
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon / Hastighet')
plt.title('Non-vacuum')
plt.grid(True)
plt.plot(tnv, xnv, label='Posisjon')
plt.plot(tnv[:-1], vnv, label='Hastighet')
plt.plot(tnv, pnv(tnv), label='Hastighet ' + '(' + str(round(pvk[0],1)) + 't^2 + ' + str(round(pvk[1],1)) + 't + ' + str(round(pvk[2],1)) + ')')
plt.legend(loc='best')
plt.show()
nvfig.savefig('oppg_4_1.png')

vfig = plt.figure()
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon / Hastighet')
plt.title('Vacuum')
plt.grid(True)
plt.plot(tv, xv, label='Posisjon')
plt.plot(tv[:-1], vv, label='Hastighet')
plt.plot(tv, pv(tv), label='Hastighet ' + '(' + str(round(pnvk[0],1)) + 't^2 + ' + str(round(pnvk[1],1)) + 't + ' + str(round(pnvk[2],1)) + ')')
plt.legend(loc='upper left')
plt.show()
vfig.savefig('oppg_4_2.png')
