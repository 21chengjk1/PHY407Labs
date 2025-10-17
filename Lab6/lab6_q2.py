"""
Code for Lab 6 Question 2
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import find_peaks

SHOW_PART_A_PLOTS = True
SHOW_PART_A_ANIMATION = True

# constants
k_over_m = 400  # 400 rad^2 s^-2


def construct_mat(n):
    """
    We need the matrix that is like
    -2  1  0 ...
     1 -2  1 ...  * (k/m) 
     0  1 -2 ...
     .  .  . ...
    where mat has -2 on the diagonal, and 1s on the super and subdiagonal
    """
    mat = (
        np.diag(-2 * np.ones(n)) +
        np.diag(np.ones(n - 1), k=1) +
        np.diag(np.ones(n - 1), k=-1)
    )
    return mat

def f(x_vec, k_over_m = k_over_m):
    """
    f, is a vector function which is actually acceleration

    f(x_vec, t) = A * x_vec
    where A is a matrix
    """
    n = len(x_vec)
    mat = construct_mat(n)
    A = mat * k_over_m

    return A @ x_vec


def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 1b!")

    N_values = [3, 10]
    dt = 0.001              # Time step of 1ms = 0.001 s
    max_t = 5               # 5 seconds
    
    for N in N_values:
        # xi = 0 for all of the upper floors
        x = np.zeros((N,))  # 1D array of N length
        
        # Use an initial value of x0 = 10 cm for the initial position of the lowest floor, 
        x[0] = 0.1          # 0.1m = 10cm
        # x = [1 0 0 0 ...], length N

        # and start from a state of rest.
        v = np.zeros((N,))  # 1D array of N length
        # v = [0 0 0 0 ...], length N

        # And now begins the Verlet Method.
        # step 1: Initialization and computing v(t + h/2)
        t = 0.0
        x_vec_list = [x]
        t_list = [t]

        # v(t + h/2) = v(t) + 1/2 * h * f(x(t))
        v = v + 1/2 * dt * f(x)

        # Now begin the loop
        while t <= max_t:
            # r(t+h) = r(t) + h v(t + h/2)
            x = x + dt * v

            # Intermediate k = h * f(r(t+h))
            inter_k = dt * f(x)

            # v(t + 3h/2) = v(t + h/2) + k
            v = v + inter_k

            t = t + dt

            x_vec_list.append(x)
            t_list.append(t)

        x_vec_list = np.array(x_vec_list)
        t_list = np.array(t_list)
        
        # all the x_values across time for floor 0 are in = x_vec_list[:, 0]

        if SHOW_PART_A_PLOTS:
            plt.figure(1)
            for i in range(N):
                plt.plot(
                    t_list,
                    x_vec_list[:, i] + i * 0.5,
                    label=f'Floor {i}',
            )
            plt.xlabel('Time (s)')
            plt.ylabel('Displacement (m) with offset by Floor')
            plt.title(f'Displacement of Floors vs Time (N = {N})')
            plt.legend()
            plt.grid(True)
            plt.show()

        # ANIMATION USED IN EARLIER VERSION OF CODE, MADE BY GPT. KEPT TO SHOW EXTENT OF AI USE.
        # ---------------------------------------------------------------------
        # if SHOW_PART_A_ANIMATION:
        #     # Convert lists to arrays
        #     x_vec_list = np.array(x_vec_list)
        #     t_list = np.array(t_list)

        #     # Set up the figure
        #     fig, ax = plt.subplots(figsize=(6, 6))
        #     ax.set_xlim(-0.2, 0.2)
        #     ax.set_ylim(-0.2, N * 0.2)
        #     ax.set_xlabel('Displacement (m)')
        #     ax.set_ylabel('Height (m)')
        #     ax.set_title('Oscillation of N-Storey Building')

        #     # Plot initial points for each floor
        #     (line,) = ax.plot([], [], 'o-', lw=2)

        #     # Initialize
        #     def init():
        #         line.set_data([], [])
        #         return (line,)

        #     # Update function for each frame
        #     def update(frame):
        #         x_positions = x_vec_list[frame, :]     # displacements at this time step
        #         y_positions = np.arange(N) * 0.1       # vertical spacing between floors
        #         line.set_data(x_positions, y_positions)
        #         return (line,)

        #     # Create the animation
        #     ani = animation.FuncAnimation(
        #         fig, update, frames=len(t_list), init_func=init,
        #         interval=1, blit=True
        #     )

        #     plt.show()

    
    # Part B
    #     Another way to characterize this system is to find its normal modes of vibra-
    # tion. 
    # For N = 3, use Python to find the characteristic normal frequencies (in Hz)
    # and describe the normal modes of the system that vibrate with these frequencies
    # (similar to the kind of analysis you would have done in PHY254). 

    N = 3
    A = construct_mat(N) * k_over_m

    # Compute eigenvalues and eigenvectors
    eigvals, eigvecs = np.linalg.eig(A)

    omega = np.sqrt(-eigvals)   # since λ = −ω2 according to the physics background
    freqs = omega / (2 * np.pi)

    print("\n--- Normal Mode for N = 3 ---")
    for i in range(N):
        print(f"{i+1}: ω = {omega[i]:.3f} rad/s, f = {freqs[i]:.3f} Hz")
        print(f"Eigenvector (mode shape): {eigvecs[:, i]}\n")

    # Plot normal mode shapes
    plt.figure(2)
    for i in range(N):
        plt.plot(range(1, N+1), eigvecs[:, i], 'o-', label=f"Mode {i+1}")
    plt.xlabel("Floor number")
    plt.ylabel("Relative displacement")
    plt.title("Normal Modes (Eigenvectors)")
    plt.legend()
    plt.grid(True)
    plt.show()


    # Then confirm
    # that these are normal modes by initializing the system in each of these modes,
    # starting from rest with ˆx set to each of the eigenvectors, in turn, and plotting the
    # time series of the solutions that result. 

    dt = 0.001
    max_t = 5
    t_vals = np.arange(0, max_t, dt)

    line_styles = ['-.', '--', ':']


    results = []            # Results for frequency analysis later.
    for mode in range(N):
        x = eigvecs[:, mode].copy()     # initial shape
        v = np.zeros_like(x)            # at rest

        x_list = [x.copy()]
        v = v + 0.5 * dt * f(x, k_over_m)

        for t in t_vals[1:]:
            x = x + dt * v
            v = v + dt * f(x, k_over_m)
            x_list.append(x.copy())

        x_list = np.array(x_list)


        # Plotting the displacements
        plt.figure()
        for floor in range(N):
            style = line_styles[floor % len(line_styles)]
            plt.plot(t_vals, x_list[:, floor], style, label=f"Floor {floor+1}")
        plt.xlabel("Time (s)")
        plt.ylabel("Displacement")
        plt.title(f"Time evolution for Normal Mode {mode+1}")
        plt.legend()
        plt.grid(True)

        # Frequency analysis: peak to peak.
        disp = x_list[:, 0]  # use floor 1 displacement
        peaks, _ = find_peaks(disp)
        T = t_vals[peaks[1]] - t_vals[peaks[0]]
        f_sim = 1 / T

        f_eig = freqs[mode]
        error = abs((f_sim - f_eig) / f_eig) * 100
        results.append((mode + 1, f_sim, f_eig, error))
    plt.show()


    # Table:
    print("\n--- Frequency Comparison Table ---")
    print(f"{'Mode':<6}{'Simulated f (Hz)':<20}{'Eigen f (Hz)':<20}{'Error (%)':<10}")
    for mode, f_sim, f_eig, err in results:
        print(f"{mode:<6}{f_sim:<20.4f}{f_eig:<20.4f}{err:<10.2f}")

    print("----------END----------")


if __name__ == '__main__':
    main()