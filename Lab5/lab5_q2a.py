"""
Welcome to the Code for Lab 5 Q2a in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab5
"""
import numpy as np
import matplotlib.pyplot as plt

from scipy.constants import speed_of_light

PLOT_OSCILLATION = True


k = 12      # k = 12N/m
m = 1       # m = 1kg

def rel_acceleration(x, v):
    """
    Acceleration equation
    -(k/m) * u1 * (1 - u2^2/c^2)^(3/2)

    current constants (from the)
    - k = 12N/m
    - m = 1kg

    """
    global k
    global m

    u1 = x
    u2 = v
    c = speed_of_light

    relativistic_factor = (1 - u2**2 / c**2) ** (3/2)     # For lack of a better name.
    return - (k/m) * u1 * relativistic_factor

def manul_integr(x_0, v_0, deltat, tot, acc = rel_acceleration):
    """
    Manual Integration method for Euler Cromer method. Partly taken from Lab 1 Submission.
    """
    num_steps = int(tot/deltat)
    
    time = np.linspace(0, tot, num_steps)
    x = np.zeros(num_steps)
    v = np.zeros(num_steps)

    x[0] = x_0
    v[0] = v_0


    for i in range(1, num_steps):
        acc_x = acc(x[i-1], v[i-1])
        v_next = v[i-1] + acc_x*deltat
        v[i] = v_next

        x_next = x[i-1] + v[i]*deltat
        x[i] = x_next
    return x, v, time


def main():
    global k
    global m
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 2a!")

    x_c = speed_of_light * np.sqrt(m/k)

    x_0_values = [1, x_c, x_c * 10]
    x_0_labels = ["1m", r"$x_c$", r"$10x_c$"]

    time_step = 0.0001
    tot = 150

    x1, v1, t = manul_integr(x_0=x_0_values[0], v_0=0, deltat=time_step, tot=tot)
    xx_c, vx_c, t = manul_integr(x_0=x_0_values[1], v_0=0, deltat=time_step, tot=tot)
    x10x_c, v10x_c, t = manul_integr(x_0=x_0_values[2], v_0=0, deltat=time_step, tot=tot)
    if PLOT_OSCILLATION:
        plt.figure(1)
        plt.title(r"$x_0 = 1m$")
        plt.plot(t, x1, label=x_0_labels[0])
        plt.xlabel("t")
        plt.ylabel("x(t)")

        plt.figure(2)
        plt.title(r"$x_0 = x_c$")
        plt.plot(t, xx_c, label=x_0_labels[1])
        plt.xlabel("t")
        plt.ylabel("x(t)")

        plt.figure(3)
        plt.title(r"$x_0 = 10x_c$")
        plt.plot(t, x10x_c, label=x_0_labels[2])
        plt.xlabel("t")
        plt.ylabel("x(t)")
        plt.show()

    N = len(t)
    fft_1 = np.fft.rfft(x1)
    fft_xc = np.fft.rfft(xx_c)
    fft_10xc = np.fft.rfft(x10x_c)

    # Construct angular frequency array
    deltat = time_step
    omega = 2 * np.pi * np.arange(len(fft_1)) / (N * deltat)
    omega = np.arange(len(fft_1)) / (N * deltat)

    # Compute and normalize amplitudes
    amp_1 = np.abs(fft_1) / np.max(np.abs(fft_1))
    amp_xc = np.abs(fft_xc) / np.max(np.abs(fft_xc))
    amp_10xc = np.abs(fft_10xc) / np.max(np.abs(fft_10xc))

    # Plot x(t) fourier
    plt.figure(2)
    plt.title(r"Scaled Fourier Spectrum $|\hat{x}(\omega)| / |\hat{x}(\omega)|_{\max}$")
    plt.plot(omega, amp_1, label=x_0_labels[0])
    plt.plot(omega, amp_xc, label=x_0_labels[1])
    plt.plot(omega, amp_10xc, label=x_0_labels[2])
    plt.xlabel(r"Angular frequency $\omega$ (rad/s)")
    plt.ylabel("Scaled amplitude")
    plt.xlim(0, 200)

    
    T_values = [1.8102536520037136, 2.1270744013035268, 11.660887636522721]     # Running compute_integral_with_gauss() from lab 3 yielded these numbers.
    # Plot vertical lines
    for T in T_values:
        plt.axvline(1 / T, color='k', linestyle='--', linewidth=1, alpha=0.7)

    plt.legend()
    plt.tight_layout()

    # FFT ON THE VELOCITIES.
    fft_v1 = np.fft.rfft(v1)
    fft_vxc = np.fft.rfft(vx_c)
    fft_v10xc = np.fft.rfft(v10x_c)

    # Compute and normalize amplitudes
    amp_v1 = np.abs(fft_v1) / np.max(np.abs(fft_v1))
    amp_vxc = np.abs(fft_vxc) / np.max(np.abs(fft_vxc))
    amp_v10xc = np.abs(fft_v10xc) / np.max(np.abs(fft_v10xc))

    # Plot v(t) fourier
    plt.figure(figsize=(8, 4))
    plt.title(r"Scaled Fourier Spectrum of $v(t)$: $|\hat{v}(\omega)| / |\hat{v}(\omega)|_{\max}$")
    plt.plot(omega, amp_v1, label=x_0_labels[0])
    plt.plot(omega, amp_vxc, label=x_0_labels[1])
    plt.plot(omega, amp_v10xc, label=x_0_labels[2])
    plt.xlabel(r"Angular frequency $\omega$ (rad/s)")
    plt.ylabel(r"Scaled amplitude")
    plt.xlim(0, 200)

    for T in T_values:
        plt.axvline(1 / T, color='k', linestyle='--', linewidth=1, alpha=0.7)

    plt.legend()
    plt.tight_layout()

    plt.show()
    
    print("----------END----------")


if __name__ == '__main__':
    main()