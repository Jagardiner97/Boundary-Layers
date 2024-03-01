# Import Packages
import numpy as np
import matplotlib.pyplot as plt
import math

# Problem Conditions
T_i = 20
T_inf = 20
q_flux = 1000
h = 100
L = 0.1
rho = 6000
k = 10
c = 700
alpha = k / (rho * c)

plot_times = [0, 100, 200, 500, 1000, 5000, 10_000]
C2 = q_flux * (1 / h + L / k)
print("C2:", C2)
dT = -q_flux * L / k
phi_l = q_flux / h
print("dT:", dT)
print("phi_l:", phi_l)

def get_temp(x, t, n_terms=100):
    T_sum = 0
    phi = -q_flux / k * x + T_inf + C2
    for i in range(1, n_terms+1):
        lambda_i = math.pi * i / L
        C_i = 2 * q_flux / (k * L) * (math.cos(lambda_i * L) / lambda_i**2 - 1/lambda_i**2)
        psi_term = math.cos(lambda_i * x) * math.exp(-(lambda_i**2 * alpha * t))
        T_sum += C_i * psi_term
    T_sum += phi
    return T_sum

x_plot = np.linspace(0, L, 50)
temp_plot = []
for time in plot_times:
    temps = []
    for x_val in x_plot:
        temps.append(get_temp(x_val, time))
    temp_plot.append(temps)

for i, temp in enumerate(temp_plot):
    plt.plot(x_plot, temp, label=f"t={plot_times[i]}")
plt.xlabel("x (m)")
plt.ylabel("T (C)")
plt.legend()
plt.title("Temperature Distributions in the Rod")
plt.show()

print("T(L,0):", get_temp(L, 0))
