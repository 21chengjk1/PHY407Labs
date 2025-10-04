"""
Welcome to the Code for Lab 4 Question 3 part b in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab4
"""
import numpy as np
import matplotlib.pyplot as plt

from lab4_q3a import relaxation

# Global Variables used by f
c = 2
def f(x):
    return 1 - np.exp(-c * x)

def main():
    global c
    print("----------<PART_B>----------")
    # b)    Consider again the equation x = 1 - e^-cx that we solved in Exercise 6.10. Take
    #       the program you wrote for part (a) of that exercise, which solved the equation
    #       for the case c = 2, and modify it to print out the number of iterations it takes to
    #       converge to a solution accurate to 10- 6 .
    
    # Here, we're going to do mostly the same code as in part a
    c = 2
    x_list, iterations = relaxation(f, init_x=0.5, dx=1, threshold=1e-6)

    print(f"Solution for c=2: {x_list[-1]}")
    print(f"Number of iterations: {iterations}")

    # c)    Now write a new program (or modify the previous one) to solve the same equation 
    #       x = 1 - e-cx for c = 2, again to an accuracy of 10^-6, but this time using
    #       overrelaxation. Have your program print out the answers it finds along with the
    #       number of iterations it took to find them. Experiment with different values of
    #       w to see how fast you can get the method to converge. A value of w = 0.5 is
    #       a reasonable starting point. With some trial and error you should be able to get
    #       the calculation to converge at least twice as fast as the simple relaxation method,
    #       i.e., in about half as many iterations.
    c = 2
    threshold = 1e-6
    init_x = 0.5

    # Try different values of w
    for w in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        x = init_x
        dx = 1.0
        iterations = 0

        while dx > threshold:
            x_new = (1 + w) * f(x) - w * x  # overrelaxation update is : x' = (1 + w)*f(x) - wx as stated by the textbook
            dx = abs(x_new - x)
            x = x_new
            iterations += 1

        print(f"w={w:.1f} : Solution: {x:.6f}, Iterations: {iterations}")


    # d)    Are there any circumstances under which using a value w < 0 would help us
    #       find a solution faster than we can with the ordinary relaxation method? (Hint:The answer is yes, but why?)

    # The answer will be written in document.

    print("----------</PART_B>----------")


if __name__ == "__main__":
    main()