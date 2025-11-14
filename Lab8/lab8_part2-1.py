"""
Created by Oscar Yasunaga University of Toronto
"""
from pylab import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Initial Parameters
h = 1e-6 #Step Size
L = 1 # length L
v = 100 #velocity 

d = 0.1 #distance d 
C = 1
sigma = 0.3
N = 300 # grid spacings
a = L/N

#Profile equation
def phi0(x):
	return C *x*(L- x)/L**2 *exp(- (x-d)**2/ 2/ sigma**2)
	
#Accumulators for plotting. 
fi = zeros(N+1,float)
x = linspace(0,L,N+1)
phi = phi0(x)

#FTCS finite difference scheme
def iterate_FTCS(fi, phi, dt=50e-3):  
    iterations = int(dt/h)
    for _ in range(iterations):
        fi_old =fi.copy()  # Save old values
        fi[1:N] =fi_old[1:N] + h*phi[1:N] #Equation 9.28
        phi[1:N]+= h*v**2/a**2*(fi_old[2:N+1]+fi_old[0:N-1]-2*fi_old[1:N]) #Equation 9.28
    return fi, phi

fi_s, phi_s   = zeros(N+1), phi0(x).copy() #Saving a copy

#Plotting 
fig, ax = plt.subplots(figsize=(8,4))
line, = ax.plot(x - L/2, fi *2000, lw=2, color='royalblue') 

ax.set_xlim((x - L/2).min(), (x - L/2).max())
ax.set_ylim(-1.0, 1.0)
ax.set_xlabel("Horizontal Displacement, centered at x-L/2 (m)")
ax.set_ylabel("Vertical displacement scaled by 1000 times")
ax.set_title("Simulation of a Vibrating Piano String")


#Animation Plotting 
dt_frame = 8e-5 # Frame Rate

#How to update each frame
def update(_frame):
    global fi, phi
    fi, phi = iterate_FTCS(fi, phi, dt_frame)
    line.set_ydata(fi *1000)   # update scaled displacement
    return (line,)

ani = FuncAnimation(fig, update, interval=33, blit=True)
plt.show()