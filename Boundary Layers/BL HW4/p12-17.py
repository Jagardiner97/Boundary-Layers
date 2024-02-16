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
rem = data["rem"].values
st_tst = data["st"].values
thermal = pd.read_csv("12-17/ftn86.txt", delim_whitespace=True, skiprows=3)
xthermal = thermal["x/s"].values
qflux = thermal["qflux"].values

# Stanton Number Calculations
st18 = []
st19 = []
st24 = []
x = []
for re in rex:
    st18.append(0.0287 * (re ** (-0.2)) * Pr ** (-0.4))
    x.append(re * mu / (rho * V_fs))
for re in rem:
    st19.append(0.0125 * (re ** (-0.25)) * Pr ** (-0.5))
denom24 = rho * V_fs * cp * (T_surface - T_fs)
for q in qflux:
    st24.append(q/denom24)

# Stanton Number Plots
plt.plot(x, st_tst, label="TEXSTAN")
plt.plot(x, st18, label="Eq. 12-18")
plt.plot(x, st19, label="Eq. 12-19")
plt.plot(xthermal, st24, label="Eq. 5-24")
plt.xlabel("x")
plt.ylabel("St")
plt.title("Stanton Number Comparisons")
plt.legend()
plt.show()

