#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import math
import matplotlib.pyplot as plt
lambda_A_tot = 2.0
lambda_B_tot = 1.5
T = 90.0

lambda_A = lambda_A_tot / T
lambda_B = lambda_B_tot / T


def poisson_pmf(k, l):
    return math.exp(-l) * l**k / math.factorial(k)

# part a
def prob_A_wins(max_k=20):
    prob = 0.0
    for k in range(max_k):
        p_B_k = poisson_pmf(k, lambda_B_tot)
        p_A_greater = sum(poisson_pmf(j, lambda_A_tot) for j in range(k+1, max_k))
        prob += p_B_k * p_A_greater
    return prob

p_win_A = prob_A_wins()
print("P", p_win_A)


# In[5]:


# part b
def prob_tie_no_goals(t, max_k=20):
    remaining = T - t
    lamA = lambda_A * remaining
    lamB = lambda_B * remaining
    prob = 0.0
    for k in range(max_k):
        prob += poisson_pmf(k, lamA) * poisson_pmf(k, lamB)
    return prob
t_vals = np.linspace(0, 90, 200)
tie_probs_b = [prob_tie_no_goals(t) for t in t_vals]
plt.figure(figsize=(10,5))
plt.plot(t_vals, tie_probs_b, label="No goals yet", color='blue')
plt.xlabel("t")
plt.ylabel("Prob of Tie")
plt.title("Prob of tie v time")
plt.grid(True)
plt.legend()
plt.show()


# In[7]:


# part c
def prob_tie_after_goal(t, max_k=20):
    if t < 60:
        return prob_tie_no_goals(t, max_k)
    remaining = T - t
    lamA = lambda_A * remaining
    lamB = lambda_B * remaining
    prob = 0.0
    for k in range(max_k):
        prob += poisson_pmf(k, lamA) * poisson_pmf(k+1, lamB)
    return prob
tie_probs_c = [prob_tie_after_goal(t) for t in t_vals]
plt.figure(figsize=(10,5))
plt.plot(t_vals, tie_probs_c, label="After A scores at t=60", color='orange')
plt.axvline(60, linestyle='--', color='red', label="A scores at 60 min")
plt.xlabel("t")
plt.ylabel("Prob of Tie")
plt.title("Prob of Tie w goal at 60")
plt.grid(True)
plt.legend()
plt.show()


# In[13]:


# Question 2
# part c
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
T = 48   
lam = 3       
def simulate_times(lam, T):
    times = []
    t = 0
    while t < T:
        t += np.random.exponential(1 / lam)
        if t < T:
            times.append(t)
    return np.array(times)
tA = simulate_times(lam, T)
tB = simulate_times(lam, T)
plt.figure(figsize=(10, 2))
plt.eventplot([tA, tB],
              lineoffsets=[1, 2],
              linelengths=0.8)
plt.yticks([1, 2], ["A", "B"])
plt.xlim(0, T)
plt.xlabel("t")
plt.title("Score sim")
plt.show()


# In[16]:


# part d
np.random.seed(1)
def simulate_combined(lam, T):
    times = []
    teams = []
    t = 0
    while t < T:
        t += np.random.exponential(1/(2*lam))
        if t < T:
            times.append(t)
            teams.append(np.random.choice(['A', 'B']))
    
    return np.array(times), np.array(teams)
times, teams = simulate_combined(lam, T)
tA = simulate_times(lam, T)
tB = simulate_times(lam, T)
plt.figure(figsize=(10, 2))
plt.eventplot([tA, tB],
              lineoffsets=[1, 2],
              linelengths=0.8)
plt.yticks([1, 2], ["A", "B"])
plt.xlim(0, T)
plt.xlabel("t")
plt.title("Score sim")
plt.show()


# In[17]:


#part e
np.random.seed(2)
num_games = 100000
T = 48
lam = 3
N = np.random.poisson(2 * lam * T, size=num_games)
NA = np.random.binomial(N, 0.5)
NB = N - NA
D = 2 * (NA - NB)
mean_est = np.mean(D)
var_est = np.var(D)
tie_prob_est = np.mean(D == 0)
print("E", mean_est)
print("Var", var_est)
print("P", tie_prob_est)
mean_th = 0
var_th = 8 * lam * T
tie_th_approx = 1 / np.sqrt(4 * np.pi * lam * T)
print("E2", mean_th)
print("Var2", var_th)
print("P2", tie_th_approx)


# In[1]:


# question 3
# part b
import sympy as sp
t = sp.symbols('t')
lam = 0.5 * (1 + (t/30)**2)
expected = sp.integrate(lam, (t, 0, 120))  
print(float(expected))


# In[2]:


# part c
import numpy as np
import matplotlib.pyplot as plt
def lam(t):
    return 0.5 * (1 + (t/30)**2)
T = 120
lam_max = lam(T) 
times = []
t = 0
while t < T:
    t += np.random.exponential(1/lam_max)
    if t < T:
        if np.random.rand() < lam(t)/lam_max:
            times.append(t)
bins = np.arange(0, T+1, 1)
plt.hist(times, bins=bins)
plt.xlabel("Day")
plt.ylabel("# reports")
plt.title("flu reports")
plt.show()
print(len(times))

