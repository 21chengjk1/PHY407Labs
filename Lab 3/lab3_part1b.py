import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import fresnel
import gaussxw as gsx

LAMBDA = 1
Z = 3
START = -5
END = 5
N = 50

x = np.linspace(START, END, N)
mu = np.sqrt(2/LAMBDA*Z)*x

def cfunction(x):
    return np.cos(1/2*np.pi*x**2)

def sfunction(x):
    return np.sin(1/2*np.pi*x**2)

def intensity(cfres, sfres):
    return 1/8*((2*cfres+1)**2+(2*sfres+1)**2)


csum_array = []
ssum_array = []


for j in mu:
    x_points, weights = gsx.gaussxwab(N, 0, j)
    csum = np.sum(weights*cfunction(x_points))
    ssum = np.sum(weights*sfunction(x_points))
    csum_array.append(csum)
    ssum_array.append(ssum)

ssci, csci = fresnel(mu)

csum_array = np.array(csum_array)
ssum_array = np.array(ssum_array)

intensity_fresnel = intensity(csci, ssci)
intensity_gauss = intensity(csum_array, ssum_array)
error = np.abs((intensity_fresnel - intensity_gauss)/intensity_fresnel)


plt.figure()
plt.plot(x, intensity_fresnel, label = "Scipy")
plt.plot(x, intensity_gauss, label = "Gauss Approximation")
plt.title("Intensity of Plane Wave Diffraction")
plt.xlabel("Position x (Meters)")
plt.ylabel("Intensity (Watts per Square Meter)") 
plt.legend(loc = "upper right")

plt.figure()
plt.title("Error Between Scipy and Gaussian Approximation of Plane Wave Diffraction")
plt.plot(x, error)
plt.xlabel("Position x (Meters)")
plt.ylabel("Error (Unitless)")
plt.show()

N_space = np.linspace(3, 48, 12)
max_error_array = []
avg_arr = []
for i in N_space:
    i = int(i)
    x = np.linspace(START, END, i)
    mu = np.sqrt(2/LAMBDA*Z)*x
    mu = mu[x>0]

    csum_array = []
    ssum_array = []


    for j in mu:
        x_points, weights = gsx.gaussxwab(N, 0, j)
        csum = np.sum(weights*cfunction(x_points))
        ssum = np.sum(weights*sfunction(x_points))
        csum_array.append(csum)
        ssum_array.append(ssum)

    ssci, csci = fresnel(mu)

    csum_array = np.array(csum_array)
    ssum_array = np.array(ssum_array)

    intensity_fresnel = intensity(csci, ssci)
    intensity_gauss = intensity(csum_array, ssum_array)

    error = np.abs((intensity_fresnel - intensity_gauss)/intensity_fresnel)
    max_error_array.append(np.max(error))
    avg_arr.append(np.sum(error)/len(error))

plt.figure()
plt.title("Maximum Error as the Number of Slices Varies")
plt.plot(N_space, max_error_array)
plt.xlabel("Number of Slices (N)")
plt.ylabel("Error (Unitless)")
plt.figure()
plt.title("Average Error as the Number of Slices Varies")
plt.plot(N_space, avg_arr)
plt.xlabel("Number of Slices (N)")
plt.ylabel("Error (Unitless)")


plt.show()

