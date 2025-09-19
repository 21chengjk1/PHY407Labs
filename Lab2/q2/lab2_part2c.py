import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import jv

from mpl_toolkits import mplot3d


SLICES = 1000

Z = 11.620
n = 2

phi = np.linspace(0, np.pi, SLICES+1)


def function(n, x, theta):
    return np.cos(n*theta-x*np.sin(theta))

def simpson(theta, y, n):
    sum = 0 
    deltax = (theta[len(theta)-1] -theta[0])/n

    sum += np.sum(y[1:len(theta)-1:2])*4
    sum += np.sum(y[2:len(theta)-1:2])*2
    sum += y[0]
    sum += y[len(theta)-1]
    return (deltax/3)*sum

def bessel_func(n, x, phi):
    jes = np.zeros_like(x)
    for i in range(len(x)):
        y = function(n, x[i], phi)
        j = simpson(phi, y, SLICES)
        jes[i] = 1/np.pi*j
    return jes

r_over_R = np.linspace(0, 1, 100+1)
theta = np.linspace(0, np.pi*2, 100+1) 

def u_func(n, x, theta):
    return bessel_func(n, Z*x, phi)*np.cos(n*theta)

u_func_vals = np.zeros((100+1, 100+1))

for i in range(len(r_over_R)):
    for j in range(len(theta)):
        vals = u_func(n, r_over_R, theta[j])
        u_func_vals[i][j] = vals[i]

r, theta = np.meshgrid(r_over_R, theta)


fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
ax.set_title("Surface Plot of Wave Equation")
ax.set_xlabel("r/R from [0, 1]")
ax.set_ylabel(r"$\theta$ from [0, 2$\pi$]")
ax.plot_surface(r, theta, u_func_vals)
plt.show()
