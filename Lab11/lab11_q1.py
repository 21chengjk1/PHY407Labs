"""
Code for Lab 11 Question 1
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 11 Question 1!")


    # Part 1 (code provided by Question Instructions)


    
    # This calculates the energy of each particle, neglecting constant factors
    energy_n = n[:, 0]**2 + n[:, 1]**2 + n[:, 2]**2
    # This calculates the frequency distribution and creates a plot
    plt.figure(2)
    plt.clf()
    hist_output = plt.hist(energy_n, 50)
    # This is the frequency distribution
    energy_frequency = hist_output[0]
    # This is what the x-axis of the plot should look like
    # if we plot the energy distribution as a function of n
    # the 2nd axis of hist_output contains the boundaries of the array.
    # Instead, we want their central value, below.
    energy_vals = 0.5*(hist_output[1][:-1] + hist_output[1][1:])
    n_vals = energy_vals**0.5
    # Create the desired plot
    plt.figure(3)
    plt.clf()
    plt.bar(n_vals, energy_frequency, width=0.1)

    print("----------END----------")


if __name__ == "__main__":
    main()
