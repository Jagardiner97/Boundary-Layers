# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Geometry Conditions
Re_start = 1000
Re_end = 2e5
W = 1
L = 0.2
u_infinity = 15
T_infinity = 300
T_s = 295
#kstart=4

# Fluid 1 Properties: air
Pr_1 = 0.7
rho_1 = 1.177
mu_1 = 1.838e-5
cp_1 = 1005

# Fluid 2 Properties: water vapor at 100C
Pr_2 = 1.0
rho_2 = 0.6
mu_2 = 0.000013
cp_2 = 2003

# Fluid 3 Properties: water at 30C
Pr_3 = 5.0
rho_3 = 995.71
mu_3 = 0.000797
cp_3 = 4180

def calculate_length(Re, mu, v, rho):
    return Re * mu / (v * rho)

print("Air: Pr=0.7")
print(f"x_start = {calculate_length(Re_start, mu_1, u_infinity, rho_1)}")
print(f"x_end = {calculate_length(Re_end, mu_1, u_infinity, rho_1)}")

print("\nSteam: Pr=1.0")
print(f"x_start = {calculate_length(Re_start, mu_2, u_infinity, rho_2)}")
print(f"x_end = {calculate_length(Re_end, mu_2, u_infinity, rho_2)}")

print("\nWater: Pr=5.0")
print(f"x_start = {calculate_length(Re_start, mu_3, u_infinity, rho_3)}")
print((f"x_end = {calculate_length(Re_end, mu_3, u_infinity, rho_3)}"))

def eq10_10(Pr, Rex):
    nux = []
    a = 0.332 * (Pr ** (1/3))
    for re in Rex:
        nux.append(a * np.sqrt(re))
    return nux

def eq10_13(Pr, Rex):
    st = []
    a = 0.332 / (Pr ** (2/3))
    for re in Rex:
        st.append(a / np.sqrt(re))
    return st

def eq10_16(Pr, Reh):
    st = []
    a = 0.2204 / (Pr ** (4/3))
    for reh in Reh:
        st.append(a / reh)
    return st

def eq5_24(qflux, rho, u, c, Ts, Tinf):
    st = []
    a = rho * u * c * (Ts - Tinf)
    for q in qflux:
        st.append(q / a)
    return st

# Get Texstan data for fluid 1
air_out = pd.read_csv("problem 5/air/out.txt", delim_whitespace=True, skiprows=17)
air_85 = pd.read_csv("problem 5/air/ftn85.txt", delim_whitespace=True, skiprows=3)
air_86 = pd.read_csv("problem 5/air/ftn86.txt", delim_whitespace=True, skiprows=3)
air_x = air_out["x"].values
air_reh = air_out["reh"].values
air_x85 = air_85["x/s"].values
air_rex = air_85["rex"].values
air_nu = air_85["nu"].values
air_st = air_85["st"].values
air_qflux = air_86["qflux"].values

# Plots for fluid 1
nu1010_air = eq10_10(Pr_1, air_rex)
plt.plot(air_x85, air_nu, label="TEXSTAN")
plt.plot(air_x85, nu1010_air, label="Eq. 10-10")
plt.xlabel("x (m)")
plt.ylabel("Nu")
plt.legend()
plt.title("Nusselt Number Comparisons for Air")
plt.show()

st1013_air = eq10_13(Pr_1, air_rex)
st1016_air = eq10_16(Pr_1, air_reh)
st524_air = eq5_24(air_qflux, rho_1, u_infinity, cp_1, T_s, T_infinity)
plt.plot(air_x85, air_st, label="TEXSTAN")
plt.plot(air_x85, st1013_air, label="Eq. 10-13")
plt.plot(air_x, st1016_air, label="Eq. 10-16")
plt.plot(air_x85, st524_air, label="Eq. 5-24")
plt.xlabel("x (m)")
plt.ylabel("St")
plt.legend()
plt.title("Stanton Number Calculations for Air")
plt.show()

start = 20
for i in range(5):
    profile = pd.read_csv("problem 5/air/profiles.txt", delim_whitespace=True, skiprows=start, nrows=128)
    y = profile["y(i)"].values
    T = profile["g(eta)"].values
    plt.plot(y, T, label=f"{i}th profile")
plt.xlabel("y (m)")
plt.ylabel("(T-T_s)/(T_inf - T_s)")
plt.legend()
plt.title("Nondimensional Temperature Profiles for Air")
plt.show()

# Get Texstan data for fluid 2
steam_out = pd.read_csv("problem 5/steam/out.txt", delim_whitespace=True, skiprows=17)
steam_85 = pd.read_csv("problem 5/steam/ftn85.txt", delim_whitespace=True, skiprows=3)
steam_86 = pd.read_csv("problem 5/steam/ftn86.txt", delim_whitespace=True, skiprows=3)
steam_x = steam_out["x"].values
steam_reh = steam_out["reh"].values
steam_x85 = steam_85["x/s"].values
steam_rex = steam_85["rex"].values
steam_nu = steam_85["nu"].values
steam_st = steam_85["st"].values
steam_qflux = steam_86["qflux"].values

