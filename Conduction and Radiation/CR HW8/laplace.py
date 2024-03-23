# Import Libraries
import math
import numpy as np
import matplotlib.pyplot as plt

# Set Problem Constants
alpha = 2.2e-4  # m^2/s
k = 2.4  # W/m*K
h = 15  # W/m^2*K
q = 7500  # W/m^2
L = 5 / 100  # m
T_i = 20  # C


def get_temperature(x, t):
    # Returns the temperature at any time and x location
    term1 = math.erfc(x/(2 * math.sqrt(alpha * t)))
    term2 = math.exp(h * x / k) * math.exp(alpha * h**2 * t / (k**2)) * math.erfc(math.sqrt(alpha * t) * h / k + x / (2 * math.sqrt(alpha * t)))
    return q / h * (term1 - term2) + T_i


times = [0.000001, 0.5, 1, 1.5, 2, 2.5, 5]
x_range = np.linspace(0, L, 50)
for time in times:
    T_vals = []
    for x_val in x_range:
        T_vals.append(get_temperature(x_val, time))
    plt.plot(x_range, T_vals, label=f"t={time} s")
plt.xlabel("x (m)")
plt.ylabel("Temperature (C)")
plt.ylim([0, 125])
plt.legend()
plt.title("Temperature vs Position at Multiple Times")
plt.show()
