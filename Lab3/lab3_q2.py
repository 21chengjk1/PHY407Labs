"""
Welcome to the Code for Lab 3 Question 2 in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab3
:)
"""

import numpy as np
from util import gaussxw as gsx

# List of Constants used by g(x)
c = ...
k = ...
m = ...

def g(x):
    dividend = ...
    divisor = ...
    quotient = dividend / divisor
    return c * np.sqrt(quotient)


def main():
    print("----------START----------")
    print("Hi!")
    
    # We want to test T = 4 * Integral from 0 to x_0 ( dx′ / g(x′) )

    N = 8
    x, w = gsx.gaussxw(N)
    # initialize integral to 0.
    I = 0.
    # loop over sample points to compute integral
    for k in range(N):
        I += w[k] * g(x[k])
    # print
    print(I)

    N = 16

    print("----------END----------")


if __name__ == "__main__":
    main()