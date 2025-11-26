from random import random,randrange
from math import exp,pi
from numpy import ones
import matplotlib.pyplot as plt

T = 10.0
L = 10.0
N = 1000
steps = 10000000

# Create a 2D array to store the quantum numbers
n = ones([N,3],int)

# Main loop
eplot = []
E = 3*N*pi*pi/(2*L*L)
for k in range(steps):
    print(f"Step {k}...")

    # Choose the particle and the move
    i = randrange(N)
    j = randrange(3)
    if random()<0.5:
        dn = 1
        dE = (2*n[i,j]+1)*pi*pi/(2*L*L)
    else:
        dn = -1
        dE = (-2*n[i,j]+1)*pi*pi/(2*L*L)

    # Decide whether to accept the move
    if n[i,j]>1 or dn==1:
        if random()<exp(-dE/T):
            n[i,j] += dn
            E += dE

    eplot.append(E)

# Make the graph
plt.plot(eplot)
plt.ylabel("Energy")
plt.ticklabel_format(style="plain")
plt.show()
