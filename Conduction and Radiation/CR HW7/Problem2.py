# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Problem Properties
L = 0.05
q_flux = 7500
k = 2.4
alpha = 2.2e-4
T_inf = 20
h_bar = 15
T_i = 20
rhoc = alpha / k

def Ts_model(t):
    return (q_flux / h_bar + T_inf) * (1 - math.exp(-2*h_bar*t*rhoc/L)) + T_i


tau_diff = L**2 / (4 * alpha)
T0 = Ts_model(tau_diff)
print("tau_diff =", tau_diff)
print("T0 =", T0)

t_plot = np.linspace(0, tau_diff, 25)
temps = []
for time in t_plot:
    temps.append(Ts_model(time))
plt.plot(t_plot, temps)
plt.xlabel("time (s)")
plt.ylabel("Temperature (C)")
plt.title("Surface Temperature vs Time")
plt.show()
