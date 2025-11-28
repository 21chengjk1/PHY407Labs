"""
Code for Lab 11 Question 1
"""
import random
from math import exp,pi
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import random

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
    plt.bar(n_vals, energy_frequency, width=0.1)

    plt.show()

    

    print("----------END----------")

def main2():
    # I was confused and asked Gemini for help
    # --- Parameters ---
    kBT = 10.0  # Temperature (as requested)
    L = 1
    N = 1000
    steps = 100000

    # --- Initialization ---
    # Create a 2D array to store the quantum numbers (nx, ny, nz)
    # Start all particles at n=1 (ground state)
    n = np.ones([N, 3], int)

    # Initial Energy Calculation
    # E = sum of (nx^2 + ny^2 + nz^2) * constants
    # We neglect constants for the simulation steps to make it faster,
    # but the formula provided includes them.
    E = 3 * N * np.pi**2 / (2 * L**2)
    eplot = []

    print("Starting simulation...")

    # --- Main Monte Carlo Loop ---
    for k in range(steps):
        if k % 10000 == 0:
            print(f"Step {k}/{steps}...")

        # 1. Choose a random particle (i) and a random direction x,y,z (j)
        i = random.randrange(N)
        j = random.randrange(3)

        # 2. Decide move direction (up or down)
        if random.random() < 0.5:
            dn = 1
            dE = (2 * n[i, j] + 1) * np.pi**2 / (2 * L**2)
        else:
            dn = -1
            dE = (-2 * n[i, j] + 1) * np.pi**2 / (2 * L**2)

        # 3. Metropolis Step: Decide whether to accept the move
        # We reject moves if n would go below 1 (n[i,j] > 1 check handles the boundary)
        if n[i, j] > 1 or dn == 1:
            # If dE < 0, exp(-dE/T) > 1, so we always accept (random < 1 is always true)
            # If dE > 0, we accept with probability exp(-dE/T)
            if random.random() < np.exp(-dE / kBT):
                n[i, j] += dn
                E += dE

        eplot.append(E)

    # --- Plot 1: Energy vs. Time ---
    plt.figure(1)
    plt.plot(eplot)
    plt.title(f"Energy vs Time (T={kBT})")
    plt.xlabel("Monte Carlo Steps")
    plt.ylabel("Total Energy")
    plt.ticklabel_format(style="plain")
    plt.grid(True)

    # --- Plot 2: Frequency Distribution ---
    # This calculates the dimensionless energy of each particle (proportional to n^2)
    energy_n = n[:, 0]**2 + n[:, 1]**2 + n[:, 2]**2

    # We need a temporary histogram to get the frequency data
    plt.figure(2)
    # The code you provided creates a histogram of energy_n
    hist_output = plt.hist(energy_n, bins=50)
    plt.title("Raw Energy Histogram (Hidden)")
    # We don't actually need to show this plot, but plt.hist draws it automatically.

    # Extract data for the final plot
    energy_frequency = hist_output[0]  # The Y-axis (counts)
    bin_edges = hist_output[1]         # The X-axis edges

    # Calculate the center of each bin
    energy_vals = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    # Convert Energy coordinates to 'n' coordinates
    # Since E ~ n^2, then n ~ sqrt(E)
    n_vals = energy_vals**0.5

    # Create the final desired plot
    plt.figure(3)
    plt.bar(n_vals, energy_frequency, width=0.2, edgecolor='black')
    plt.title(f"Frequency Distribution vs n (T={kBT})")
    plt.xlabel("Magnitude of n vector")
    plt.ylabel("Frequency (Number of particles)")
    plt.grid(True, alpha=0.3)

    plt.show()


if __name__ == "__main__":
    # main2()
    main()
