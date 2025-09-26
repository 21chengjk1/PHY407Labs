"""
Welcome to the Code for Lab 3 Question 3 in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab3
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

ADD_CENTRAL_DIFFERENCE_SCHEME = True

def f(x):
    return np.exp(-x ** 2)

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 3 Question 3!")

    h_values = [10 ** i for i in range(-16, 1)]
    numerical_derivatives = []

    x = 0.5
    for h in h_values:
        d = ( f(x + h) - f(x) ) / h
        numerical_derivatives.append(d)

    central_numerical_derivatives = []
    for h in h_values:
        cd = ( f(x + h) - f(x - h) ) / (2 * h)
        central_numerical_derivatives.append(cd)

    # The actual value of f'(0.5) ~ -0.778800783071, or −2x * e^(−x^2)

    analytic_derivative = -2 * x * np.exp(-x ** 2)

    print(f"The analytic value is −2x * e^(−x^2), or {analytic_derivative} at x = 0.5")

    abs_errors = [abs(d - analytic_derivative) for d in numerical_derivatives]
    abs_errors_central = [abs(cd - analytic_derivative) for cd in central_numerical_derivatives]

    print("\n")
    # Print a table showing columns of h, numerical derivative, and absolute error
    print(f"{'h':>12} {'Numerical Derivative':>25} {'Absolute Error':>25}")
    print("-" * 65)
    for h, d, e in zip(h_values, numerical_derivatives, abs_errors):
        print(f"{h:12.1e} {d:25.15e} {e:25.15e}")

    # Plot error vs h on a log-log scale
    plt.figure()
    plt.plot(h_values, abs_errors, marker="o")
    if ADD_CENTRAL_DIFFERENCE_SCHEME:
        plt.plot(h_values,  abs_errors_central, marker="o")
    plt.xscale('log')  # Set the y-axis to a logarithmic scale
    plt.yscale('log')  # Set the y-axis to a logarithmic scale
    plt.xlabel("Step size h")
    plt.ylabel("Absolute error")
    plt.title("Error in numerical derivative vs step size")
    plt.grid(True)
    plt.xticks(h_values)
    plt.show()

    print("----------END----------")


if __name__ == "__main__":
    main()