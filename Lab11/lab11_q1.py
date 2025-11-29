"""
Code for Lab 11 Question 1
"""
import random
from math import exp,pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x, m, c):
    """
    return y = mx + c
    """
    return m * x + c

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 11 Question 1!")


    # Part 1 (code provided by Question Instructions)

    # Code from Newmann Textbook: mcsim.py
    T = 10.0
    L = 1
    N = 1000
    steps = 100000

    # Create a 2D array to store the quantum numbers
    n = np.ones([N,3],int)

    # Main loop
    eplot = []
    E = 3*N*pi*pi/(2*L*L)
    for k in range(steps):
        if k % 10000 == 0:
            print(f"Step {k}/{steps}...")

        # Choose the particle and the move
        i = random.randrange(N)
        j = random.randrange(3)
        if random.random() < 0.5:
            dn = 1
            dE = (2*n[i,j]+1)*pi*pi/(2*L*L)
        else:
            dn = -1
            dE = (-2*n[i,j]+1)*pi*pi/(2*L*L)

        # Decide whether to accept the move
        if n[i,j]>1 or dn==1:
            if random.random() < exp(-dE/T):
                n[i,j] += dn
                E += dE

        eplot.append(E)

    # Make the graph
    plt.plot(eplot)
    plt.title("Quantum ideal gas in a box: Energy vs. Time plot.")
    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.ticklabel_format(style="plain")
    plt.show()


    # And here is code from the question instructions.
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
    plt.title("Distribution of Quantum Numbers After Equilibrium")
    plt.xlabel("Quantum number n")
    plt.ylabel("Frequency") 
    plt.bar(n_vals, energy_frequency, width=0.1)

    plt.show()

    
    # ---------------------------------------------------------
    # Part 2 — Compute E(T) and n(T) for different temperatures
    # ---------------------------------------------------------
    print("\n--- Calculating E(T) and n(T) over various temperatures ---")

    temps = [10, 40, 100, 400, 1200, 1600]
    steps_list = [100000, 200000, 400000, 800000, 3000000, 3500000]
    # steps_list = [100000, 100000, 100000, 100000, 100000, 100000]

    N = 1000
    L = 1
    pi2 = pi * pi

    # storage
    avg_E = []
    avg_n = []

    for T, steps in zip(temps, steps_list):
        print(f"\nRunning simulation at T = {T} ...")

        burn_in = steps // 2   # discard early nonequilibrated samples

        n_vals_list = []
        later_E_vals = []
        E_vals = []

        # initial state
        n = np.ones([N, 3], int)
        E = 3*N*pi2/(2*L*L)

        for k in range(steps):
            if k % 100000 == 0:
                print(f"    Step {k}/{steps}...")

            # Monte Carlo move
            i = random.randrange(N)
            j = random.randrange(3)

            if random.random() < 0.5:
                dn = 1
                dE = (2*n[i,j] + 1)*pi2/(2*L*L)
            else:
                dn = -1
                dE = (-2*n[i,j] + 1)*pi2/(2*L*L)

            if n[i,j] > 1 or dn == 1:
                if random.random() < exp(-dE/T):
                    n[i,j] += dn
                    E += dE

            E_vals.append(E)

            # Record after burn-in
            if k > burn_in:
                # compute n magnitude for each particle
                n_mag = np.sqrt(n[:,0]**2 + n[:,1]**2 + n[:,2]**2)
                n_vals_list.append(np.mean(n_mag))
                later_E_vals.append(E)

        # Averages at this temperature
        avg_n_T = np.mean(n_vals_list)
        avg_E_T = np.mean(later_E_vals)

        avg_n.append(avg_n_T)
        avg_E.append(avg_E_T)

        plt.figure()
        plt.title(f"T = {T}")
        plt.plot(E_vals)
        plt.xlabel("Time")
        plt.ylabel("Energy")
        plt.axvline(x=burn_in, color='r', linestyle='--', linewidth=2)
        plt.ticklabel_format(style="plain")

        print(f"  <n> = {avg_n_T:.3f},   <E> = {avg_E_T:.3f}")


    plt.show()  # Show all the plots of E against Time.

    x_values = temps
    y_values = avg_E
    p_opt, p_cov = curve_fit(linear, x_values, y_values)

    m_fit, c_fit = p_opt
    print("Fitted slope m =", m_fit)
    print("Fitted intercept c =", c_fit)

    # -----------------------
    # Plot E(T) and n(T)
    # -----------------------
    plt.figure()
    plt.plot(temps, avg_E, marker='o', ls='', label='Energy after equilibrium')
    x_linspace = np.linspace(min(x_values), max(x_values), 100)
    plt.plot(x_linspace, linear(x_linspace, m_fit, c_fit), label="linear fit", linestyle="--")
    plt.xlabel("Temperature T")
    plt.ylabel("E")
    plt.title("Total Energy vs Temperature")
    plt.legend()
    plt.grid(True)

    plt.figure()
    plt.plot(temps, avg_n, marker='o')
    plt.xlabel("Temperature T")
    plt.ylabel(r"$\overline{n}$")
    plt.title(r"Average quantum number $\overline{n}$ vs Temperature")
    plt.grid(True)
    plt.show()

    print("----------END----------")


if __name__ == "__main__":
    main()
