"""
Code for Lab 9 Question 3
"""

import numpy as np
import matplotlib.pyplot as plt

def lax_wendroff_step(u, N, beta):
    """One Lax–Wendroff step for Burgers' equation."""
    u_next = np.zeros_like(u)

    for i in range(N):
        ip = (i + 1) % N
        im = (i - 1) % N

        term1 = - (beta / 4.0) * (u[ip]**2 - u[im]**2)

        term2 = (beta**2 / 8.0) * (
            (u[i] + u[ip]) * (u[ip]**2 - u[i]**2)
            - (u[im] + u[i]) * (u[i]**2 - u[im]**2)
        )

        u_next[i] = u[i] + term1 + term2

    return u_next

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 9 Question 3!")

    # Code...

    # Parameters, same as Lab 8 Q3.
    eps = 1.0           
    dx = 0.02           
    dt = 0.005          # time step
    Lx = 2*np.pi        # domain length
    Tf = 2.0            # final time

    beta = eps * dt / dx

    # Grid
    x = np.arange(0, Lx, dx)
    N = len(x)

    # Initial condition from Lab 8 q3.
    u = np.sin(x)

    # Times at which to show plots
    plot_times = [0.0, 0.5, 1.0, 1.5]
    next_plot_index = 0

    t = 0.0

    # Time stepping loop
    plt.figure(1)
    while t <= Tf + 1e-12:
        # Plot if we reached a requested time
        if next_plot_index < len(plot_times) and abs(t - plot_times[next_plot_index]) < dt/2:
            plt.plot(x, u, label=f"t = {t:.2f}")
            next_plot_index += 1

        # Step forward in time
        u = lax_wendroff_step(u, N, beta)
        t += dt

    plt.title("Burgers Equation solutions: Lax–Wendroff")
    plt.xlabel("x")
    plt.ylabel("u")
    plt.grid(True)
    plt.legend()
    plt.show()
    print("----------END----------")


if __name__ == "__main__":
    main()
