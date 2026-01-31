#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math
Nlst = [100, 1000, 10000]
gamma = 4
x0 = 10
xmax = 60
def fxn(x):
    c = (gamma - 1)*x0**(gamma-1)
    return c*x**(-gamma)
def cdf(n):
    u = np.random.rand(n)
    return x0*(1-u)**(-1/(gamma-1))
xvals = np.linspace(x0, xmax, 1000)
for num in Nlst:
    samples = cdf(num)
    plt.hist(samples, bins = 50, range = (0, xmax), density = True)
plt.plot(xvals, fxn(xvals), label = "Theoretical")
plt.xlim(0, xmax)
plt.xlabel('x')
plt.ylabel('Density')
plt.title("Sampling")
plt.show()


# In[2]:


# question 2b
import time
def sampling(N = 10**6, tolerance = 1e-6, iterations = 100):
    u = np.random.rand(N)
    x = np.ones(N)
    start = time.time()
    for i in range(iterations):
        g = 1-(1+x)*(np.exp(-x)) - u
        dg = x*np.exp(-x)
        dx = g/dg
        x = x-dx
        if np.max(np.abs(dx))< tolerance:
            break
    end = time.time()
    print("The runtime is", str(end-start))
    return x
samples=sampling()
samples   


# In[6]:


# question 2c
N = 10**6
c = 4*np.exp(-1)
def f(x):
    return x*np.exp(-x)
def g(x):
    return .5*np.exp(-x/2)
acceptances = np.zeros(N)
count = 0
start = time.perf_counter()
while count<N:
    u = np.random.uniform(0, 1)
    y = -2*np.log(u)
    uac = np.random.uniform(0, 1)
    if uac<= f(y)/(c*g(y)):
        acceptances[count] = y
        count += 1
end = time.perf_counter()
print('Runtime was', str(end-start))
acceptances


# In[7]:


# question 2d
n = 10**6
start = time.perf_counter()
u1 = np.random.uniform(0, 1, n)
u2 = np.random.uniform(0, 1, n)
samps = -np.log(u1)-np.log(u2)
end = time.perf_counter()
print('Runtime was', str(end-start))
samps


# In[13]:


# question 2 e
x = np.linspace(0, np.max(samples), 1000)
pdf = x * np.exp(-x)
plt.hist(samples, bins=100, density=True, label='Hist A')
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
plt.title('Comparison of Gamma(2,1) vs PDF')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()


# In[16]:


x = np.linspace(0, np.max(samples), 1000)
pdf = x * np.exp(-x)
plt.hist(samps, bins=100, density=True, color = 'orange', label='Hist D')
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
plt.title('Comparison of Gamma(2,1) vs PDF')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()


# In[17]:


x = np.linspace(0, np.max(samples), 1000)
pdf = x * np.exp(-x)
plt.hist(acceptances, bins=100, density=True, color = 'cyan', label='Hist C')
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
plt.title('Comparison of Gamma(2,1) vs PDF')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()
plt.show()

