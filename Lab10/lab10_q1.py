"""
Code for Lab 10 Question 1
"""

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

SHOW_RANDOM_SPHERE = False

def generate_random_thetas(N):
    """
    Generates N random theta values in an array.
    """
    random = np.random.rand(N)
    argument = 1 - (2*random)
    return np.arccos(argument)

def generate_random_phis(N):
    """
    Generates N random phi values in an array.
    """
    random = np.random.rand(N)
    return 2 * np.pi * random


def numerical_land_fraction():
    """
    Numerically compute the land fraction from the npz data.
    """
    loaded = np.load('data/Earth.npz')
    data = loaded['data']
    lon_array = loaded['lon']
    lat_array = loaded['lat']

    # Convert degrees → radians
    lat = np.radians(lat_array)
    lon = np.radians(lon_array)

    dlat = abs(lat[1] - lat[0])
    dlon = abs(lon[1] - lon[0])

    # area strip as before
    strip_area = np.cos(lat) * dlat * dlon   # shape: (2160,)

    # reshape to broadcast with data(lon,lat)
    area_grid = strip_area[None, :]    # to shape (1, 2160)

    # compute land area
    land_area = np.sum(area_grid * data)

    earth_area = 4 * np.pi
    return land_area / earth_area

def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 10 Question 1!")

    N = 5000        # Number provided by instructions
    list_of_theta = generate_random_thetas(N)
    list_of_phi = generate_random_phis(N)

    if SHOW_RANDOM_SPHERE:
        # Convert spherical (theta, phi) to Cartesian (x, y, z)
        theta = list_of_theta
        phi = list_of_phi

        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)

        # 3D scatter plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z, s=1)

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title("Random Points on Sphere")

        plt.show()
    
    
    # Part C) Calculate land fraction by numerical integration
    land_fraction = numerical_land_fraction()
    print("Fraction:", land_fraction)

    # Part D) 

    print("----------END----------")


if __name__ == "__main__":
    main()
