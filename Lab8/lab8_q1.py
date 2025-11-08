"""
Code for Lab 8 Question 1
"""

import numpy as np
import matplotlib.pyplot as plt

ANIMATE = True

def init_boundary_conditions(phi):
    # AB: y = 0, x in [0, 50], T from 0 → 5
    for x in range(0, 51):
        phi[x, 0] = 5 * (x / 50)

    # BC: x = 50, y in [0, 30], T from 5 → 7
    for y in range(0, 31):
        phi[50, y] = 5 + 2 * (y / 30)

    # CD: y = 30, x in [50, 150], T = 7
    for x in range(50, 151):
        phi[x, 30] = 7

    # DE: x = 150, y in [0, 30], T from 7 → 5
    for y in range(0, 31):
        phi[150, y] = 5 + 2 * (y / 30)

    # EF: y = 0, x in [150, 200], T from 5 → 0
    for x in range(150, 201):
        phi[x, 0] = 5 - 5 * ((x - 150) / 50)

    # FG: x = 200, y in [0, 80], T from 0 → 10
    for y in range(0, 81):
        phi[200, y] = 10 * (y / 80)

    # GH: y = 80, x in [0, 200], T = 10
    for x in range(0, 201):
        phi[x, 80] = 10

    # HA: x = 0, y in [0, 80], T from 10 → 0
    for y in range(0, 81):
        phi[0, y] = 10 * (y / 80)
    

    # Internal indentation area (the cutout between B-C-D-E) should remain "empty"
    # We’ll set those to np.nan to exclude them from relaxation updates
    phi[51:150, 0:30] = np.nan

    new_phi = phi
    return new_phi

def gauss_seidel(input_phi, omega, iterations=100, use_precision=False):
    X = 200
    Y = 80

    phi = np.copy(input_phi)
    phiprime = np.empty([X+1,Y+1],float)

    delta = 1.0

    if use_precision:
        iterations = 10000      # Arbitrarily big
        target = 1e-6  

    if ANIMATE:
        plt.figure(100)
        plt.title("Gauss-Seidel Relaxation.")
        plt.gray()

    for it in range(iterations):

        phiprime = np.copy(phi)

        for x in range(1, X):
            for y in range(1, Y):
                # Skip NaN regions (indentation)
                if np.isnan(phi[x, y]):
                    phi[x,y] = np.nan
                
                # Skip boundary points (which are fixed)
                elif (
                    np.isnan(phi[x + 1, y]) or np.isnan(phi[x - 1, y])
                    or np.isnan(phi[x, y + 1]) or np.isnan(phi[x, y - 1])
                ):
                    phi[x,y] = phi[x,y]

                # update rule
                else:
                    phi[x, y] = ((1 + omega) / 4.0) * (
                        phi[x + 1, y] + phi[x - 1, y] + phi[x, y + 1] + phi[x, y - 1]
                    ) - omega * phi[x, y]

        if ANIMATE:
            plt.clf()
            plt.title(f"Iteration {it}")
            plt.imshow(phiprime.T, origin="lower")
            plt.colorbar(label="Temperature (C)")
            plt.pause(0.001)

        # Optional progress printout
        if it % 10 == 0:
            print(f"Iteration {it} complete")

        if use_precision:
            delta = np.nanmax(abs(phi-phiprime))
            if delta < target:
                # DONE !!!
                break


    if ANIMATE:
        plt.title(rf"Ani finish: Temp. Dist. ($\omega = {omega}$)")
        plt.show()

    return phi


def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 8 Question 1!")

    # Gauss-Seidel relaxation with replacement and overrelaxation.

    # Step 1: Initialize the boundaries
    # Look at the instructions and directions on Figure 1 of the instructions.

    X = 200     # 20cm with grid spacing of 0.1cm
    Y = 80      # 8cm with grid spacing of 0.1cm

    phi = np.zeros([X+1,Y+1],float)

    phi = init_boundary_conditions(phi)

    # Step 2: Looping...
    # IF ITERATIONS < 100
    #   on each (x,y) value not on the boundary...
    #       do the equation shown on the Computational background. 
    #       T(x,y) = 1 + omega / 4  * [T(x + a, y) + T(x - a, y) T(x, y + a) T(x, y - a)] - omega T(x,y)
    
    # Step 3: Output:
    # plt.imshow(phi.T, origin="lower")
    # plt.gray()
    # plt.show()

    iterations_phi_0 = gauss_seidel(phi, omega=0.0)
    iterations_phi_9 = gauss_seidel(phi, omega=0.9)

    plt.figure(1)
    plt.title(r"Temperature Distribution after 100 Iterations ($\omega = 0.0$)")
    plt.imshow(iterations_phi_0.T, origin="lower")
    plt.gray()
    plt.xlabel("X axis (mm)")
    plt.ylabel("Y axis (mm)")
    plt.colorbar(label="Temperature (C)")

    plt.figure(2)
    plt.title(r"Temperature Distribution after 100 Iterations ($\omega = 0.9$)")
    plt.imshow(iterations_phi_9.T, origin="lower")
    plt.gray()
    plt.xlabel("X axis (mm)")
    plt.ylabel("Y axis (mm)")
    plt.colorbar(label="Temperature (C)")
    plt.show()  

    # Step 4: Do the same thing but with level of convergence
    # IF level of convergence not reached:
    #   on each (x,y) value not on the boundary...
    #       do the equation shown on the Computational background. 
    #       T(x,y) = 1 + omega / 4  * [T(x + a, y) + T(x - a, y) T(x, y + a) T(x, y - a)] - omega T(x,y)
    # 
    # plt.imshow(phi.T, origin="lower")
    # plt.gray()
    # plt.show()

    precision_phi = gauss_seidel(phi, omega=0.9, use_precision=True)
    plt.figure(3)
    plt.title(r"Temperature Distribution to precision 1e-6. ($\omega = 0.9$)")
    plt.imshow(precision_phi.T, origin="lower")
    plt.xlabel("X axis (mm)")
    plt.ylabel("Y axis (mm)")
    plt.gray()
    plt.colorbar(label="Temperature (C)")
    plt.show()  

    # After the solution converges, what is temperature at the point x = 2.5 cm, y = 1 cm?
    print(f"Temperature at (x = 2.5 cm, y = 1.0 cm): {precision_phi[25, 1]:.4f} C")

    print("----------END----------")


if __name__ == "__main__":
    main()
