#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[2]:


# Question 1
def f(x):
    return (1/3)*x*(x+1)*np.exp(-x)
astar = np.sqrt(3)-1
def g(x, a = astar):
    return a**2*x*np.exp(-a*x)
cstar = 1 / (((3 * astar**2 * (1 - astar))) * np.exp(-astar))
x = np.linspace(0, 15, 1000)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, cstar * g(x), label=r"$c(a^*) g_{a^*}(x)$")
plt.xlabel("x")
plt.ylabel("density")
plt.legend()
plt.show()


# In[3]:


# Question 2
import numpy as np

P = np.array([
    [9/10, 1/10, 0],
    [0, 7/8, 1/8],
    [2/5, 0, 3/5]
])

P50 = np.linalg.matrix_power(P, 50)
P50


# In[4]:


# Question 2
import random

states = ["G", "S", "D"]
state = "G"

count_G = 0
steps = 10000

for _ in range(steps):
    if state == "G":
        state = "S" if random.random() < 1/10 else "G"
    elif state == "S":
        state = "D" if random.random() < 1/8 else "S"
    elif state == "D":
        state = "G" if random.random() < 2/5 else "D"

    if state == "G":
        count_G += 1

fraction_G = count_G / steps
fraction_G


# In[3]:


#Question 3
import numpy as np

P = np.array([
    [1, 0, 0, 0, 0],
    [1/3, 0, 2/3, 0, 0],
    [0, 1/3, 0, 2/3, 0],
    [0, 0, 1/3, 0, 2/3],
    [0, 0, 0, 0, 1]
])

P4 = np.linalg.matrix_power(P, 4)
P4


# In[4]:


# Question 4 b
import numpy as np

P = np.array([
    [1/2, 1/2, 0, 0, 0, 0],
    [0, 1/2, 1/2, 0, 0, 0],
    [1/3, 0, 1/3, 1/3, 0, 0],
    [0, 0, 0, 1/2, 1/2, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0]
])

P5 = np.linalg.matrix_power(P, 5)
P5


# In[5]:


# Question 4 c
def simulate_chain(P, x0, steps):
    x = x0
    for a in range(steps):
        # defined matrix P above
        x = np.random.choice(len(P), p=P[x])
        # here len(P) gives us the possible states that it could be in
        # and x is the current state, so P[x] gives us the row for state
        # x
    return x
n = 10000
count = 0

for i in range(n):
    X5 = simulate_chain(P, x0=0, steps=5)
    # state 4 is indexed at 3 bc of python notation
    if X5 == 3:    
        count += 1

fraction = count / n
fraction

