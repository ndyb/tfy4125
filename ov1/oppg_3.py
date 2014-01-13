# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

Tmin = 0
Tmax = 5
At = 4.0

x = range(Tmax+1)

st = lambda t: (At*(t**2))/2
sp = lambda t: (8.0*t)-8


fig = plt.figure()
plt.axis([Tmin, Tmax, 0, 25])
plt.xlabel('Tid (s)')
plt.ylabel('Posisjon (m)')
plt.title('Rekke toget..')
plt.grid(True)
plt.plot(x, [st(t) for t in x], label='Tog')
plt.plot(x, [sp(t) for t in x], label='Person')
plt.legend(loc='upper left')
plt.show()
fig.savefig('oppg_3.png')
