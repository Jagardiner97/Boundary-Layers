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
data = pd.read_csv("problem 4/out.txt", delim_whitespace=True, skiprows=1)
