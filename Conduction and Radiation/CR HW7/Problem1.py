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
Bi = h * L / k
C2 = q_flux * (1 / h + L / k)
plot_times = [0, 100, 200, 500, 1000, 5000, 10_000]


def make_list(x_values):
    temp_list = []
    for pos in x_values:
        temp_list.append(0)
    return temp_list


def calculate_theta(x_vals, time, num_terms):
    temps = make_list(x_vals)
    lambdas = []
    cs = []
    for i in range(num_terms):
        if i == 0:
            lb = 0
            ub = math.pi / 2
        else:
            lb = (1 + 2 * (i - 1)) * math.pi / 2
            ub = (1 + 2 * i) * math.pi / 2
        converged = False
        i_count = 0
        while not converged:
            lambdaL = (lb + ub) / 2
            lhs = math.tan(lambdaL)
            rhs = Bi / lambdaL
            diff = rhs - lhs
            if abs(diff) < 0.00001:
                converged = True
                lambda_i = lambdaL / L
            elif diff > 0:
                lb = lambdaL
            else:
                ub = lambdaL
            i_count += 1
        lambdas.append(lambda_i)
        c_num = q_flux / k * (lambdaL * math.sin(lambdaL) + math.cos(lambdaL) - 1)/(lambda_i**2) - C2 * math.sin(lambdaL) / lambda_i
        C = c_num / ((lambdaL + math.cos(lambdaL)*math.sin(lambdaL))/(2 * lambda_i))
        cs.append(C)
        for i, x_pos in enumerate(x_vals):
            theta_psi = C * math.cos(lambda_i * x_pos) * math.exp(-(lambda_i**2) * alpha * time)
            temps[i] += theta_psi
    for i, x_pos in enumerate(x_vals):
        theta_phi = C2 - q_flux / k * x_pos + T_inf
        temps[i] += theta_phi
    print(lambdas)
    print(cs)
    return temps


x = np.linspace(0, L, 50)
for t in plot_times:
    temperatures = calculate_theta(x, t, 30)
    plt.plot(x, temperatures, label=f"t = {t}")

plt.xlabel("x (m)")
plt.ylabel("Temperature (C)")
plt.legend()
plt.title("Temperature Distribution in the Rod")
plt.show()
