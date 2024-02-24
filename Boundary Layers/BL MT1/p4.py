# Import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Geometry conditions
Re = 1000
spacing = 0.025
L_min = spacing * 10
L_max = spacing * 20
D_h = 2 * spacing
print(L_min, L_max, D_h)

# fluid properties
rho = 825
nu = 0.21
cp = 2000
Pr = 5000

# Read data files
data = pd.read_csv("problem 4/out.txt", delim_whitespace=True, skiprows=21)
xdh = data["x/dh"].values
nu_bottom = data["nu(I)"].values
nu_top = data["nu(E)"].values

# Plot Nusselt Number
plt.plot(xdh, nu_bottom, label="bottom")
plt.plot(xdh, nu_top, label="top")
plt.xlabel("x/dh")
plt.ylabel("Nu")
plt.legend()
plt.title("Nusselt Number on Each Side of the Channel")
plt.show()

num_locs = 5
read_row = 23
for i in range(num_locs):
    profile_data = pd.read_csv("problem 4/profiles.txt", delim_whitespace=True, skiprows=read_row, nrows=127)
    y = profile_data["y(i)"].values
    T = profile_data["f(1,i)"].values
    plt.plot(y, T, label=f"{i}")
    read_row += 131
plt.xlabel("y (m)")
plt.ylabel("T (K)")
plt.legend()
plt.title("Temperature Profiles at x Locations")
plt.show()
