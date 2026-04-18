#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig, expm
Q = np.array([
    [-1, 1, 0, 0],
    [0, -1, 1, 0],
    [0, 0, -1, 1],
    [1, 0, 0, -1]
], dtype=float)
eigvals, eigvecs = eig(Q)
print(eigvals)


# In[2]:


# part d
import sympy as sp
Q = sp.Matrix([
    [-1,  1,  0,  0],
    [ 0, -1,  1,  0],
    [ 0,  0, -1,  1],
    [ 1,  0,  0, -1]
])
QT = Q.T 
y0 = sp.Matrix([sp.Rational(1,3), sp.Rational(2,3), 0, 0])
t = sp.Symbol('t', positive=True)
expQTt = (QT * t).exp()
yt = expQTt * y0 
y1_t = sp.simplify(yt[0])
y1_expanded = sp.expand(y1_t)
print(y1_expanded)
t0   = y1_expanded.subs(t, 0)
print(t0)            
tinf = sp.limit(y1_expanded, t, sp.oo)
print(tinf)  


# In[5]:


# part e
def y1(t):
    return 1/4 - (1/12)*np.exp(-2*t) + np.exp(-t)*(np.cos(t)/6 + np.sin(t)/3)
def simulate_chain(T):
    t = 0
    state = 1 if np.random.rand() < 1/3 else 2
    times = [0]
    states = [state]

    while t < T:
        rate = 1 
        t += np.random.exponential(1 / rate)
        state = state % 4 + 1

        times.append(t)
        states.append(state)

    return times, states


def fraction_in_state1(N, T=5, dt=0.01):
    grid = np.arange(0, T, dt)
    counts = np.zeros_like(grid)
    for _ in range(N):
        times, states = simulate_chain(T)
        idx = 0
        current_state = states[0]

        for i, t in enumerate(grid):
            while idx + 1 < len(times) and times[idx + 1] <= t:
                idx += 1
                current_state = states[idx]
            if current_state == 1:
                counts[i] += 1
    return grid, counts / N
plt.figure()
for N in [100, 1000, 10000, 100000]:
    t, f = fraction_in_state1(N)
    plt.plot(t, f, label=f"N={N}")
t_vals = np.linspace(0, 5, 300)
theory = [y1(t) for t in t_vals]
plt.plot(t_vals, theory, linestyle='--', label="theory")
plt.xlim(0, 5)
plt.ylim(0, 0.5)
plt.xlabel("t")
plt.ylabel("Fraction in state 1")
plt.title("Convergence to Stationary Distribution")
plt.legend()
plt.show()


# In[13]:


# question 2 c
import numpy as np
from scipy.linalg import expm
import numpy as np
from sympy import *
Q = Matrix([[-2, 1, 1],
            [ 1,-1, 0],
            [ 1, 0,-1]])
evals = Q.eigenvals()
evecs = Q.eigenvects()
t = symbols('t', positive=True)
c0, c1, c2 = symbols('c0 c1 c2')
v0 = Matrix([1, 1, 1])
v1 = Matrix([0,-1, 1])
v2 = Matrix([-2, 1, 1])
y0 = Matrix([0, 1, 0])
sol = solve(c0*v0 + c1*v1 + c2*v2 - y0, [c0, c1, c2])
yF = sol[c0]*1 + sol[c1]*0         + sol[c2]*(-2)*exp(-3*t)
yN = sol[c0]*1 + sol[c1]*(-1)*exp(-t) + sol[c2]*1*exp(-3*t)
yD = sol[c0]*1 + sol[c1]*1*exp(-t)  + sol[c2]*1*exp(-3*t)
print("sol")
print("y_F(t) =", yF)
print("y_N(t) =", yN)
print("y_D(t) =", yD)


# In[17]:


#question 3 part c
from sympy import * #looked up how to solve this infinite sum
n = symbols('n', integer=True, nonnegative=True)
def w(k):
    return Rational(6)**k * factorial(12) / factorial(k + 12)
Z = summation(w(n), (n, 0, oo))
pi0 = 1 / Z
EX = sum(k * w(k) / Z for k in range(100)) 
print(float(EX))

