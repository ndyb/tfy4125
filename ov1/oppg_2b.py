# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

Tmin = 0
Tmax = 30*60
Tone = 120
Vzero = 30.0

x = range(Tmax+1)
y = [0]*len(x)

f = lambda t: -2*((Vzero*(Tone**2))/(t**3))

for n in range(Tone, Tmax): y[n+1] = f(n)

fig = plt.figure()
plt.axis([Tmin, Tmax, -0.6, 0.1])
plt.xlabel('Tid (s)')
plt.ylabel('Akselerasjon (m/s^2)')
plt.title('Togets akselerasjon')
plt.grid(True)
plt.plot(x, y)
plt.show()
fig.savefig('oppg_2b.png')
