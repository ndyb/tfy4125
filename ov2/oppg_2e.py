# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

Nmax = 200

f = lambda n: (n-1.0)/(n+1.0)
x = range(Nmax)
y = [f(i) for i in x]

fig = plt.figure()
plt.xlabel('n')
plt.axis([-2, Nmax, -1, 1.2])
plt.grid(True)
plt.plot(x, y)
plt.show()
fig.savefig('oppg_2e.png')
