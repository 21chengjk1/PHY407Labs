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
    # b)    With the equation x = 1 - e^-cx in part a, output the number of iterations.
    
    # Here, we're going to do mostly the same code as in part a. 
    # Imported the method from part a which properly modified to count iterations.
    c = 2
    x_list, iterations = relaxation(f, init_x=0.5, dx=1, threshold=1e-6)

    print(f"Solution for c=2: {x_list[-1]}")
    print(f"Number of iterations: {iterations}")

    # c)    solve the same equation again to an accuracy of 10^-6, but this time using
    #       overrelaxation. 
    #       Have your program print out the answers it finds along with the
    #       number of iterations it took to find them. 
    #       Try multiple values of w.
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

    print("----------</PART_B>----------")


if __name__ == "__main__":
    main()