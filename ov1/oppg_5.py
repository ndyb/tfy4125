# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

xnv = np.genfromtxt('data/xnonvacuum.txt', delimiter='\t')
tnv = np.genfromtxt('data/tnonvacuum.txt', delimiter='\t')
vnv =(xnv[1:]-xnv[:-1]) / (tnv[1:]-tnv[:-1])

xv = np.genfromtxt('data/xvacuum.txt', delimiter='\t')
tv = np.genfromtxt('data/tvacuum.txt', delimiter='\t')
vv =(xv[1:]-xv[:-1]) / (tv[1:]-tv[:-1])

nvfig = plt.figure()
plt.axis([0.3, 0.6, -0.5, 1.5])
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon / Hastighet')
plt.title('Non-vacuum')
plt.grid(True)
plt.plot(tnv, xnv, label='Posisjon')
plt.plot(tnv[:-1], vnv, label='Hastighet')
plt.legend(loc='upper left')
plt.show()
nvfig.savefig('oppg_5_1.png')

vfig = plt.figure()
plt.axis([0.4, 0.7, -0.5, 2.5])
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon / Hastighet')
plt.title('Vacuum')
plt.grid(True)
plt.plot(tv, xv, label='Posisjon')
plt.plot(tv[:-1], vv, label='Hastighet')
plt.legend(loc='upper left')
plt.show()
vfig.savefig('oppg_5_2.png')
