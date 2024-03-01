# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Problem Properties
L = 0.05
q_flux = 7500
k = 2.4
alpha = 2.2e-4
T_inf = 20
h_bar = 15
T_i = 20

#
tau_diff = L**2 / (4 * alpha)
T0 = q_flux / (k * L / (2 * alpha)) * (1 - np.exp(-h_bar / (k * L / (2 * alpha)) * tau_diff)) + T_inf
print("tau_diff =", tau_diff)
print("T0 =", T0)
print(np.exp(-h_bar / (k * L / (2 * alpha)) * tau_diff))