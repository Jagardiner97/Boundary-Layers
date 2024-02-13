# Import libraries
import matplotlib.pyplot as plt
import pandas as pd

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

# set fluid properties
rho = 1.177
mu = 1.838e-5
cp = 1005

# Calculate start and stop x values
x_start = Reynolds_start * mu / (rho * V_fs)
x_end = Reynolds_end * mu / (rho * V_fs)
print(f"xstart: {x_start}")
print(f"xend: {x_end}")
