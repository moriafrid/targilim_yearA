# ex6 yael kapon


import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# import data from Fig 2 of paper

NW=(np.array([111,146,158,180,201,234,321,490,635,810,1014,1500,1800,2000,3000])-111)/700

# add numerix
n1 = 10000
NW = np.append(0.05, NW)
g2 = np.zeros(len(NW))
k = 0
for i in NW:
    photons = 1 + random.poisson(i, n1)
    ar = np.zeros(n1)
    at = np.zeros(n1)
    for j in range(n1):
        bs = random.choice(2, photons[j])
        ar[j] = len(np.where(bs == 0)[0])
        at[j] = len(np.where(bs == 1)[0])
    g2[k] = np.mean(ar * at) / (np.mean(ar) * np.mean(at))
    k += 1

plt.plot(NW, g2,'.', color='red', label='numeric')
plt.legend()
plt.show()