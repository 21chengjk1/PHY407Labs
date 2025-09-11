import numpy as np
import matplotlib.pyplot as plt


x0 = 0.47
y0 = 0
vx0 = 0
vy0 = 8.17
deltat = 0.0001
G = 39.5

ALPHA = 0.01

def radius(x,y):
    return np.sqrt((x**2)+(y**2))

def force(x,y, radius = radius):
    return -1*G*x/radius(x,y)**3, -1*G*y/radius(x,y)**3

def rel_force(x, y):
    return -1*G*x/radius(x,y)**3*(1+ALPHA/radius(x,y)**2), -1*G*y/radius(x,y)**3*(1+ALPHA/radius(x,y)**2)


def manul_integr(x_0, y_0, v_x0, v_y0, deltat, tot, force = force):
    num_steps = int(tot/deltat)
    
    time = np.linspace(0, tot, num_steps)
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    v_x = np.zeros(num_steps)
    v_y = np.zeros(num_steps)

    x[0] = x_0
    y[0] = y_0
    v_x[0] = v_x0
    v_y[0] = v_y0

    for i in range(1, num_steps):
        forcex, forcey = force(x[i-1], y[i-1])
        v_next_x = v_x[i-1] + forcex*deltat
        v_next_y = v_y[i-1] + forcey*deltat
        v_x[i], v_y[i] = v_next_x, v_next_y

        x_next = x[i-1] + v_x[i]*deltat
        y_next = y[i-1] + v_y[i]*deltat
        x[i], y[i] = x_next, y_next
    
    return x,y, v_x, v_y, time
        
def plotting(x_axis, y_axis, title, xlabel, ylabel):
    plt.title(f"{title}")
    plt.xlabel(f"{xlabel}")
    plt.ylabel(f"{ylabel}")
    plt.plot(x_axis, y_axis)
    plt.show()

x,y, vx, vy, t = manul_integr(x_0 = x0, y_0 = y0, v_x0= vx0, v_y0 = vy0, deltat = deltat, tot = 1)
plotting(x, y, "Mercury's Orbit", "Mercury's X position (AU)", "Mercury's Position (AU)")
plotting(t,vx, "Mercury's Velocity along X-Directioun vs Time", "Time (Year)", "Mercury's X Velocity (AU/Year)")
plotting(t,vy, "Mercury's Velocity along Y-Direction vs Time","Time (Year)",  "Mercury's Y Velocity (AU/Year)")

x,y, vx, vy, t = manul_integr(x_0 = x0, y_0 = y0, v_x0= vx0, v_y0 = vy0, deltat = deltat, tot = 1, force = rel_force)
plotting(x, y, "Mercury's Orbit with General Relativity Gravitational Force", "Mercury's X Position (AU)", "Mercury's Y Position (AU)")


x0 = 1
y0 = 0
vx0 = 0
vy0 = 6.18

