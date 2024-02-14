# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set geometry parameters
Reynolds_start = 2e5
Reynolds_end = 2.9e6
Reynolds_start_momentum = 700
Reynolds_end_momentum = 5400
T_fs = 300
plate_width = 1 #m unit width
plate_length = 3
V_fs = 15
T_surface = 295
Pr = 0.707

# set fluid properties
rho = 1.177
mu = 1.838e-5
cp = 1005

# Calculate start and stop x values
x_start = Reynolds_start * mu / (rho * V_fs)
x_end = Reynolds_end * mu / (rho * V_fs)
print(f"xstart: {x_start}")
print(f"xend: {x_end}")

# Read data
filepath = "12-17/out.txt"
data = pd.read_csv(filepath, delim_whitespace=True, skiprows=26)
rex = data["rex"].values
st_tst = data["st"].values

# Stanton Number Calculations
st18 = []
st19 = []
for re in rex:
    st18.append(0.0287 * (re ** (-0.2)) * Pr ** (-0.4))
    st19.append(0.0125 * (re ** (-0.25)) * Pr ** (-0.5))

# Plots
plt.plot(rex, st_tst, label="TEXSTAN")
plt.plot(rex, st18, label="Eq. 12-18")
plt.plot(rex, st19, label="Eq. 12-19")
plt.xlabel("Re_x")
plt.ylabel("St")
plt.legend()
plt.show()

