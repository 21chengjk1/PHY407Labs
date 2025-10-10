"""
Welcome to the Code for Lab 5 Q1b in PHY407

If you're running the code as organised in the Repo, please run code from the directory Lab5
"""

import numpy as np
import matplotlib.pyplot as plt

    
def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 5 Question 1b!")
    
    
    # The task is as follows:
    # TEXTBOOK 7.8, PAGE 321 (look for page 331 in the pdf)
    # Write a Python program that uses a fast Fourier transform to calculate the diffrac-
    # tion pattern for a grating with transmission function 
    # q(u) = sin^2 (alpha u) with slits of width 20 micrometre [meaning that alpha = pi/(20 mirco m)] and parameters
    # as above: 
    # w = 200 micro m, 
    # W = 10w = 2 mm, 
    # incident light of wavelength A = 500 nm, 
    # a lens with focal length of 1 meter, 
    # and a screen 10 cm wide. 
    #
    # Choose a suitable number of points to give a good approximation to the grating transmission function and then
    # make a graph of the diffraction intensity on the screen as a function of position x in the
    # range -5cm <= x <= 5cm.
    #
    # Intensity is given by I(x_k) = W^2 / N^2 |c_k|^2, where x_k = (lambda f/ W) * k
    # y_n will need to be padded out with 0s
    
    
    # -----------CONSTANTS-----------:
    lam = 500e-9                # wavelength [m]
    f = 1.0                     # focal length
    w = 200e-6                  # grating width
    W = 10 * w                  # Increased grating width W = 10w
    a = 20e-6                   # slit width [m]
    alpha = np.pi / a           # parameter for sin^2(alpha u)
    screen_width = ...          # The screen width is defined in the plot.

    N = 100                         # Number of Sample points
    u = np.linspace(-w/2, w/2, N)   # A list of sample points.

    q = np.sin(alpha * u)**2        # Define q = sin^2(alpha u)

    P = 10 * N  # number of points after padding
    y = np.zeros(P)
    start = (P - N)//2  # center q(u) in padded array
    y[start:start+N] = q

    C = np.fft.fft(y)    # Each term C_k corresponds to a discrete diffraction order.

    # I_k = (W / N)^2 * |C_k|^2 
    I = (W / N)**2 * np.abs(C)**2

    # x_k = (lambda f / W) * k, with k from 0 to P-1
    k = np.arange(P)
    k_signed = ((k + P//2) % P) - P//2  # shift indices
    x = lam * f * k_signed / W          # position on the screen [m]

    # ------------PLotting the Result.---------------------------
    print("Printing Plots:")
    plt.figure(figsize=(8, 4))
    plt.plot(x * 1000, I, lw=1.2)
    plt.xlabel("x on screen [mm]")
    plt.ylabel("Normalized intensity")
    plt.title("Diffraction pattern for q(u)")
    plt.grid(True)
    plt.xlim(-50, 50)
    plt.tight_layout()
    plt.show()

    # Will need to hand in code and plots and explanatory notes
    print("----------END----------")

if __name__ == '__main__':
    main()