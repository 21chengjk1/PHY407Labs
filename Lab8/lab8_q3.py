"""
Code for Lab 8 Question 3
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 8 Question 3!")

    # --- Parameters ---
    eps = 1.0
    dx = 0.02
    dt = 0.005
    Lx = 2 * np.pi     # domain length
    Tf = 2.0           # final time

    beta = eps * dt / dx

    # Define Nx, Nt
    Nx = int(Lx / dx) + 1
    Nt = int(Tf / dt)

    x = np.linspace(0, Lx, Nx)
    u = np.zeros((Nt, Nx))

    # Initial conditions and boundary conditions
    u[0, :] = np.sin(x)
    u[0, 0] = 0
    u[0, -1] = 0

    # Apply the first step.
    for i in range(1, Nx - 1):
        u[1, i] = u[0, i] - (beta / 2.0) * ((u[0, i + 1])**2 - (u[0, i - 1])**2)

    u[1, 0] = 0
    u[1, -1] = 0

    # Apply the leapfrog rule in the loop.
    for j in range(1, Nt - 1):
        for i in range(1, Nx - 1):
            u[j + 1, i] = u[j - 1, i] - (beta / 2.0) * ((u[j, i + 1])**2 - (u[j, i - 1])**2)

        # Apply boundary conditions
        u[j + 1, 0] = 0
        u[j + 1, -1] = 0

    # Plot at some specific times
    times_to_plot = [0, 0.5, 1.0, 1.5]
    plt.figure(1)

    for time in times_to_plot:
        j = int(time / dt)
        plt.plot(x, u[j, :], label=f"t = {time}")

    plt.xlabel("x")
    plt.ylabel("u(x, t)")
    plt.title("Solutions to Burgers' Equation")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("----------END----------")

if __name__ == "__main__":
    main()
