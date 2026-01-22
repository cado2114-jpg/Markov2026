#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp


# In[ ]:





# In[2]:


def fxn(x):
    return 1/(1+x**6)
actual = mp.quad(fxn, [1, mp.inf])
def fxnu(u):
    t = .5*(1+u)
    return 1/12*(t**(-5/6))*((1-t)**(-1/6))
x2 = np.arange(1, 5.1, .1)
N = np.floor(10**x2).astype(int)
est = []
r = np.random.default_rng(0)
for item in N:
    u = r.random(item)
    v = r.random(item)
    est.append(np.mean(v<= fxnu(u)))
plt.figure()
plt.semilogx(N, est, label = "Monte Carlo Est")
plt.axhline(actual, label = "Actual Integral Value")
plt.xlabel("N")
plt.ylabel("Est")
plt.legend()
plt.show()


# In[5]:


n = 10**5
times = np.random.uniform(0, 1, size = (n, 3))
maxt = np.max(times, axis = 1)
plt.hist(maxt, bins = 50)
plt.xlabel('Time')
plt.ylabel('Density Value')
plt.title('Arrival Time Distribution')
plt.show()


# In[8]:


import sympy as sp
s, n = sp.symbols('s n', positive = True)
mgf = sp.exp(n*(sp.exp(s/sp.sqrt(n))-1-s/sp.sqrt(n)))
sp.series(mgf, s, 0, 4)
             
                


# In[10]:


E1  = sp.diff(mgf, s).subs(s, 0)
E2 = sp.diff(mgf, s, 2).subs(s, 0)
E3 = sp.diff(mgf, s, 3).subs(s, 0)
E3

