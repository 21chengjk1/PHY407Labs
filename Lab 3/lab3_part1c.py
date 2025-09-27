import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import fresnel
import gaussxw as gsx


LAMBDA = 4
ZSTART = 1
ZEND = 5
XSTART = -3
XEND = 10
N = 50

x = np.linspace(XSTART, XEND, N) #1D array
z = np.linspace(ZSTART, ZEND, N) #1D array
z2D = np.tile(z, (50, 1)) 

result = z2D*x[:, np.newaxis] #Changing column varies with z

# print(x[:, np.newaxis])

mu = np.sqrt(2/LAMBDA/z2D)*x[:, np.newaxis] #2D array.

def cfunction(x):
    return np.cos(1/2*np.pi*x**2)

def sfunction(x):
    return np.sin(1/2*np.pi*x**2)

def intensity(cfres, sfres):
    return 1/8*((2*cfres+1)**2+(2*sfres+1)**2)

gauss = np.ones_like(mu)

for i in range(mu.shape[0]):
    for j in range(mu.shape[1]):
        x_points, weights = gsx.gaussxwab(N, 0, mu[i][j])
        csum = np.sum(weights*cfunction(x_points))
        ssum = np.sum(weights*sfunction(x_points))
        gauss[i][j] = intensity(csum, ssum)

ssci, csci = fresnel(mu)

scipy_vals = intensity(csci, ssci)

cut = 2.0
gauss_focus = np.ma.masked_greater(gauss, cut)

plt.figure(figsize=(6,4))
plt.contourf(z, x, gauss_focus, 60)
plt.xlabel('z'); plt.ylabel('x'); plt.title(f'Fresnel intensity (λ={LAMBDA} m), Gauss quad')
plt.colorbar()

plt.figure(figsize=(6,4))
plt.contourf(z, x, scipy_vals, 60)
plt.xlabel('z'); plt.ylabel('x'); plt.title('Validation with SciPy fresnel')
plt.colorbar()

plt.show()

