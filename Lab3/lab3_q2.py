"""
Welcome to the Code for Lab 3 Question 2 in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab3
"""

import numpy as np
from util import gaussxw as gsx
from scipy.constants import speed_of_light
import matplotlib.pyplot as plt

PRINT_OUPUTS_FOR_PART_C = False
PLOT_GRAPHS = False

GET_LAB5_VALUES = True


# List of Constants used by g(x)
c = speed_of_light  # The speed of light!
k = 12              # 12 N/m          
m = 1               # 1 kg
x_0 = 1e-2          # 1 cm = 1 * 10 ^ -2 metres 
def g(x):
    x_diff_sq = x_0 ** 2 - x ** 2
    dividend = k * x_diff_sq * (2 * m * (c ** 2) + (k * x_diff_sq / 2) )
    divisor = 2 * ((m * (c ** 2) + (k * x_diff_sq / 2)) ** 2)
    quotient = dividend / divisor
    return c * np.sqrt(quotient)

def integrand(x):
    return 1 / g(x)

def compute_integral_with_gauss(N, a, b):
    """
    Helper function to compute 
    
    Time period = 4 * integral from a to b ( 1 / g(x))
    
    using gaussian quadrature with a given N, bounds a and b
    outputs:
    - The Time period answer
    - x
    - w
    - integrands
    - weighted
    """
    x, w = gsx.gaussxwab(N, a, b)
    integrands = 4 * np.array([integrand(xi) for xi in x])
    weighted = 4 * w * np.array([integrand(xi) for xi in x])
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for i in range(N):
        I += w[i] * integrand(x[i])
    time_period = 4 * I

    return time_period, x, w, integrands, weighted

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 3 Question 2!")

    global x_0  # Declare x_0 as a global variable that we may need to change

    # We want to test T = 4 * Integral from 0 to x_0 ( dx′ / g(x′) )
    # Let's first compute the "Boring value" = 2 * pi * sqrt( m / k )

    # While we do this we need to save:
        # sample values x from gaussxw
        # integrands 4/g_k
        # weighted values 4 w_k/g_k

    boring_time_period = 2 * np.pi * np.sqrt(m / k)
    print(f"The boring time period is: {boring_time_period}")

    # Now let's compute the for x_0 = 1cm to see if the relativistic value matches
    global x_0
    x_0 = 1e-2

    time_period_N_is_8, x_8, w_8, integrands_8, weighted_8 = compute_integral_with_gauss(8, 0, x_0)
    fractional_error_N_is_8 = abs(time_period_N_is_8 - boring_time_period) / boring_time_period
    print(f"The time period for N = 8 is: {time_period_N_is_8}\
    This implies fractional error of: {fractional_error_N_is_8}")
    
    time_period_N_is_16, x_16, w_16, integrands_16, weighted_16 = compute_integral_with_gauss(16, 0, x_0)
    fractional_error_N_is_16 = abs(time_period_N_is_16 - boring_time_period) / boring_time_period
    print(f"The time period for N = 16 is: {time_period_N_is_16}\
    This implies fractional error of: {fractional_error_N_is_16}")

    if PLOT_GRAPHS:
        # Plot integrands.
        plt.figure()
        plt.plot(x_8, integrands_8, "o", label="N=8")
        plt.plot(x_16, integrands_16, "s", label="N=16")
        plt.title("Integrand values 4/g(x) at sample points")
        plt.xlabel("x (m)")
        plt.ylabel("4/g(x)")
        plt.legend()
        plt.grid(True)

        # Plot weighted values
        plt.figure()
        plt.plot(x_8, weighted_8, "o", label="N=8")
        plt.plot(x_16, weighted_16, "s", label="N=16")
        plt.title("Weighted values 4 w/g(x) at sample points")
        plt.xlabel("x (m)")
        plt.ylabel("4 w/g(x)")
        plt.legend()
        plt.grid(True)

        plt.show()


    if PRINT_OUPUTS_FOR_PART_C:
        print("\nThis is part c")
        # For N = 200, what is your estimate of the percentage error for the small amplitude case? 
        time_period_N_is_200, x_200, w_200, integrands_200, weighted_200 = compute_integral_with_gauss(200, 0, x_0)
        fractional_error_N_is_200 = abs(time_period_N_is_200 - boring_time_period) / boring_time_period
        print(f"The time period for N = 200 is: {time_period_N_is_200}\
        This implies fractional error of: {fractional_error_N_is_200}")

        x_c = c * np.sqrt(m/k)
        x0_values = np.linspace(1.0, 10.0 * x_c, 100)  # points between 1 m and 10 x_c
        T_values = []

        for x0_val in x0_values:
            x_0 = x0_val
            T_val, _, _, _, _ = compute_integral_with_gauss(200, 0, x_0)
            T_values.append(T_val)

        # Classical limit: plot a constant line
        T_classical = boring_time_period * np.ones_like(x0_values)

        # Relativistic limit: from the document it tells us that  T --> 4 x_0/c
        T_relativistic = 4 * x0_values / c
        if PLOT_GRAPHS:
            plt.figure()
            plt.plot(x0_values, T_values, label="Numerical (Gauss, N=200)")
            plt.plot(x0_values, T_classical, "--", label="Classical limit")
            plt.plot(x0_values, T_relativistic, "--", label="Relativistic limit")
            plt.xlabel("$x_0$ (m)")
            plt.ylabel("Time period (s)")
            plt.title("Time Period vs Initial Amplitude")
            plt.legend()
            plt.grid(True)
            plt.show()


    if GET_LAB5_VALUES:
        # Extra code for help in Lab 5...
        print("ASDKLFAS;DFJASDFASFJLAKSDFJF")
        x_c = c * np.sqrt(m/k)

        x_0 = 1
        T_x1, _, _, _, _ = compute_integral_with_gauss(200, 0, 1)
        
        x_0 = x_c
        T_xxc, _, _, _, _ = compute_integral_with_gauss(200, 0, x_c)

        x_0 = 10*x_c
        T_x10xc, _, _, _, _ = compute_integral_with_gauss(200, 0, 10*x_c)

        print(T_x1)
        print(T_xxc)
        print(T_x10xc)

    print("----------END----------")


if __name__ == "__main__":
    main()