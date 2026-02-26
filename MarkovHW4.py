#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Question 1
import numpy as np

def simulate_gamblerruin(p, q, s, start_i, trials=100000):
    final_amounts = []
    
    for _ in range(trials):
        current_money = start_i
        while current_money > 0:
            rand = np.random.random()
            if rand < p:
                current_money += 1
            elif rand < p + q:
                current_money -= 1
            else:
                break
        else:
            current_money = 0
            
        final_amounts.append(current_money)
        
    return np.mean(final_amounts)

p, q, s = 0.35, 0.4, 0.25
i = 10
trials = 100000

ev = simulate_gamblerruin(p, q, s, i, trials)

print("Simulated Expected Value:",   ev)


# In[2]:


#Question 2 part b
import numpy as np

def factorial(n):
    result = 1
    for k in range(1, n+1):
        result *= k
    return result

def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def binomial_pmf(n, k, p):
    return binomial_coeff(n, k) * (p**k) * ((1-p)**(n-k))

p_survive = 0.9
n_states = 6  

P = np.zeros((n_states, n_states))

P[0,5] = 1

for i in range(1,6):
    for j in range(i+1):
        P[i,j] = binomial_pmf(i, j, p_survive)

print(P)

A = P.T - np.eye(6)
A[-1,:] = np.ones(6) 
b = np.zeros(6)
b[-1] = 1

pi = np.linalg.solve(A,b)

print("Stationary distribution:", pi)
print("Long-run probability only one machine works:", pi[1])



# In[6]:


# part b
A = np.zeros((5,5))
b = np.ones(5)

for i in range(1,6):
    A[i-1,i-1] = 1 - P[i,i]
    for j in range(1,i):
        A[i-1,j-1] = -P[i,j]

E = np.linalg.solve(A,b)

print("E =", E)
print("E5 =", E[4])


# In[4]:


# part c
A = P.T - np.eye(6)
A[-1,:] = np.ones(6) 
b = np.zeros(6)
b[-1] = 1

pi = np.linalg.solve(A,b)

print("Stationary distribution:", pi)
print("Long-run probability only one machine works:", pi[1])

