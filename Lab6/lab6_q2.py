"""
Code for Lab 6 Question 2
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

SHOW_ANIMATION = True

# constants
k_over_m = 400  # 400 rad^2 s^-2


def f(x_vec, k_over_m = k_over_m):
    """
    f, is a vector function which is actually acceleration

    f(x_vec, t) = A * x_vec
    where A is a matrix
    """
    # Define matrix A, based on how big x_vec is...
    # -2  1  0 ...
    #  1 -2  1 ...  * (k/m) 
    #  0  1 -2 ...
    #  .  .  . ...
    # A has -2 on the diagonal, and 1s on the super and subdiagonal
    
    n = len(x_vec)

    mat = (
        np.diag(-2 * np.ones(n)) +
        np.diag(np.ones(n - 1), k=1) +
        np.diag(np.ones(n - 1), k=-1)
    )

    A = mat * k_over_m

    return A @ x_vec


def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 1b!")

    N = 10               # The code should handle N as any integer, representing some N storey building.
    dt = 0.001          # Time step of 1ms = 0.001 s

    # Use an initial value of x0 = 10 cm for the initial position of the lowest floor, 
    # xi = 0 for all of the upper floors, 
    # and start from a state of rest.
    

    x = np.zeros((N,))  # 1D array of N length
    x[0] = 0.1          # 0.1m = 10cm
    # x = [1 0 0 0 ...], length N

    v = np.zeros((N,))  # 1D array of N length
    # v = [0 0 0 0 ...], length N

    
    # step 1:
    t = 0
    x_vec_list = [x]
    t_list = [t]

    # v(t + h/2) = v(t) + 1/2 * h * f(x(t))
    v = v + 1/2 * dt * f(x)

    # Now begin the loop
    max_t = 5               # 5 seconds
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

    # Now let's try plotting
    # Plot movement of floor 0

    x_vec_list = np.array(x_vec_list)
    
    # all the x_values across time for floor 0 are in = x_vec_list[:, 0]

    plt.figure(1)
    plt.plot(t_list, x_vec_list[:, 0], label='Floor 0')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Displacement of Floor 0 vs Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    if SHOW_ANIMATION:
        # Convert lists to arrays
        x_vec_list = np.array(x_vec_list)
        t_list = np.array(t_list)

        # Set up the figure
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.set_xlim(-0.2, 0.2)
        ax.set_ylim(-0.2, N * 0.2)
        ax.set_xlabel('Displacement (m)')
        ax.set_ylabel('Height (m)')
        ax.set_title('Oscillation of N-Storey Building')

        # Plot initial points for each floor
        (line,) = ax.plot([], [], 'o-', lw=2)

        # Initialize
        def init():
            line.set_data([], [])
            return (line,)

        # Update function for each frame
        def update(frame):
            x_positions = x_vec_list[frame, :]     # displacements at this time step
            y_positions = np.arange(N) * 0.1       # vertical spacing between floors
            line.set_data(x_positions, y_positions)
            return (line,)

        # Create the animation
        ani = animation.FuncAnimation(
            fig, update, frames=len(t_list), init_func=init,
            interval=1, blit=True
        )

        plt.show()

    
    print("----------END----------")


if __name__ == '__main__':
    main()