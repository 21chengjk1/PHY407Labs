"""
Welcome to the Code for Lab 5 Q1b in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab5
"""

import numpy as np
import matplotlib.pyplot as plt

    
def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 1b!")
    
    
    # The task is as follows:
    # TEXTBOOK 7.8, PAGE 321 (look for page 331 in the pdf)
    # Write a Python program that uses a fast Fourier transform to calculate the diffrac-
    # tion pattern for a grating with transmission function 
    # q(u) = sin^2 (alpha u) with slits of width 20 micrometre [meaning that alpha = pi/(20 mirco m)] and parameters
    # as above: 
    # w = 200 micro m, 
    # W = 10w = 2 mm, 
    # incident light of wavelength A = 500 nm, 
    # a lens with focal length of 1 meter, 
    # and a screen 10 cm wide. 
    #
    # Choose a suitable number of points to give a good approximation to the grating transmission function and then
    # make a graph of the diffraction intensity on the screen as a function of position x in the
    # range -5cm <= x <= 5cm.
    #
    # Intensity is given by I(x_k) = W^2 / N^2 |c_k|^2, where x_k = (lambda f/ W) * k
    # y_n will need to be padded out with 0s
    
    
    # CONSTANTS:
    alpha = np.pi / 20 / 10e-6



    N = 1000  # CHOOSE A SUITABLE NUMBER OF POINTS
    n = np.arange(N)
    y = np.sin(alpha * n)

    c = ...

    ...


    # Will need to hand in code and plots and explanatory notes
    print("----------END----------")

if __name__ == '__main__':
    main()