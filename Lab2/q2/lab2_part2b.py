import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import jv

N = 1000
END  = np.pi
START = 0

theta = np.linspace(START, END, N+1)
theta = theta.reshape((theta.shape))
print(theta.shape)

def simpson(theta, y, n):
    sum = 0 
    deltax = (theta[len(x)-1] -theta[0])/n

    sum += np.sum(y[1:len(theta)-1:2])*4
    sum += np.sum(y[2:len(theta)-1:2])*2
    sum += y[0]
    sum += y[len(theta)-1]
    return (deltax/3)*sum

x = np.linspace(0, 20, N+1)

def function(n, x, theta):
    return np.cos(n*theta-x*np.sin(theta))

def bessel_func(n, x, theta):
    jes = np.zeros_like(x)
    for i in range(len(x)):
        y = function(n, x[i], theta)
        j = simpson(theta, y, N)
        jes[i] = j
    return jes
    

J0 = bessel_func(0, x, theta)
print(J0[0])
J3 = bessel_func(3, x, theta)
J5 = bessel_func(5, x, theta)

# plt.title("Bessel Functions Plotted Together J0, J3, J5")
# plt.plot(x, J0, label = "J0")
# plt.plot(x, J3, label = "J3")
# plt.plot(x, J5, label = "J5")
# plt.legend(["J0", "J3", "J5"], labels = ["J0", "J3", "J5"])

# plt.xlabel("X: 0 to 20")
# plt.ylabel("Range of Bessel Functions")
# plt.show()

# def plotting(actual, mine, x, n):
#     plt.title(f"Difference Between Bessel Functions {n}")
#     plt.plot(x, actual, label = "Actual")
#     plt.plot(x, mine, label = "Simpson")
#     plt.legend(["Actual", "Simpson"], labels = ["Actual", "Simpson"])
#     plt.show()

# plotting(jv(0, x), J0, x, 0)
# plotting(jv(3, x), J3, x, 3)
# plotting(jv(5, x), J5, x, 5)