"""
Code for Lab 7 Question 2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import elementary_charge, electron_mass, hbar


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

    e = elementary_charge       # e = 1.6e-19 Coulomb
    m = electron_mass           # m = 9.1e-31 kg
    h_bar = hbar

    V_0 = 50 * e                # 50eV --> 50 * e Joules
    a = 1e-11                   # 10 ** -11 == 1 * 10**-11 = 1e-11

    x_0 = -10 * a   # x = -10a to 10a
    x_f = 10 * a    

    N = 1000        # N Steps
    h = (x_f - x_0) / N

    def V_parta():
        """
        
        """
        return 

    def f(r,x,E, V=V_parta):
        psi = r[0]
        phi = r[1]
        fpsi = phi
        fphi = (2*m/hbar**2)*(V(x)-E)*psi
        return np.array([fpsi,fphi],float)

    def solve(E):
        psi = 0.0
        phi = 1.0
        r = np.array([psi,phi],float)
        for x in np.arange(x_0,x_f,h):
            k1 = h*f(r,x,E)
            k2 = h*f(r+0.5*k1,x+0.5*h,E)
            k3 = h*f(r+0.5*k2,x+0.5*h,E)
            k4 = h*f(r+k3,x+h,E)
            r += (k1+2*k2+2*k3+k4)/6
        return r[0]


    # b) Now modify your program to calculate the same three energies for the 
    # anharmonic oscillator with V(x) = V_0 x^4 /a^4, with the same parameter values. 


    # c) Modify your program further to calculate the properly normalized wavefunctions 
    # of the anharmonic oscillator for the three states and make a plot of them, 
    # all on the same axes, as a function of x over a modest range near the origin-say 
    # x = -5a to x = 5a


    print("----------END----------")


if __name__ == "__main__":
    main()