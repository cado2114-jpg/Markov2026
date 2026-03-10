#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question 2 - b, c, d
import numpy as np
import matplotlib.pyplot as plt


a = 0.04
b = 0.16
K = 0.1
states = 5


p = np.array([K*np.exp(a*i) for i in range(1,5)])     # p1..p4
q = np.array([K*np.exp(b*(i-1)) for i in range(2,6)]) # q2..q5


P = np.zeros((states,states))

P[0,0] = 1 - p[0]
P[0,1] = p[0]

for i in range(1,4):
    P[i,i+1] = p[i]
    P[i,i-1] = q[i-1]
    P[i,i] = 1 - p[i] - q[i-1]

P[4,3] = q[3]
P[4,4] = 1 - q[3]



eigvals, eigvecs = np.linalg.eig(P.T)
idx = np.argmin(np.abs(eigvals - 1))
pi_eigen = np.real(eigvecs[:,idx])
pi_eigen = pi_eigen / np.sum(pi_eigen)

print("Stationary distribution from eigenvector:")
print(pi_eigen)


pi_theory = np.array([
    np.exp((a-b)*i*(i-1)/2) for i in range(1,6)
])

pi_theory = pi_theory / np.sum(pi_theory)


steps = 10**6
current = 0
counts = np.zeros(states)

for _ in range(steps):
    counts[current] += 1
    current = np.random.choice(states, p=P[current])

hist = counts / steps


x = np.arange(1,6)

plt.bar(x-0.2, hist, width=0.2, label='Simulation')
plt.bar(x, pi_theory, width=0.2, label='Detailed Balance')
plt.bar(x+0.2, pi_eigen, width=0.2, label='Eigenvector')

plt.xlabel("State")
plt.ylabel("Probability")
plt.title("Stationary Distribution Comparison")
plt.legend()

plt.show()


# In[1]:


import sympy as sp
a = sp.symbols('a')
A = sp.Matrix([
    [1-a, a, 0],
    [a, 0, 1-a],
    [0, 1-a, a]
])

eigenvals = A.eigenvals()
print("Eigenvalues (as functions of a):")
for val in eigenvals:
    print(val)

eigenvects = A.eigenvects()
print("\nEigenvectors (v, eigenvalue, multiplicity):")
for vect in eigenvects:
    print(f"For lambda = {vect[0]}: {vect[2][0]}")
import numpy as np

a = 0.99
A = np.array([[1-a, a, 0], [a, 0, 1-a], [0, 1-a, a]])
vals, vecs = np.linalg.eig(A)

# Initial state q0
q0 = np.array([1, 0, 0])
# Find coefficients c
c = np.linalg.solve(vecs, q0)

print("Final Expression Components:")
for i in range(3):
    print(f"Term {i+1}: c={c[i]:.4f}, lambda={vals[i]:.4f}, vector={vecs[:,i]}")


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def solve_markov_chain():
    a = 0.99

    P = np.array([
        [1-a, a,   0],
        [a,   0,   1-a],
        [0,   1-a, a]
    ])
    A = P.T
    eigenvalues, eigenvectors = np.linalg.eig(A)
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    print(f"Eigenvalues for a={a}:")
    print(eigenvalues)
    print("\nEigenvectors:")
    print(eigenvectors)

    q0 = np.array([1, 0, 0])

    c = np.linalg.solve(eigenvectors, q0)

    def theoretical_q(n):
        return eigenvectors @ (c * (eigenvalues**n))

    def theoretical_qn1(n):
        return theoretical_q(n)[0].real

    n_steps = 400
    N_values = [100, 1000, 10000]

    plt.figure(figsize=(12,8))

    n_range = np.arange(n_steps)
    theoretical_probs = [theoretical_qn1(n) for n in n_range]
    plt.plot(n_range, theoretical_probs,
             'r-', linewidth=2,
             label='Theoretical $q_n(1)$', zorder=5)
    for N in N_values:

        states = np.zeros((N, n_steps), dtype=int)
        current_states = np.zeros(N, dtype=int)

        for n in range(n_steps):

            states[:, n] = current_states

            for i in range(N):

                curr = current_states[i]

                if curr == 0:
                    current_states[i] = np.random.choice([0,1], p=[1-a, a])

                elif curr == 1:
                    current_states[i] = np.random.choice([0,2], p=[a, 1-a])

                else:
                    current_states[i] = np.random.choice([1,2], p=[1-a, a])

        fn = np.mean(states == 0, axis=0)

        plt.plot(n_range, fn,
                 alpha=0.7,
                 label=f'Simulation N={N}')

    plt.title(f'Convergence to Stationary Distribution (a={a})')
    plt.xlabel('Time step (n)')
    plt.ylabel('Probability of being in State 1')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

solve_markov_chain()

