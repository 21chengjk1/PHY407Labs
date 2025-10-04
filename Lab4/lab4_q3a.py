"""
Welcome to the Code for Lab 4 Question 3 part a in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab4
"""
import numpy as np
import matplotlib.pyplot as plt

SHOW_PLOTS = True

# Global Variables used by f
c = 2
def f(x):
    """
    Relaxation solves for x = f(x). This function defines that f(x)
    """
    return 1 - np.exp(-c * x)

def relaxation(func, init_x, dx, threshold):
    """
    Carries out the relaxation method on a function func
    Returns
    : x_list, the list of x values. The final guess should be at x_list[-1]
    : iterations, the number of iterations it took to find an answer within the threshold.
    """
    iterations = 0
    x_list = [init_x] 
    while dx > threshold:
        x_list.append(func(x_list[-1]))
        dx = np.abs(x_list[-1] - x_list[-2])
        iterations += 1

    return x_list, iterations

def main():
    global c
    print("----------<PART_A>----------")
    # Consider the equation x = 1 - e^-cx, where c is a known parameter and x is unknown.
    #
    # a)    Write a program to solve this equation for x using the relaxation method for the
    #       case c = 2. Calculate your solution to an accuracy of at least 10^-6 

    x_list, _ = relaxation(f, init_x=0.5, dx=1, threshold=1e-6)
    print("Estimate for solution to x = 1 - e^-cx. x =", x_list[-1])

    if SHOW_PLOTS:
        plt.figure()
        plt.title(r"Solve $x = 1 - e^{-cx}$ with relaxation method")
        plt.plot(x_list)
        plt.xlabel("Iteration number")
        plt.ylabel(r"Solution to $x = 1 - e^{-cx}$")
        plt.grid()
        plt.show()

    # b)    Modify your program to calculate the solution for values of c from 0 to 3 in steps
    #       of 0.01 and make a plot of x as a function of c. You should see a clear transition
    #       from a regime in which x = 0 to a regime of nonzero x. This is another example of 
    #       a phase transition.
    
    c_values = np.arange(0, 3.01, 0.01)
    x_values = []

    for some_c in c_values:
        c = some_c
        x_list, _ = relaxation(f, init_x=0.5, dx=1, threshold=1e-6)
        x = x_list[-1]          # The final value in x_list is the estimated solution to x.
        x_values.append(x)

    # Plot result
    if SHOW_PLOTS:
        plt.figure()
        plt.title(r"Phase transition: Solution of $x = 1 - e^{-cx}$")
        plt.plot(c_values, x_values, label="Solution")
        plt.xlabel(r"$c$")
        plt.ylabel(r"Solution $x$")
        plt.legend()
        plt.grid()
        plt.show()


    # HAND IN YOUR PLOT
    print("----------</PART_A>----------")


if __name__ == "__main__":
    main()