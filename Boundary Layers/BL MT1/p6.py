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
plt.title("Friction Factor Comparisons for One Equation")
plt.show()

# ktmu=21 Launder-Sharma
ktmu21_84 = pd.read_csv("problem 6/ktmu21/ftn84.txt", delim_whitespace=True, skiprows=2)
ktmu21_85 = pd.read_csv("problem 6/ktmu21/ftn85.txt", delim_whitespace=True, skiprows=3)
ktmu21_rex = ktmu21_85["rex"].values
ktmu21_rem = ktmu21_85["rem"].values
ktmu21_cf2 = ktmu21_85["cf/2"].values
ktmu21_del2 = ktmu21_84["del2"].values
ktmu21_x = ktmu21_84["x/s"].values

# Plot
ktmu21_1120 = eq11_20(ktmu21_rem)
ktmu21_1123 = eq11_23(ktmu21_rex)
ktmu21_511 = eq5_11(rho, u_inf, nu, ktmu21_del2)
plt.plot(ktmu21_x, ktmu21_cf2, label="TEXSTAN")
plt.plot(ktmu21_x, ktmu21_1120, label="Eq. 11-20")
plt.plot(ktmu21_x, ktmu21_1123, label="Eq. 11-23")
plt.plot(ktmu21_x, ktmu21_511, label="Eq. 5-11")
plt.xlabel("x (m)")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Friction Factor Comparisons for Launder-Sharma")
plt.show()

# ktmu=22 KY Chien
ktmu22_84 = pd.read_csv("problem 6/ktmu22/ftn84.txt", delim_whitespace=True, skiprows=2)
ktmu22_85 = pd.read_csv("problem 6/ktmu22/ftn85.txt", delim_whitespace=True, skiprows=3)
ktmu22_rex = ktmu22_85["rex"].values
ktmu22_rem = ktmu22_85["rem"].values
ktmu22_cf2 = ktmu22_85["cf/2"].values
ktmu22_del2 = ktmu22_84["del2"].values
ktmu22_x = ktmu22_84["x/s"].values

# Plot
ktmu22_1120 = eq11_20(ktmu22_rem)
ktmu22_1123 = eq11_23(ktmu22_rex)
ktmu22_511 = eq5_11(rho, u_inf, nu, ktmu22_del2)
plt.plot(ktmu22_x, ktmu22_cf2, label="TEXSTAN")
plt.plot(ktmu22_x, ktmu22_1120, label="Eq. 11-20")
plt.plot(ktmu22_x, ktmu22_1123, label="Eq. 11-23")
plt.plot(ktmu22_x, ktmu22_511, label="Eq. 5-11")
plt.xlabel("x (m)")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Friction Factor Comparisons for Launder-Sharma")
plt.show()

# ktmu=23 Lam-Bremhorst
ktmu23_84 = pd.read_csv("problem 6/ktmu23/ftn84.txt", delim_whitespace=True, skiprows=2)
ktmu23_85 = pd.read_csv("problem 6/ktmu23/ftn85.txt", delim_whitespace=True, skiprows=3)
ktmu23_rex = ktmu23_85["rex"].values
ktmu23_rem = ktmu23_85["rem"].values
ktmu23_cf2 = ktmu23_85["cf/2"].values
ktmu23_del2 = ktmu23_84["del2"].values
ktmu23_x = ktmu23_84["x/s"].values

# Plot
ktmu23_1120 = eq11_20(ktmu23_rem)
ktmu23_1123 = eq11_23(ktmu23_rex)
ktmu23_511 = eq5_11(rho, u_inf, nu, ktmu23_del2)
plt.plot(ktmu23_x, ktmu23_cf2, label="TEXSTAN")
plt.plot(ktmu23_x, ktmu23_1120, label="Eq. 11-20")
plt.plot(ktmu23_x, ktmu23_1123, label="Eq. 11-23")
plt.plot(ktmu23_x, ktmu23_511, label="Eq. 5-11")
plt.xlabel("x (m)")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Friction Factor Comparisons for Launder-Sharma")
plt.show()

# ktmu=24 Jones-Launder
ktmu24_84 = pd.read_csv("problem 6/ktmu24/ftn84.txt", delim_whitespace=True, skiprows=2)
ktmu24_85 = pd.read_csv("problem 6/ktmu24/ftn85.txt", delim_whitespace=True, skiprows=3)
ktmu24_rex = ktmu24_85["rex"].values
ktmu24_rem = ktmu24_85["rem"].values
ktmu24_cf2 = ktmu24_85["cf/2"].values
ktmu24_del2 = ktmu24_84["del2"].values
ktmu24_x = ktmu24_84["x/s"].values

# Plot
ktmu24_1120 = eq11_20(ktmu24_rem)
ktmu24_1123 = eq11_23(ktmu24_rex)
ktmu24_511 = eq5_11(rho, u_inf, nu, ktmu24_del2)
plt.plot(ktmu22_x, ktmu24_cf2, label="TEXSTAN")
plt.plot(ktmu22_x, ktmu24_1120, label="Eq. 11-20")
plt.plot(ktmu22_x, ktmu24_1123, label="Eq. 11-23")
plt.plot(ktmu22_x, ktmu24_511, label="Eq. 5-11")
plt.xlabel("x (m)")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Friction Factor Comparisons for Launder-Sharma")
plt.show()

# Compare Figure 11.7
plt.plot(one_eq_rem, one_eq_cf2, label="1 Equation")
plt.plot(ktmu21_rem, ktmu21_cf2, label="Launder-Sharma")
plt.plot(ktmu22_rem, ktmu22_cf2, label="KY Chien")
plt.plot(ktmu23_rem, ktmu23_cf2, label="Lam-Bremhorst")
plt.plot(ktmu24_rem, ktmu24_cf2, label="Jones-Launder")
plt.xscale("log")
plt.xlabel("Momentum Thickness Reynolds Number")
plt.ylabel("c_f/2")
plt.legend()
plt.title("Mixing-Length Model")
plt.show()
