"""
Code for Lab 7 Question 2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import elementary_charge, electron_mass, hbar

PART_B = True

def simpson(x, y, n):
    sum = 0 
    deltax = (x[len(x)-1] -x[0])/n

    sum += np.sum(y[1:len(x)-1:2])*4
    sum += np.sum(y[2:len(x)-1:2])*2
    sum += y[0]
    sum += y[len(x)-1]
    return (deltax/3)*sum

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 7 Question 2!")

    # Consider the one-dimensional, time-independent Schrodinger equation in a harmonic 
    # (i.e., quadratic) potential V(x) = V_0 x^2/a^2, where V0 and a are constants. 
    
    # a) Find the energies of the ground state and the first two excited states for these equations when m is the electron 
    # mass, V_0 = 50eV, and a = 10^-11 m.
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

    def V_parta(x):
        """
        The V for part a of the question
        V(x) = V_0 x^2 / a^2
        """
        return V_0 * (x ** 2) / (a ** 2)
    
    def V_partb(x):
        """
        The V for part b of the question
        V(x) = V_0 x^2 / a^2
        """
        return V_0 * (x ** 4) / (a ** 4)

    def f(r,x,E):

        V = V_parta
        if PART_B:
            V = V_partb

        psi = r[0]
        phi = r[1]
        fpsi = phi
        fphi = (2*m/h_bar**2)*(V(x)-E)*psi
        return np.array([fpsi,fphi],float)

    def solve(E):
        """
        This comes from squarewell.py. 
        It does...
        """
        psi = 0.0
        phi = 1.0
        r = np.array([psi,phi],float)
        wave_function = []
        for x in np.arange(x_0,x_f,h):
            wave_function.append(r[0])
            k1 = h*f(r,x,E)
            k2 = h*f(r+0.5*k1,x+0.5*h,E)
            k3 = h*f(r+0.5*k2,x+0.5*h,E)
            k4 = h*f(r+k3,x+h,E)
            r += (k1+2*k2+2*k3+k4)/6
        return np.array(wave_function, float), r[0]
    
    def find_energy_shooting(E1_guess, E2_guess):
        E1 = E1_guess
        E2 = E2_guess
        wave_function, psi2 = solve(E1)
        target = e / 1000   # some target accuracy.
        while abs(E2 - E1) > target:
            psi1 = psi2
            wave_function, psi2 = solve(E2)
            E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)
        
        wave_function, _ = solve(E2)
        # Use simpson's rule to get the integral
        x_vals = np.arange(x_0, x_f, h)
        mod_squared = wave_function ** 2

        # Take only left half
        half_mask = x_vals <= 0
        x_half = x_vals[half_mask]
        y_half = mod_squared[half_mask]

        # n should be even for Simpson’s rule
        n = len(x_half) - 1
        if n % 2 != 0:
            n -= 1
            x_half = x_half[:n+1]
            y_half = y_half[:n+1]

        integral_half = simpson(x_half, y_half, n)
        integral = 2 * integral_half

        return E2, wave_function/np.sqrt(integral)


    # GOOD BOUNDS FOR PART A
    E_guesses = [
        (100 * e, 150 * e),   # ground state
        (200 * e, 450 * e),   # 1st excited
        (450 * e, 700 * e)    # 2nd excited
    ]


    if PART_B:
        # GOOD BOUNDS FOR PART B
        E_guesses = [
            (0 * e, 200 * e),   # ground state
            (300 * e, 800 * e),   # 1st excited
            (900 * e, 1500 * e)    # 2nd excited
        ]

    
    E1, E2 = E_guesses[0]
    E_0, psi0 = find_energy_shooting(E1, E2)

    E1, E2 = E_guesses[1]
    E_1, psi1 = find_energy_shooting(E1, E2)

    E1, E2 = E_guesses[2]
    E_2, psi2 = find_energy_shooting(E1, E2)

    print(f"State 0: E = {E_0 / e:.3f} eV")
    print(f"State 1: E = {E_1 / e:.3f} eV")
    print(f"State 2: E = {E_2 / e:.3f} eV")


    difference = (E_2/e-E_1/e) - (E_1/e - E_0/e)
    print(f"(E2 - E1) - (E1 - E0) = {difference:.3g}")

    # b) Now modify your program to calculate the same three energies for the 
    # anharmonic oscillator with V(x) = V_0 x^4 /a^4, with the same parameter values. 

        # NOTE: just change the True/False value called PART_B to see changes for part B.

    # c) Modify your program further to calculate the properly normalized wavefunctions 
    # of the anharmonic oscillator for the three states and make a plot of them, 
    # all on the same axes, as a function of x over a modest range near the origin-say 
    # x = -5a to x = 5a

    # Create x-values and trim to -5a to 5a
    x_vals = np.arange(x_0, x_f, h)
    mask = (x_vals >= -5 * a) & (x_vals <= 5 * a)
    x_trim = x_vals[mask]

    # Plot the wavefunctions
    plt.figure(1)
    plt.plot(x_trim, psi0[mask] / np.max(np.abs(psi0[mask])), label=r"$\psi_0$ (ground state)")
    plt.plot(x_trim, psi1[mask] / np.max(np.abs(psi1[mask])), label=r"$\psi_1$ (1st excited)")
    plt.plot(x_trim, psi2[mask] / np.max(np.abs(psi2[mask])), label=r"$\psi_2$ (2nd excited)")

    plt.title("Normalized Wavefunctions for Oscillator" + (" (Anharmonic)" if PART_B else ""))
    plt.xlabel(r"$x/a$")
    plt.ylabel(r"Normalized $\psi(x)$")
    plt.grid(True)
    plt.tight_layout()

    if not PART_B:
        omega = np.sqrt(2 * V_0 / (m * a ** 2))
        alpha = m * omega / h_bar

        y = np.sqrt(alpha) * x_trim

        norm_factor = (alpha / np.pi) ** 0.25

        phi0 = norm_factor * np.exp(-y ** 2 / 2)
        phi1 = norm_factor * np.sqrt(2) * y * np.exp(-y ** 2 / 2)
        phi2 = norm_factor * (1 / np.sqrt(2)) * (2 * y ** 2 - 1) * np.exp(-y ** 2 / 2)

        # Scale analytical curves for visual comparison (same amplitude range)
        phi0 /= np.max(np.abs(phi0))
        phi1 /= np.max(np.abs(phi1))
        phi2 /= np.max(np.abs(phi2))

        plt.plot(x_trim, phi0       , 'b--', label=r"Analytic $\phi_0$")
        plt.plot(x_trim, phi1 * -1  , 'r--', label=r"Analytic $\phi_1$")    # It was flipped but I think it doesn't actually matter since probabilities would be the same anyways
        plt.plot(x_trim, phi2       , 'y--', label=r"Analytic $\phi_2$")

    plt.legend()
    plt.show()


    print("----------END----------")


if __name__ == "__main__":
    main()