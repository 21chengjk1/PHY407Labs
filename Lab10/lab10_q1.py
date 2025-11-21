"""
Code for Lab 10 Question 1
"""

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

SHOW_RANDOM_SPHERE = True
PLOT_MONTE_CARLO_EARTH = True

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

    # Convert degrees to radians
    lat = np.radians(lat_array)
    lon = np.radians(lon_array)

    dlat = abs(lat[1] - lat[0])
    dlon = abs(lon[1] - lon[0])

    # area strip as before
    strip_area = np.cos(lat) * dlat * dlon   # shape: (2160,)

    # reshape
    area_grid = strip_area[None, :]    # to shape (1, 2160)

    # compute land area
    land_area = np.sum(area_grid * data)

    earth_area = 4 * np.pi
    return land_area / earth_area

def monte_carlo_land_fraction(N, data, lon_array, lat_array):
    """
    Randomly sample N points on the sphere and estimate land fraction.
    """
    theta = generate_random_thetas(N)
    phi = generate_random_phis(N)

    # Convert spherical coordinates to earth coordinates.
    lat_deg = 90 - np.degrees(theta)     # latitude in degrees
    lon_deg = np.degrees(phi)            # longitude in degrees
    lon_deg = (lon_deg + 180) % 360 - 180

    # Prepare output, start it as all 0s first.
    is_land = np.zeros(N, dtype=bool)

    # Loop through samples
    for i in range(N):
        # find nearest indices. 
        # (ChatGPT suggested this method which I think looks neater than the suggested method in the Computational Background)
        lat_idx = np.argmin(np.abs(lat_array - lat_deg[i]))
        lon_idx = np.argmin(np.abs(lon_array - lon_deg[i]))

        # dataset is shape (lon, lat)
        is_land[i] = (data[lon_idx, lat_idx] == 1)

    return np.mean(is_land), is_land, lon_deg, lat_deg


def main():
    print("----------START----------")
    print("Hi! Welcome to Lab 10 Question 1!")

    np.random.seed(67 + 67 + 67)

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
        ax.scatter(x, y, z, s=1) # type: ignore

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        ax.set_title(f"{N} Random Points on Sphere")

        plt.show()
    
    
    # Part C) Calculate land fraction by numerical integration
    land_fraction = numerical_land_fraction()
    print("Fraction:", land_fraction)

    # Part D) 
    loaded = np.load('data/Earth.npz')
    data = loaded['data']
    lon_array = loaded['lon']
    lat_array = loaded['lat']

    for N in [50, 500, 5000, 50000]:
        frac, is_land, lon_deg, lat_deg = monte_carlo_land_fraction(N, data, lon_array, lat_array)
        print(f"N={N}: Monte Carlo land fraction = {frac:.4f}")

        # Data for N = 50000, to plot.
        if N == 50000:
            mc_is_land = is_land
            mc_lon = lon_deg
            mc_lat = lat_deg

    if PLOT_MONTE_CARLO_EARTH:
        plt.figure(figsize=(10,5))
        plt.scatter(mc_lon[mc_is_land], mc_lat[mc_is_land], s=1, color="green", label="Land")
        plt.scatter(mc_lon[~mc_is_land], mc_lat[~mc_is_land], s=1, color="blue", label="Water")
        plt.xlabel("Longitude (deg)")
        plt.ylabel("Latitude (deg)")
        plt.title("Monte Carlo Land/Water Classification (N = 50000)")
        plt.legend(markerscale=6)
        plt.show()

    print("----------END----------")


if __name__ == "__main__":
    main()
