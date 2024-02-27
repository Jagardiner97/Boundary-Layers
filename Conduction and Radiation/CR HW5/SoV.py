# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Set Properties
k = 20
th = 0.0005
a = 0.02
b = 0.015
T_h = 40
T_inf = 20
h_bar = 50

# Calculations
Bi = h_bar * th / (2 * k)

# Equations
def theta_to_T(theta):
    return theta * (T_h - T_inf) + T_inf

def theta(x, y, n_terms):
    G = 2 * h_bar / (k * th) * (T_h - T_inf)
    theta_sum = 0
    for i in range(n_terms):
        i_odd = i * 2 - 1
        lambda_i = np.pi * i_odd / (2 * a)
        C_i = 4 / (np.pi * i_odd * np.cosh(np.sqrt(lambda_i**2 + G) * b))
        theta_sum += C_i * np.cos(lambda_i * x) * np.cosh(np.sqrt(lambda_i**2 + G) * y)
    return theta_sum

def plot_contour(x_resolution=20, y_resolution=15, num_terms=30):
    # Make the grid and calculate theta
    x = np.linspace(0, a, x_resolution)
    y = np.linspace(0, b, y_resolution)
    X, Y = np.meshgrid(x, y)
    Z = theta(X, Y, num_terms)

    # Plot the contours
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, cmap='viridis')
    plt.colorbar(label="Theta")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Theta Contour Plot")
    plt.show()


# Calculate grid and make contour plot
plot_contour()

print(theta(a/2, b, 100))
