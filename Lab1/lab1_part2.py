from lab1_part1 import force, radius, manul_integr, plotting
import numpy as np
import matplotlib.pyplot as plt

MJ = 10**(-3)
AJ = 5.2

earth_x0 = 1
earth_y0 = 0
earth_vx0 = 0
earth_vy0 = 6.18

jupiter_x0 = 5.2
jupiter_y0 = 0
jupiter_vx0 = 0
jupiter_vy0 = 2.63

deltat = 0.0001
G = 39.5

total_years = 40

def dist(jupx, jupy, eartx, earty):
    diffx, diffy = jupx-eartx, jupy-earty
    return np.sqrt(diffx**2+diffy**2)

def new_force(x,y, jx, jy):
    sunx, suny = force(x,y)
    jupx, jupy = -1*G*MJ*x/dist(jx, jy, x, y)**3, -1*G*MJ*y/dist(jx, jy, x, y)**3
    return sunx+jupx, suny+jupy

def new_manul_integr(x_0, y_0, v_x0, v_y0, deltat, tot, jx, jy):
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
        forcex, forcey = new_force(x[i-1],  y[i-1], jx[i-1], jy[i-1])
        print(forcex, forcey)

        v_next_x = v_x[i-1] + forcex*deltat
        v_next_y = v_y[i-1] + forcey*deltat
        v_x[i], v_y[i] = v_next_x, v_next_y

        x_next = x[i-1] + v_x[i]*deltat
        y_next = y[i-1] + v_y[i]*deltat
        x[i], y[i] = x_next, y_next
    
    return x, y, v_x, v_y, time    

# jx, jy, jvx, jvy, jt = manul_integr(jupiter_x0, jupiter_y0, jupiter_vx0, jupiter_vy0, deltat, total_years, force = force)
# ex, ey, evx, evy, et = new_manul_integr(earth_x0, earth_y0, earth_vx0, earth_vy0, deltat, total_years, jx, jy)

# plotting(jx, jy, "Jupiter's Orbit with Same Mass as Sun Over 20 Years", "Jupiter's X Position (AU)", "Jupiter's Y Position (AU)")
# plotting(ex, ey, "Earth Orbit Over 20 Years", "Earth's X Position (AU)", "Earth's Y Position (AU)")

total_years = 20
xa0 = 3.3
ya0 = 0
vxa0  = 0
vya0 = 3.46

jx, jy, jvx, jvy, jt = manul_integr(jupiter_x0, jupiter_y0, jupiter_vx0, jupiter_vy0, deltat, total_years, force = force)
ax, ay, avx, avy, at = new_manul_integr(xa0, ya0, vxa0, vya0, deltat, total_years, jx, jy)

plotting(jx, jy, "Jupiter Orbit", "Jupiter's X Position (AU)", "Jupiter's Y Position (AU)")
plotting(ax, ay, "Asteroid Orbit", "Asteroid's X Position (AU)", "Asteroid's Y Position (AU)")