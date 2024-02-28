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
theta_h = T_h - T_inf

# Equations
def theta_to_T(theta):
    return theta + T_inf

def theta(x, y, n_terms):
    G = 2 * h_bar / (k * th)
    theta_sum = 0
    for i in range(1, n_terms+1):
        i_odd = i * 2 - 1
        lambda_i = np.pi * i_odd / (2 * a)
        C_i = 2 * (-1**(i-1)) / (lambda_i * a * np.cosh(np.sqrt(lambda_i**2 + G) * b))
        cos_term = np.cos(lambda_i * x)
        cosh_term = np.cosh(np.sqrt(lambda_i**2 + G) * y)
        theta_val = C_i * cos_term * cosh_term * theta_h
        theta_sum += theta_val
    Temp = theta_to_T(theta_sum)
    return Temp

def plot_contour(x_resolution=20, y_resolution=15, num_terms=100):
    # Make the grid and calculate theta
    x = np.linspace(0, a, x_resolution)
    y = np.linspace(0, b, y_resolution)
    X, Y = np.meshgrid(x, y)
    Z = theta(X, Y, num_terms)
    z = []
    for x_point in x:
        z_row = []
        for y_point in y:
            z_row.append(theta(x_point, y_point, num_terms))

    # Plot the contours
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, cmap='YlOrRd', levels=20)
    plt.colorbar(label="Theta")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Theta Contour Plot")
    plt.show()


# Calculate grid and make contour plot
plot_contour()

print(theta(a, b/2, 100))
