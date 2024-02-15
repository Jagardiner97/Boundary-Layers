# Import packages
import matplotlib.pyplot as plt

# Define geometry and material properties
y = [0.02, 0.03, 0.051, 0.081, 0.127, 0.191, 0.279, 0.406, 0.660, 1.1, 1.61, 2.12, 2.82, 3.58]#cm
u = [12.94, 14.08, 15.67, 17.31, 19.24, 20.87, 22.68, 24.54, 27.38, 31.10, 34.15, 37.21, 39.37, 39.68]#m/s
P = 1#atm
D = 1.27#mm balls on the surface
T = 19#C
u_inf = 39.7#m/s
delta_2 = 0.367#cm
Re_delta2 = 9974
cf2 = 0.00243

# Find ks, Re_k, kappa, roughness regime, and compare wake to smooth surface

