import numpy as np
import matplotlib.pyplot as plt
import math

k = 20
th = 0.5 / 1000
a = 20 / 1000
b = 15 / 1000
T_h = 40
T_inf = 20
h_bar = 50

theta_h = T_h - T_inf
Bi = h_bar * th / (2 * k)

def calculate_temperature(x, y, n_terms):
    G = 2 * h_bar / (k * th)
    theta_sum = 0
    for i in range(1, n_terms+1):
        lambda_i = (2 * i - 1) * math.pi / (2 * a)
        C_i = 2 * theta_h * (2 * (i%2) - 1) / (a * lambda_i * math.cosh(math.sqrt(lambda_i**2 + G) * b))
        theta_sum += C_i * math.cos(lambda_i * x) * math.cosh(math.sqrt(lambda_i**2 + G) * y)
    Temperature = theta_sum + T_inf
    return Temperature

def plot_contour(x_resolution=20, y_resolution=15, num_terms=100):
    # Make the grid and calculate theta
    x = np.linspace(0, a, x_resolution)
    y = np.linspace(0, b, y_resolution)
    Z = []
    for x_pos in x:
        z_row = []
        for y_pos in y:
            z_row.append(calculate_temperature(x_pos, y_pos, num_terms))
        Z.append(z_row)
    z_array = np.array(Z)
    z_array = np.rot90(z_array)
    z_array = np.flipud(z_array)

    # Plot the contours
    plt.figure(figsize=(8, 6))
    plt.contourf(x, y, z_array, cmap='YlOrRd', levels=20)
    plt.colorbar(label="T (C)")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Temperature Contour Plot")
    plt.show()


def get_heater_power(n_terms=100):
    G = 2 * h_bar / (k * th)
    q_sum1 = 0
    q_sum2 = 0
    for i in range(1, n_terms+1):
        lambda_i = (2*i - 1) * math.pi / (2 * a)
        C_i = 2 * theta_h * (2 * (i % 2) - 1) / (a * lambda_i * math.cosh(math.sqrt(lambda_i ** 2 + G) * b))
        q_sum1 += C_i / (lambda_i * math.sqrt(lambda_i**2 + G)) * math.sin(lambda_i * a) * math.sinh(math.sqrt(lambda_i ** 2 + G) * b)
        q_sum2 += C_i * lambda_i / math.sqrt(lambda_i**2 + G) * math.sin(lambda_i * a) * math.sinh(math.sqrt(lambda_i**2 + G) * b)
    q = 8 * h_bar * q_sum1 + 4 * k * th * q_sum2
    return q


plot_contour()
print(f"q_h = {get_heater_power():.3f} W")