# Plots for fluid 2
nu1010_steam = eq10_10(Pr_2, steam_rex)
plt.plot(steam_x85, steam_nu, label="TEXSTAN")
plt.plot(steam_x85, nu1010_steam, label="Eq. 10-10")
plt.xlabel("x (m)")
plt.ylabel("Nu")
plt.legend()
plt.title("Nusselt Number Comparisons for Steam")
plt.show()

st1013_steam = eq10_13(Pr_2, steam_rex)
st1016_steam = eq10_16(Pr_2, steam_reh)
st524_steam = eq5_24(steam_qflux, rho_2, u_infinity, cp_2, T_s, T_infinity)
plt.plot(steam_x85, steam_st, label="TEXSTAN")
plt.plot(steam_x85, st1013_steam, label="Eq. 10-13")
plt.plot(steam_x, st1016_steam, label="Eq. 10-16")
plt.plot(steam_x85, st524_steam, label="Eq. 5-24")
plt.xlabel("x (m)")
plt.ylabel("St")
plt.legend()
plt.title("Stanton Number Calculations for Steam")
plt.show()

start = 20
for i in range(5):
    profile = pd.read_csv("problem 5/steam/profiles.txt", delim_whitespace=True, skiprows=start, nrows=128)
    y = profile["y(i)"].values
    T = profile["g(eta)"].values
    plt.plot(y, T, label=f"{i}th profile")
plt.xlabel("y (m)")
plt.ylabel("(T-T_s)/(T_inf - T_s)")
plt.legend()
plt.title("Nondimensional Temperature Profiles for Steam")
plt.show()

# Get Texstan data for fluid 3
water_out = pd.read_csv("problem 5/water/out.txt", delim_whitespace=True, skiprows=17)
water_85 = pd.read_csv("problem 5/water/ftn85.txt", delim_whitespace=True, skiprows=3)
water_86 = pd.read_csv("problem 5/water/ftn86.txt", delim_whitespace=True, skiprows=3)
water_x = water_out["x"].values
water_reh = water_out["reh"].values
water_x85 = water_85["x/s"].values
water_rex = water_85["rex"].values
water_nu = water_85["nu"].values
water_st = water_85["st"].values
water_qflux = water_86["qflux"].values

# Plots for fluid 2
nu1010_water = eq10_10(Pr_3, water_rex)
plt.plot(water_x85, water_nu, label="TEXSTAN")
plt.plot(water_x85, nu1010_water, label="Eq. 10-10")
plt.xlabel("x (m)")
plt.ylabel("Nu")
plt.legend()
plt.title("Nusselt Number Comparisons for Water")
plt.show()

st1013_water = eq10_13(Pr_3, water_rex)
st1016_water = eq10_16(Pr_3, water_reh)
st524_water = eq5_24(water_qflux, rho_3, u_infinity, cp_3, T_s, T_infinity)
plt.plot(water_x85, water_st, label="TEXSTAN")
plt.plot(water_x85, st1013_water, label="Eq. 10-13")
plt.plot(water_x, st1016_water, label="Eq. 10-16")
plt.plot(water_x85, st524_water, label="Eq. 5-24")
plt.xlabel("x (m)")
plt.ylabel("St")
plt.legend()
plt.title("Stanton Number Calculations for Water")
plt.show()

start = 20
for i in range(5):
    profile = pd.read_csv("problem 5/water/profiles.txt", delim_whitespace=True, skiprows=start, nrows=128)
    y = profile["y(i)"].values
    T = profile["g(eta)"].values
    plt.plot(y, T, label=f"{i}th profile")
plt.xlabel("y (m)")
plt.ylabel("(T-T_s)/(T_inf - T_s)")
plt.legend()
plt.title("Nondimensional Temperature Profiles for Water")
plt.show()

# Compare All
plt.plot(air_x85, air_st, label="Air")
plt.plot(steam_x85, steam_st, label="Steam")
plt.plot(water_x85, water_st, label="Water")
plt.xlabel("x (m)")
plt.ylabel("St")
plt.legend()
plt.title("Stanton Number Comparisons for All Fluids")
plt.show()

plt.plot(air_x85, air_nu, label="Air")
plt.plot(steam_x85, steam_nu, label="Steam")
plt.plot(water_x85, water_nu, label="Water")
plt.xlabel("x (m)")
plt.ylabel("Nu")
plt.legend()
plt.title("Nusselt Number Comparisons for All Fluids")
plt.show()
