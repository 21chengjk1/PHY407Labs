import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import jv
import gaussxw as gsx

N = 4
END  = 1
START = 0
ACTUAL_VAL = np.pi

x = np.linspace(START, END, N+1)

def function(x):
    return 4/(1+np.square(x))

integrand = function(x)

def trapezoid(x_vals, y, n = 0):
    sum = 0
    for i in range(1, len(x_vals)):
        sum += (x_vals[i]-x_vals[i-1])*(y[i]+y[i-1])/2
    
    return sum

def simpson(x, y, n):
    sum = 0 
    deltax = (x[len(x)-1] -x[0])/n

    sum += np.sum(y[1:len(x)-1:2])*4
    sum += np.sum(y[2:len(x)-1:2])*2
    sum += y[0]
    sum += y[len(x)-1]
    return (deltax/3)*sum

def gauss(N):
    x_points, weights = gsx.gaussxwab(N, START, END)
    cumulative = np.sum(weights*function(x_points))
    return cumulative

trap_area = trapezoid(x, integrand)
simp_area = simpson(x, integrand, N)
gauss_area = gauss(N)

print(f"Trapeozid Area with {N} slices: {trap_area}, Error: {np.abs(trap_area-np.pi)}")
print(f"Simpson Area with {N} slices: {simp_area}, Error: {np.abs(simp_area-np.pi)}")
print(f"Gauss Area with {N} slices: {gauss_area}, Error: {np.abs(gauss_area-np.pi)}")

N_space = np.linspace(8, 2048, 21)
print(N_space)

gauss_error_array = []
simpson_error_array = []
trapezoid_error_array = []


for i in N_space:
    i = int(i)
    x = np.linspace(START, END, i+1)
    integrand = function(x)
    trap_area = trapezoid(x, integrand, i)
    simp_area = simpson(x, integrand, i)
    gauss_area = gauss(i)
    # print(f"Trapeozid Area with {i} slices: {trap_area}, Manhattan Error: {np.abs(trap_area-np.pi)}")
    # print(f"Simpson Area with {i} slices: {simp_area}, Manhattan Error: {np.abs(simp_area-np.pi)}")
    # print(f"Gauss Area with {i} slices: {gauss_area}, Manhattan Error: {np.abs(gauss_area-np.pi)}")

    gauss_area_2 = gauss(2*i)
    error = gauss_area_2 - gauss_area
    gauss_error_array.append(np.abs(error))

    x_2 = np.linspace(START, END, 2*i+1)
    integrand2 = function(x_2)
    trap_area_2 = trapezoid(x_2, integrand2, 2*i)
    error = trap_area_2 - trap_area
    trapezoid_error_array.append(np.abs(error))


    simp_area_2 = simpson(x_2, integrand2, 2*i)
    error = simp_area_2 - simp_area
    simpson_error_array.append(np.abs(error))
    

gauss_error_array = np.array(gauss_error_array)
trapezoid_error_array = np.array(trapezoid_error_array)
simpson_error_array = np.array(simpson_error_array)

plt.title("Log Log Curve of the Relative Error for Gaussian, Trapezoid, and Simpson Approx")
plt.loglog(N_space, gauss_error_array, label = "Gauss Quadrature")
plt.loglog(N_space, trapezoid_error_array, label = "Trapezoid")
plt.loglog(N_space, simpson_error_array, label = "Simpson")
plt.xlabel("Number of Slices N")
plt.ylabel("Relative Error")
plt.legend(["gauss", "trap", "simp"])
plt.show()







# def timing(func):
#     error = 100
#     n = 1

#     while error >= 10**(-9):
#         n +=1 
#         N = 2**n
#         x = np.linspace(START, END, N+1)
#         integrand = function(x)
#         area = func(x, integrand, N)
#         error = np.abs(ACTUAL_VAL - area)

#     start = time.time()
#     x = np.linspace(START, END, N+1)
#     integrand = function(x)
#     area = func(x, integrand, N)
#     end = time.time()
#     total_time = end-start
#     print(end-start)
    
#     return area, N, total_time

# trap_area, trap_slices, trap_time = timing(trapezoid)
# simp_area, simp_slices, simp_time = timing(simpson)

# print(f"""Trapezoid Area: {trap_area}
# Trapezoid Slices: {trap_slices}
# Trapezoid Timing: {trap_time}
# Trapezoid Error: {np.abs(trap_area-np.pi)}""")

# print(f"""Simpson Area: {simp_area}
# Simpson Slices: {simp_slices}
# Simpson Timing: {simp_time}
# Simpson Error: {np.abs(simp_area-np.pi)}""")

# N1 = 16
# x1 = np.linspace(START, END, N1)
# integrand1 = function(x1)
# trap1 = trapezoid(x1, integrand1)

# N2 = 32
# x2= np.linspace(START, END, N+1)
# integrand2 = function(x2)
# trap2 = trapezoid(x2, integrand2)

# error = 1/3*np.abs(trap2 - trap1)
# print(f"Practial Estimation of Error: {error}")