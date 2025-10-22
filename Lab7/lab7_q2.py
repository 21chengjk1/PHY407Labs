"""
Code for Lab 7 Question 2
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 7 Question 2!")

    # Consider the one-dimensional, time-independent Schrodinger equation in a harmonic 
    # (i.e., quadratic) potential V(x) = V_0 x^2/a^2, where V0 and a are constants. 
    
    # a) Write down the Schrodinger equation for this problem and convert it from a 
    # second-order equation to two first-order ones, as in Example 8.9. 
    # Write a program, or modify the one from Example 8.9, to find the energies of the ground 
    # state and the first two excited states for these equations when m is the electron 
    # mass, V_0 = 50eV, and a = 10^-11 m. Note that in theory the wavefunction goes 
    # all the way out to x = ±oo (infinity), but you can get good answers by using a large but 
    # finite interval. Try using x = - 10a to + 10a, with the wavefunction psi = 0 at both 
    # boundaries. (In effect, you are putting the harmonic oscillator in a box with impenetrable walls.) The wavefunction is real everywhere, so you don't need to use 
    # complex variables, and you can use evenly spaced points for the solution-there 
    # is no need to use an adaptive method for this problem. 
    # The quantum harmonic oscillator is known to have energy states that are 
    # equally spaced. Check that this is true, to the precision of your calculation, for 
    # your answers. (Hint: The ground state has energy in the range 100 to 200eV.) 


    # b) Now modify your program to calculate the same three energies for the 
    # anharmonic oscillator with V(x) = V_0 x^4 /a^4, with the same parameter values. 


    # c) Modify your program further to calculate the properly normalized wavefunctions 
    # of the anharmonic oscillator for the three states and make a plot of them, 
    # all on the same axes, as a function of x over a modest range near the origin-say 
    # x = -5a to x = 5a


    print("----------END----------")


if __name__ == "__main__":
    main()