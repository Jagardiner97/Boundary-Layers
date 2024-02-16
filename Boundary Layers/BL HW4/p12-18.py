# Import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Geometry
u_inf = 15
T_s = 295
T_fs = 300
Reynolds_start = 2e5
Reynolds_end = 2.9e6

# Air
rho_air = 1.177
mu_air = 1.838e-5
cp_air = 1005
Pr_air = 0.707

# Water 303 K
rho_water = 995.67
mu_water = 7.97e-4
cp_water = 4180
Pr_water = 5.43

# Acetone at 293 K
rho_acetone = 784.5
mu_acetone = 3.16e-4
cp_acetone = 2140
Pr_acetone = 2.19

# Equations
def eq12_17(Re_x, Pr):
    # General
    return 0.0287 * Re_x**(-0.2) / (0.169 * Re_x**(-0.1) * (13.2 * Pr - 9.25) + 0.85)

def eq12_18(Re_x, Pr):
    # if 0.5<Pr<1 and 5e5<Rex<5e6
    return 0.0287 * Re_x**(-0.2) * Pr**(-0.4)

def eq12_19(Re_enthalpy, Pr):
    # gases
    return 0.0125 * Re_enthalpy ** (-0.25) * Pr**(-0.5)

def eq12_20(Re_x, Pr):
    # 0.7 < Pr < 5.9
    n = 0.1879 * Pr**(-0.18)
    return 0.02426 * Pr**(-0.895) * Re_x**(-n)

def eq12_21(Re_enthalpy, Pr):
    # 0.7 < Pr < 5.9
    n = 0.1879 * Pr ** (-0.18)
    C = 0.02426 * Pr**(-0.895)
    return C * ((1 - n)/C)**(n/(n-1)) * Re_enthalpy**(n/(n-1))

def start_end(rho, u, mu, Re_start, Re_end):
    x_start = Re_start * mu / (rho * u)
    x_end = Re_end * mu / (rho * u)
    return x_start, x_end

def rex_to_x(rho, u, mu, Re):
    return Re * mu / (rho * u)


# Calculate starting and ending values so that the reynolds range is the same
start_air, end_air = start_end(rho_air, u_inf, mu_air, Reynolds_start, Reynolds_end)
start_water, end_water = start_end(rho_water, u_inf, mu_water, Reynolds_start, Reynolds_end)
start_acetone, end_acetone = start_end(rho_acetone, u_inf, mu_acetone, Reynolds_start, Reynolds_end)
print(f"Air: x_start = {start_air}, x_end = {end_air}")
print(f"Water: x_start = {start_water}, x_end = {end_water}")
print(f"Acetone: x_start = {start_acetone}, x_end = {end_acetone}")

# Read data files
air = pd.read_csv("12-18/air.txt", delim_whitespace=True, skiprows=26)
rex_air = air["rex"].values
reh_air = air["reh"].values
st_air = air["st"].values
water = pd.read_csv("12-18/water.txt", delim_whitespace=True, skiprows=26)
rex_water = water["rex"].values
reh_water = water["reh"].values
st_water = water["st"].values
acetone = pd.read_csv("12-18/acetone.txt", delim_whitespace=True, skiprows=26)
rex_acetone = acetone["rex"].values
reh_acetone = acetone["reh"].values
st_acetone = acetone["st"].values

# St Calculation Comparisons for air
air1217 = []
air1218 = []
air1219 = []
air1220 = []
air1221 = []
x_air = []
for re in rex_air:
    x_air.append(rex_to_x(rho_air, u_inf, mu_air, re))
    air1217.append(eq12_17(re, Pr_air))
    air1218.append(eq12_18(re, Pr_air))
    air1220.append(eq12_20(re, Pr_air))
for re in reh_air:
    air1219.append(eq12_19(re, Pr_air))
    air1221.append(eq12_21(re, Pr_air))

plt.plot(x_air, st_air, label="TEXSTAN")
plt.plot(x_air, air1217, label="Eq. 12-17")
plt.plot(x_air, air1218, label="Eq. 12-18")
plt.plot(x_air, air1219, label="Eq. 12-19")
plt.plot(x_air, air1220, label="Eq. 12-20")
plt.plot(x_air, air1221, label="Eq. 12-21")
plt.legend()
plt.xlabel("x (m)")
plt.ylabel("St")
plt.title("Stanton Number Calculations for Air")
plt.show()

# St Calculation Comparisons for Water
water1217 = []
water1220 = []
water1221 = []
x_water = []
for re in rex_water:
    x_water.append(rex_to_x(rho_water, u_inf, mu_water, re))
    water1217.append(eq12_17(re, Pr_water))
    water1220.append(eq12_20(re, Pr_water))
for re in reh_water:
    water1221.append(eq12_21(re, Pr_water))

plt.plot(x_water, st_water, label="TEXSTAN")
plt.plot(x_water, water1217, label="Eq. 12-17")
plt.plot(x_water, water1220, label="Eq. 12-20")
plt.plot(x_water, water1221, label="Eq. 12-21")
plt.legend()
plt.xlabel("x (m)")
plt.ylabel("St")
plt.title("Stanton Number Calculations for Water")
plt.show()

# St Calculation Comparisons for Acetone
acetone1217 = []
acetone1220 = []
acetone1221 = []
x_acetone = []
for re in rex_acetone:
    x_acetone.append(rex_to_x(rho_acetone, u_inf, mu_acetone, re))
    acetone1217.append(eq12_17(re, Pr_acetone))
    acetone1220.append(eq12_20(re, Pr_acetone))
for re in reh_acetone:
    acetone1221.append(eq12_21(re, Pr_acetone))

plt.plot(x_acetone, st_acetone, label="TEXSTAN")
plt.plot(x_acetone, acetone1217, label="Eq. 12-17")
plt.plot(x_acetone, acetone1220, label="Eq. 12-20")
plt.plot(x_acetone, acetone1221, label="Eq. 12-21")
plt.legend()
plt.xlabel("x (m)")
plt.ylabel("St")
plt.title("Stanton Number Calculations for Acetone")
plt.show()

# St Comparisons between fluids
plt.plot(reh_air, st_air, label="Air: Pr=0.707")
plt.plot(reh_water, st_water, label="Water: Pr=5.43")
plt.plot(reh_acetone, st_acetone, label="Acetone: Pr=2.19")
plt.xlabel("Re_h")
plt.ylabel("St")
plt.legend()
plt.title("Stanton Numbers For All Fluids vs Enthalpy Reynolds Number")
plt.show()

