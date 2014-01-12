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

Tn = lambda b, a, n, l: ((b-a)/(n*2))*(y[b]+y[a])

# ...
