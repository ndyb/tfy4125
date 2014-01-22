# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

N = 50
Tmin = 0
Tmax = 1
Vzero = 1.5
K = 3

t = np.linspace(Tmin, Tmax, N)
h = t[1] - t[0]

v = np.zeros(N)
v[0] = Vzero

for i in range(N-1):
	v[i+1] = v[i] - K*h*v[i]**2

f = lambda t: ((2/3)+3*t)**(-1)

fig = plt.figure()
plt.axis([Tmin, Tmax, np.min(v), Vzero])
plt.grid(True)
plt.ylabel('Hastighet')
plt.xlabel('Tid')
plt.title('Eulers metode med N=50')
plt.plot(t, v, label='Numerisk approksimasjon')
plt.plot(t, f(t), '--', label='Analytisk løsning')
plt.plot(2/9, 0.75, 'o', label='Halv fart')
plt.legend()
plt.savefig('oppg_3a.png')
plt.show()
