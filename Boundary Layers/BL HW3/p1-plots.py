# Import Packages
import matplotlib.pyplot as plt
import math
import pandas as pd

# Material Properties
rho_air = 1.17 #kg/m3
mu = 1.838e-5 #Pa*s
cp = 1005 #J/kg*K
Re = 1000
Pr = 0.7

# Geometry Properties
D_h = 0.1 #m
L = 0.3 * Re * Pr * D_h / 2 #m

# Display calculated values
print(f"Length = {L}")

# Using T_wall = 400 K, assuming properties at 25 C

# Read the Data
out_data = pd.read_csv("basic.txt", delim_whitespace=True, skiprows=21)
x_plus = out_data["x/dh"].values * (2/(Re * Pr))
nu = out_data["nu(E)"].values

plt.plot(x_plus, nu)
plt.xlabel("x+")
plt.ylabel("Nu_x")
plt.ylim(0, 10)
plt.axhline(y=3.657, color='red', linestyle='--', label="3.657")
plt.legend()
plt.title("Nusselt Number Development")
plt.show()

start_row = 24
xvals = [0, 0.35, 3.5, 10, 105]
for profile in range(5):
    profile_data = pd.read_csv("out.txt", delim_whitespace=True, skiprows=start_row, nrows=64)
    y = profile_data["y(i)"].values
    temps = profile_data["f,ratio"].values
    xplus = xvals[profile] * (2 / (Re * Pr))
    plt.plot(y, temps, label=f"x+ = {xplus:.4f}")
    start_row += 69

plt.xlabel("y (m)")
plt.ylabel("(T_s - T)/(T_s - T_m)")
plt.title("Nondimensional Temperature Profiles at Multiple x+ Locations")
plt.legend()

plt.show()
