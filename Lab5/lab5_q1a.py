"""
Welcome to the Code for Lab 5 Q1a in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab5
"""

import numpy as np
import matplotlib.pyplot as plt

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


plot_count = 1
def part_a_plots(y, c, coefficient_index, title):
    """
    Helper for Part A
    """
    global plot_count

    plt.figure(plot_count)
    plt.plot(y)
    plt.title("Square Wave")
    plot_count += 1

    plt.figure(plot_count)
    plt.bar(coefficient_index, abs(c))
    # plt.plot(abs(c_square))
    plt.title(title)
    plt.xlim(0, 500)
    
    plot_count += 1

    
def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 1a!")
    
    
    # The task is as follows:
    # Write Python programs to calculate the coefficients in the discrete Fourier transforms of
    # the following periodic functions sampled at N = 1000 evenly spaced points, and make
    # plots of their amplitudes similar to the plot shown in Fig. 7.4:
    # a) A single cycle of a square-wave with amplitude 1
    # b) The sawtooth wave y_n = n
    # c) The modulated sine wave y_n = sin(pi n/N) sin(20 pi n/N)
    # If you wish you can use the Fourier transform function from the file dft.py as a starting
    # point for your program.

    N = 1000
    n = np.arange(N)

    coefficient_index = np.arange(N//2 + 1)

    # Square wave
    y_square = np.ones(N)
    y_square[N//2:] = -1
    c_square = dft(y_square)

    # Sawtooth wave
    y_sawtooth = n
    c_sawtooth = dft(y_sawtooth)

    # Modulated sine wave
    y_sin = np.sin(np.pi * n / N) * np.sin(20 * np.pi * n / N)
    c_sin = dft(y_sin)

    # Square wave
    part_a_plots(y_square, c_square, coefficient_index, "Amplitude of Fourier Coefficients (Square Wave)")

    # Sawtooth waves
    part_a_plots(y_sawtooth, c_sawtooth, coefficient_index, "Amplitude of Fourier Coefficients (Sawtooth)")

    # sin waves
    part_a_plots(y_sin, c_sin, coefficient_index, "Amplitude of Fourier Coefficients (Modulated Sine)")

    plt.show()

    # Will need to hand in code and plots and explanatory notes

    print("----------END----------")

if __name__ == '__main__':
    main()