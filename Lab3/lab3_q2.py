"""
Welcome to the Code for Lab 3 Question 2 in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab3
"""

import numpy as np
from util import gaussxw as gsx
from scipy.constants import speed_of_light

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

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 3 Question 2!")

    x_sample_values = []    # sample values x from gaussxw
    integrands = []         # integrands 4/g_k
    weighted_values = []    # weighted values 4 w_k/g_k

    # We want to test T = 4 * Integral from 0 to x_0 ( dx′ / g(x′) )
    # Let's first compute the "Boring value" = 2 * pi * sqrt( m / k )

    boring_time_period = 2 * np.pi * np.sqrt(m / k)
    print(f"The boring time period is: {boring_time_period}")

    # Now let's compute the for x_0 = 1cm to see if the relativistic value matches
    x_0 = 1e-2
    N = 8
    x, w = gsx.gaussxwab(N, 0, x_0)
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for i in range(N):
        I += w[i] * integrand(x[i])
    time_period_N_is_8 = 4 * I
    # print
    fractional_error_N_is_8 = abs(time_period_N_is_8 - boring_time_period) / boring_time_period
    print(f"The time period for N = 8 is: {time_period_N_is_8}\
    This implies fractional error of: {fractional_error_N_is_8}")

    print("Here's the values x after N = 8")
    print(x)
    x_sample_values.extend(x)

    N = 16
    x, w = gsx.gaussxwab(N, 0, x_0)
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for i in range(N):
        I += w[i] * integrand(x[i])
    time_period_N_is_16 = 4 * I
    # print
    fractional_error_N_is_16 = abs(time_period_N_is_16 - boring_time_period) / boring_time_period
    print(f"The time period for N = 8 is: {time_period_N_is_16}\
    This implies fractional error of: {fractional_error_N_is_16}")

    print("Here's the values x after N = 16")
    print(x)
    x_sample_values.extend(x)



    print("----------END----------")


if __name__ == "__main__":
    main()