"""
Lab 2 Question 3
"""
import numpy as np
from scipy.constants import epsilon_0
from scipy.special import k0
import matplotlib.pyplot as plt

def simpson(x, y):
    """
    Simpson's rule is : 
    (deltax / 3) * ( y(x_first) 
                    + 4 * (sum of y(x_odds)) 
                    + 2 * (sum of y(x_even))
                    + y(x_last) ) 


    """
    n = len(x) - 1
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of subintervals (odd number of points).")

    deltax = (x[-1] - x[0]) / n
    sum = y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2])
    return (deltax/3) * sum


def function(u, Q, l, r, z, eps0):
    return (Q * np.exp(-(np.tan(u))**2)) / (
        4*np.pi*eps0 * (np.cos(u)**2) * np.sqrt((z - l*np.tan(u))**2 + r**2)
    )


def V_simpson(r, z, Q, l, n):
    x = np.linspace(-np.pi/2, np.pi/2, n+1)
    y = function(x, Q, l, r, z, epsilon_0)
    return simpson(x, y)


def V_exact(r, Q, l):
    return (Q / (4*np.pi*epsilon_0*l)) * np.exp(r**2/(2*l**2)) * k0(r**2/(2*l**2))


def main():
    print("----------START----------")
    print("Hi! Let's do some Simpson's rule stuff.")

    # Parameters
    Q = 1e-13
    l = 1e-3
    z = 0
    
    r_values = np.linspace(0.25e-3, 5e-3, 100)  # 0.25 mm to 5 mm
    n = 50                                      # must be even (adjust this number until the y axis is ~10^-6   )

    V_by_simpson = [V_simpson(r, z, Q, l, n) for r in r_values]
    V_by_exact = [V_exact(r, Q, l) for r in r_values]

    plt.figure()
    plt.plot(r_values*1e3, V_by_simpson, label="Simpson (Eq. 8)")
    plt.plot(r_values*1e3, V_by_exact, label="Exact (Eq. 9)")
    plt.xlabel("r (mm)")
    plt.ylabel("V(r, 0)")
    plt.legend()
    plt.title("V(r,0): Numerical vs Exact")
    plt.show()

    plt.figure()
    diff = abs(np.array(V_by_simpson) - np.array(V_by_exact))
    frac_error = diff / np.array(V_by_exact)
    plt.plot(r_values*1e3, frac_error)
    plt.xlabel("r (mm)")
    plt.ylabel("Fractional error")
    plt.title(f"Fractional error (N={n})")
    plt.show()


    # -----------Part b----------------

    # r and z grids (units: meters)
    r_min = 0.25e-3
    r_max = 5e-3
    z_min = -5e-3
    z_max = 5e-3

    # Choose grid resolution (start moderate; increase if needed)
    Nr = 140   # try 140 or 150 for good resolution
    Nz = 160

    r_vals = np.linspace(r_min, r_max, Nr)
    z_vals = np.linspace(z_min, z_max, Nz)

    # Precompute u grid once for speed if you want (but current pointwise function recomputes)
    # Compute V on the (r,z) grid (this is the slow loop)
    V = np.zeros((Nz, Nr))  # V[z_index, r_index] for easier plotting with imshow/contour

    for i, z in enumerate(z_vals):
        for j, r in enumerate(r_vals):
            V[i, j] = V_simpson(r, z, Q, l, n)

    # --- Plot contours ---
    R_mm = r_vals * 1e3   # convert to mm for axis
    Z_mm = z_vals * 1e3
    Rg, Zg = np.meshgrid(R_mm, Z_mm)  # shapes (Nz, Nr)

    fig, ax = plt.subplots()
    levels = 20
    cs = ax.contourf(Rg, Zg, V, levels=levels)
    cbar = fig.colorbar(cs)
    cbar.set_label("V (volts)")
    # draw labeled contour lines on top
    cl = ax.contour(Rg, Zg, V, levels=8, colors='k', linewidths=0.5)
    ax.clabel(cl, fmt="%.2e")
    ax.set_xlabel("r (mm)")
    ax.set_ylabel("z (mm)")
    ax.set_title("Potential V(r,z) (contours)")

    plt.tight_layout()
    plt.show()

    print("----------END----------")

if __name__ == "__main__":
    main()