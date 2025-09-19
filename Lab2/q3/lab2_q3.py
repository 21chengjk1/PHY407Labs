"""
Lab 2 Question 3
"""
import numpy as np
from scipy.constants import epsilon_0
from scipy.special import k0
import matplotlib.pyplot as plt

def simpson(x, y):
    """
    Simpson's rule is : 
    (deltax / 3) * ( y(x_first) 
                    + 4 * (sum of y(x_odds)) 
                    + 2 * (sum of y(x_even))
                    + y(x_last) ) 


    """
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of subintervals (odd number of points).")

    deltax = (x[-1] - x[0]) / n
    sum = y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2])
    return (deltax/3) * sum


def function(u, Q, l, r, z, eps0):
    return (Q * np.exp(-(np.tan(u))**2)) / (
        4*np.pi*eps0 * (np.cos(u)**2) * np.sqrt((z - l*np.tan(u))**2 + r**2)
    )


def V_simpson(r, z, Q, l, n):
    x = np.linspace(-np.pi/2, np.pi/2, n+1)
    y = function(x, Q, l, r, z, epsilon_0)
    return simpson(x, y)


def V_exact(r, Q, l):
    return (Q / (4*np.pi*epsilon_0*l)) * np.exp(r**2/(2*l**2)) * k0(r**2/(2*l**2))


def main():
    print("----------START----------")
    # Parameters
    Q = 1e-13
    l = 1e-3
    z = 0
    
    r_values = np.linspace(0.25e-3, 5e-3, 100)  # 0.25 mm to 5 mm
    n = 14                                      # must be even

    V_by_simpson = [V_simpson(r, z, Q, l, n) for r in r_values]
    V_by_exact = [V_exact(r, Q, l) for r in r_values]

    print(V_by_simpson[0])
    print(V_by_exact[0])

    plt.figure()
    plt.plot(r_values*1e3, V_by_simpson, label="Simpson (Eq. 8)")
    plt.plot(r_values*1e3, V_by_exact, label="Exact (Eq. 9)")
    plt.xlabel("r (mm)")
    plt.ylabel("V(r, 0)")
    plt.legend()
    plt.title("V(r,0): Numerical vs Exact")
    plt.show()

    plt.figure()
    diff = np.array(V_by_simpson) - np.array(V_by_exact)
    frac_error = diff / np.array(V_by_exact)
    plt.plot(r_values*1e3, frac_error)
    plt.xlabel("r (mm)")
    plt.ylabel("Fractional error")
    plt.title(f"Fractional error (N={n})")
    plt.show()

    print("----------END----------")

if __name__ == "__main__":
    main()