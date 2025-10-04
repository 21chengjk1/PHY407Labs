"""
Welcome to the Code for Lab 4 Question 3 part b in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab4
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light, Planck, Boltzmann

from lab4_q3a import relaxation

SHOW_PLOTS = True

def f(x):
    """
    This is the function we want to solve: 0 = f(x) = 5e^{-x} + x - 5
    """
    return 5*np.exp(-x) + x - 5

def fprime(x):
    """
    This is the derivative of the function above.
    """
    return 1 - 5*np.exp(-x)

def g(x):
    """
    Rearrangement of f(x) = 0, it can be rewritten as x = 5(1 - e^-x) = g(x)
    """
    return 5 * (1 - np.exp(-x))


def binary_search(func, a, b, threshold):
    """
    Carries out the binary search method on a function func
    Returns x_list, the list of x values, and iterations.
    So the final guess should be at x_list[-1]
    """
    x_list = [0.5 * (a + b)]
    fa, fb = func(a), func(b)
    if fa * fb > 0:                                 # We should make sure that one is positive, and the other is negative.
        raise ValueError("Solution not bracketed")
    iterations = 0
    while (b - a) / 2 > threshold:
        mid = 0.5 * (a + b)                         # find the midpoint
        fm = func(mid)                              # evaluate the function at the midpoint
        iterations += 1
        if fa * fm <= 0:                            # If f(a) and f(mid) are opposite sides of the zero line
            b, fb = mid, fm                         # new range can be (a,mid)
            x_list.append(0.5 * (a + b))
        else:
            a, fa = mid, fm                         # If not, then it definitely works on the other side. new range can be (mid,b)
            x_list.append(0.5 * (a + b))
    return x_list, iterations


def newton(func, dfunc, x0, threshold):
    """
    Newtons method: x_n+1 = x_n - f(x_n)/f'(x_n)
    Returns x_list, the list of x values, and iterations.
    So the final guess should be at x_list[-1]
    """
    x_list = [x0]
    x = x0
    iterations = 0
    while True:
        x_new = x - func(x)/dfunc(x)
        iterations += 1
        x_list.append(x_new)
        if abs(x_new - x) < threshold:
            return x_list, iterations
        x = x_new


def main():
    print("----------<PART_C>----------")
    # Exercise 6.13: Wien's displacement constant
    # Planck's radiation law tells us that the intensity of radiation per unit area and per unit
    # wavelength lambda from a black body at temperature T is:
    # I(lambda) = (2 * pi * h * c^2 * lambda^-5) / ( exp( (hc) / (lambda * k_b * T) ) - 1 )
    # where h is Planck's constant, c is the speed of light, and k_b is Boltzmann's constant.
    # 
    # a) The wavelength lambda at which the emitted radiation is strongest is the solution of the equation
    # 5e ^( (hc) / (lambda * k_b * T) ) + h*c / (lambda * k_b * T) = 0.

    # And turns out that we can solve fox x in this equation, 5e^-x + x - 5 = 0.
    # and yield that b = h c / k_b x

        # NO CODE TO SUBMIT FOR PART A, JUST USE THE RESULT.

    # b) Write a program to solve this equation to an accuracy of  10- 6 using the
    # binary search method, and hence find a value for the displacement constant.
    # In addition to the binary search method, also try the relaxation and Newton’s
    # methods. Count the number of iterations each method takes and then
    # comment on their relative efficiencies.

    # Binary search
    x_binary_list, iter_binary = binary_search(f, 1, 7, threshold=1e-6)
    x_binary = x_binary_list[-1]

    # Relaxation. This takes f(x) = 0 rearraged to g(x) = x.
    x_relax_list, iter_relax = relaxation(g, init_x=4.0, dx=1, threshold=1e-6)
    x_relax = x_relax_list[-1]

    # Newton
    x_newton_list, iter_newton = newton(f, fprime, x0=4.0, threshold=1e-6)
    x_newton = x_newton_list[-1]

    h = Planck              # Planck's constant
    c = speed_of_light      # speed of light
    kB = Boltzmann          # Boltzmann constant

    # Displacement constant
    b_bisect = (h*c)/(kB*x_binary)
    b_relax  = (h*c)/(kB*x_relax)
    b_newton = (h*c)/(kB*x_newton)

    print(f"{'Method':<15}{'x':>12}{'Iterations':>15}{'b (mK)':>20}")
    print("-" * 62)
    print(f"{'Binary Search':<15}{x_binary:>12.6f}{iter_binary:>15}{b_bisect:>20.3e}")
    print(f"{'Relaxation':<15}{x_relax:>12.6f}{iter_relax:>15}{b_relax:>20.3e}")
    print(f"{'Newton':<15}{x_newton:>12.6f}{iter_newton:>15}{b_newton:>20.3e}")


    # c) The displacement law is the basis for the method of optical pyrometry, a method
    # for measuring the temperatures of objects by observing the color of the thermal
    # radiation they emit. The method is commonly used to estimate the surface temperatures 
    # of astronomical bodies, such as the Sun. The wavelength peak in the
    # Sun's emitted radiation falls at lambda = 502nm. From the equations above and your
    # value of the displacement constant, estimate the surface temperature of the Sun

    # Wien displacement law: lambda = b/T, so T = b/lambda.
    b = b_relax 
    lambda_sun = 502e-9     # 502 nm
    T = b / lambda_sun
    print(f"Using b from the relaxation method, estimate that T = {T:.0f} K")

    if SHOW_PLOTS:
        plt.figure()
        plt.title(r"Solve $0 = 5e^{-x} + x - 5$ with various methods")
        plt.plot(x_relax_list, label="Relaxation")
        plt.plot(x_binary_list, label="Binary Search")
        plt.plot(x_newton_list, label="Newton")
        plt.xlabel("Iteration number")
        plt.ylabel("Solution of x at iteration")
        plt.legend()
        plt.axvline(x=iter_relax,  color='blue',   linestyle='--')
        plt.axvline(x=iter_newton, color='green',  linestyle='--')
        plt.axvline(x=iter_binary, color='orange', linestyle='--')
        plt.grid()
        plt.show()


    print("----------</PART_C>----------")

if __name__ == "__main__":
    main()