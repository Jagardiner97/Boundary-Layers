# Import packages
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit

# Define Functions
def curve_function(y_i, c, k):
    return 1 / 0.41 * np.log(32.6 * (y_i + c) / k + 1)

def roughness_regime(Reynolds_k):
    if Reynolds_k <= 5.0:
        return "smooth"
    elif Reynolds_k <= 70.0:
        return "transitional"
    else:
        return "fully rough"

def fit_values(y_values, ks, offset):
    predicted = []
    for y_point in y_values:
        prediction = curve_function(y_point, offset, ks)
        predicted.append(prediction)
    return predicted


# Define geometry and material properties
y = [0.02, 0.03, 0.051, 0.081, 0.127, 0.191, 0.279, 0.406, 0.660, 1.1, 1.61, 2.12, 2.82, 3.58]#cm
y_m = [val/100 for val in y]
u = [12.94, 14.08, 15.67, 17.31, 19.24, 20.87, 22.68, 24.54, 27.38, 31.10, 34.15, 37.21, 39.37, 39.68]#m/s
P = 1#atm
D = 1.27#mm balls on the surface
T = 19#C
u_inf = 39.7#m/s
delta_2 = 0.367#cm
Re_delta2 = 9974
cf2 = 0.00243
nu = 14.97e-6

# Calculate u_tau and use to solve for u+ and y+
u_tau = math.sqrt(cf2 * u_inf**2)
y_plus = []
for yval in y:
    y_plus.append((yval/100) * u_tau / nu)
u_plus = []
for ubar in u:
    u_plus.append(ubar/u_tau)

# Solve for ks and y offset using a curve fit
wake_removal = -5
y_fit = np.array(y_m[:wake_removal])
u_fit = np.array(u_plus[:wake_removal])
c_lower_bound = np.min(y_fit)
popt, _ = curve_fit(curve_function, y_fit, u_fit, bounds=([-c_lower_bound, c_lower_bound], [np.inf, np.inf]))
y_offset, k_s = popt

# Calculate Re_k, print and plot results
Re_k = k_s * u_tau / nu
print(f"Last {-wake_removal} values removed to avoid wake:")
print("kappa =", 0.41)
print("y_offset =", y_offset*1000, "mm")
print("k_s = ", k_s*1000, "mm")
print("Re_k =", Re_k)
print("The flow is", roughness_regime(Re_k))

fit = fit_values(y_m, k_s, y_offset)
plt.scatter(y_plus, u_plus, label="data")
plt.plot(y_plus, fit, label="fit")
plt.xlabel("y+")
plt.ylabel("u+")
plt.xscale("log")
plt.title("Plot of y+ vs u+")
plt.legend()
plt.show()
