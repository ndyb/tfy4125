# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

Tmin = 0
Tmax = 30*60
Tone = 120
Vzero = 30.0

x = range(Tmax+1)
y = [Vzero]*len(x)

f = lambda t: ((Vzero*(Tone**2))/(t**2))

for n in range(Tone, Tmax): y[n+1] = f(n)

fig = plt.figure()
plt.axis([Tmin, Tmax, -10, 40])
plt.xlabel('Tid (s)')
plt.ylabel('Hastighet (m/s)')
plt.title('Togets hastighet')
plt.grid(True)
plt.plot(x, y)
plt.show()
fig.savefig('oppg_2a.png')
