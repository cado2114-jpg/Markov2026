#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def simulate_once(L, alpha=1, beta=1):
    i = 0
    t = 0.0
    while i < L:
        if i == 0:
            rate = alpha
            t += np.random.exponential(1/rate)
            i += 1
        else:
            rate = alpha + beta
            t += np.random.exponential(1/rate)
            if np.random.rand() < alpha / rate:
                i += 1
            else:
                i -= 1
    return t
def run_sim(N=1000, L=20):
    times = [simulate_once(L) for _ in range(N)]
    return np.mean(times), np.var(times)
mean, var = run_sim(1000, 20)
print(mean, var)


# In[2]:


# q 4 on yule
import numpy as np
import matplotlib.pyplot as plt
beta = 1.0 
m_vals = np.arange(2, 101)
tau1 = []
for m in m_vals:
    sum1 = sum(1/k for k in range(1, m))
    tau1.append(sum1 / beta)
tau1 = np.array(tau1)
tau_det = (1 / beta) * np.log(m_vals)
plt.figure()
plt.plot(m_vals, tau1, label="tau 1")
plt.plot(m_vals, tau_det, label="det")
plt.xlabel("m")
plt.ylabel("tau_m")
plt.title("Yule process")
plt.legend()
plt.show()

