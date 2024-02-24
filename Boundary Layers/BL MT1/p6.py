# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# flow conditions
u_inf = 15
rho = 1.177
mu = 1.838e-5
nu = mu / rho

def tau_s(rho, u_inf, nu, delta2):
    return 0.0125 * rho * u_inf**2 * (delta2 * u_inf / nu)**(-1/4)

def eq11_20(Rem):
    cf2 = []
    for r in Rem:
        cf2.append(0.0125 * r**(-1/4))
    return cf2

def eq11_23(Rex):
    cf2 = []
    for r in Rex:
        cf2.append(0.0287 * r**(-0.2))
    return cf2

def eq5_11(rho, u_inf, nu, delta):
    cf2 = []
    for d in delta:
        tau = tau_s(rho, u_inf, nu, d)
        cf2.append(tau / (rho * u_inf**2))
    return cf2


# One Equation Model
# Read data from TEXSTAN
one_eq_84 = pd.read_csv("problem 6/1eq/ftn84.txt", delim_whitespace=True, skiprows=2)
one_eq_85 = pd.read_csv("problem 6/1eq/ftn85.txt", delim_whitespace=True, skiprows=3)
one_eq_rex = one_eq_85["rex"].values
one_eq_rem = one_eq_85["rem"].values
one_eq_cf2 = one_eq_85["cf/2"].values
one_eq_del2 = one_eq_84["del2"].values
one_eq_x = one_eq_84["x/s"].values

# Plot
one_eq_1120 = eq11_20(one_eq_rem)
one_eq_1123 = eq11_23(one_eq_rex)
one_eq_511 = eq5_11(rho, u_inf, nu, one_eq_del2)
plt.plot(one_eq_x, one_eq_cf2, label="TEXSTAN")
plt.plot(one_eq_x, one_eq_1120, label="Eq. 11-20")
plt.plot(one_eq_x, one_eq_1123, label="Eq. 11-23")
plt.plot(one_eq_x, one_eq_511, label="Eq. 5-11")
plt.xlabel("x (m)")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Friction Factor Comparisons")
plt.show()

#

# Compare Figure 11.7
#plt.plot(one_eq_rem, one_eq_cf2, label="1 Equation")

