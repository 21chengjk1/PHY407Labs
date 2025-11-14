"""
Code for Lab 9 Question 1
"""

import numpy as np
import matplotlib.pyplot as plt
from dcst import dst, idst

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 9 Question 1!")

    # -----------------------------------------------------------
    # Problem parameters (same as Lab08 Q2)
    # -----------------------------------------------------------
    L = 1.0
    v = 100.0
    C = 1.0
    d = 0.1
    sigma = 0.3

    N = 300                             # number of Fourier modes
    x = np.linspace(0, L, N+1)

    # -----------------------------------------------------------
    # Initial displacement
    # -----------------------------------------------------------
    def phi0(x):
        return C * x * (L - x) / L**2 * np.exp(-(x - d)**2 / (2 * sigma**2))

    phi_initial = phi0(x)

    # -----------------------------------------------------------
    # Compute the DST of φ0(x)
    # dst() expects indexing starting at 1 and y[0] = 0
    # -----------------------------------------------------------
    phi_for_dst = phi_initial.copy()
    phi_for_dst[0] = 0.0       # ensure Dirichlet BC

    phi0_tilde = dst(phi_for_dst)    # Fourier sine coefficients

    # -----------------------------------------------------------
    # Frequencies ω_k = v * kπ / L
    # -----------------------------------------------------------
    k = np.arange(N+1)
    omega_k = v * k * np.pi / L

    # -----------------------------------------------------------
    # Function computing φ(x,t) using truncated Fourier series
    # -----------------------------------------------------------
    def phi_xt(t):
        # A_k(t) = φ̃_{0,k} cos(ω_k t)
        A = phi0_tilde * np.cos(omega_k * t)

        # reconstruct φ(x,t) using inverse DST
        phi_xt = idst(A)

        return phi_xt

    # -----------------------------------------------------------
    # Times to plot (in seconds)
    # -----------------------------------------------------------
    times = np.array([2e-3, 4e-3, 6e-3, 12e-3, 100e-3])

    # -----------------------------------------------------------
    # Plotting
    # -----------------------------------------------------------
    plt.figure(figsize=(10,6))

    for t in times:
        phi_t = phi_xt(t)
        plt.plot(x, phi_t, label=f"t = {t*1000:.0f} ms")

    plt.xlabel("x (m)")
    plt.ylabel("φ(x,t)")
    plt.title("String displacement using truncated sine series and DST")
    plt.legend()
    plt.grid(True)
    plt.show()

    print("----------END----------")


if __name__ == "__main__":
    main()
