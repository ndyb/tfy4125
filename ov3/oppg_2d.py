# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

N = 50
Tmin = 0
Tmax = 10
Vzero = 0
Theta = np.pi/6
g = 9.81

t = np.linspace(Tmin, Tmax, N)
h = t[1] - t[0]

v = np.zeros(N)
v[0] = Vzero

dv = lambda v: (0.42+0.13*v)*g*np.cos(Theta)-np.sin(Theta)*g
dv = lambda v: 0.42*g*np.cos(Theta)+0.13*v*g*np.cos(Theta)-np.sin(Theta)*g

for i in range(N-1):
        v[i+1] = v[i] - h*(dv(v[i]))

a = -0.13*g*np.cos(Theta)
c = -0.42*g*np.cos(Theta)+np.sin(Theta)*g
f = lambda t: (c/a)*(np.e**(a*t)-1)

fig = plt.figure()
# plt.axis([Tmin, Tmax, np.min(v), Vzero])
plt.grid(True)
plt.ylabel('Hastighet')
plt.xlabel('Tid')
plt.title('Eulers metode med N=50')
plt.plot(t, v, label='Numerisk approksimasjon')
plt.plot(t, f(t), '--', label='Analytisk løsning')
plt.legend(loc = 'lower right')
plt.savefig('oppg_2d.png')
plt.show()
