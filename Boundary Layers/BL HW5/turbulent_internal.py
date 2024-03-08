import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set problem geometry conditions
Re_d_min = 50_000
Re_d_max = 100_000
Pr_fluids = [0.01, 0.7, 10, 100]
T_entrance = 280#K
D_h = 3.5/100#cm
L = 12
q_flux = 250
#epsilon_m/nu = aRe^b, a=0.005, b=0.9
# Van Driest damping function
kappa = 0.4
A_plus = 26
#ktmu=7
#ktme=2
#Turbulent Prandtl number 0.9, fxx=0.9

# Define Equations
def eq14_5(Re, Pr, cf2):
    # No Re or Pr ranges specified
    return Re * Pr * cf2 / (0.88 + 13.39 * (Pr**(2/3) - 0.78) * np.sqrt(cf2))

def eq14_6(Re, Pr):
    # No Re or Pr ranges specified
    return 0.023 * Re**0.8 * Pr / (0.88 + 2.03 * (Pr**(2/3) - 0.78) * Re**(-0.1))

def eq14_7(Re, Pr):
    # For gases (0.5 < Pr < 1.0)
    return 0.022 * Pr**0.5 * Re**0.8

def eq14_8(Re, Pr, cf2):
    # 0.5 < Pr < 2000, 2300 < Re < 5e6
    return (Re - 1000) * Pr * cf2 / (1.0 + 12.7 * np.sqrt(cf2 * (Pr**(2/3) - 1.0)))

def eq14_9(Re, Pr):
    # 0.1 < Pr < 10**4, 10**4 < Re < 10**6
    a = 0.88 - 0.24 / (4 + Pr)
    b = 0.333 + 0.5 * np.exp(-.6 * Pr)
    return 5 + 0.015 * Re**a * Pr**b

def dittus_boelter_heating(Re, Pr):
    return 0.024 * Re**0.8 * Pr**0.4

def dittus_boelter_cooling(Re, Pr):
    return 0.026 * Re**0.8 * Pr**0.4

def eq14_10(Re, Pr):
    # Liquid metals
    return 6.3 + 0.0167 * Re**0.85 * Pr**0.93


# Material Properties
# Fluid 1: Pr=0.01 (Mercury at 200C)
Pr_hg = 0.01
rho_hg = 13110
mu_hg = 1.01 / 1000
cp_hg = 136
k_hg = 12.4

# Fluid 2: Pr=0.7 (Air at 300K)
Pr_air = 0.7
rho_air = 1.177
mu_air = 1.838e-5
cp_air = 1005
k_air = 26.38 / 1000

# Fluid 3: Pr=10 (Water at 10C)
Pr_water = 10
rho_water = 999.8
mu_water = 13.08e-4
cp_water = 4193
k_water = 0.582

# Fluid 4: Pr=100 (Hydraulic Fluid at 75C Table A-15)
Pr_hf = 100
rho_hf = 815
mu_hf = 49.9e-4
cp_hf = 2101
k_hf = 10.8e-2

# Compare to equations 14-5 through 14-9 for Pr=0.7, compare profiles (especially fully developed compared to Eq. 14-4)
# For Pr = 0.01, compare with 14-10
# For Pr = 100, compare with Eq. 14-8
# Compare with figs 14-6, 14-7, 14-8

# Read Texstan data
hg_low = pd.read_csv("Low Re Results/mercury.txt", delim_whitespace=True, skiprows=21)
hg_high = pd.read_csv("High Re Results/mercury.txt", delim_whitespace=True, skiprows=21)
air_low = pd.read_csv("Low Re Results/air.txt", delim_whitespace=True, skiprows=21)
air_high = pd.read_csv("High Re Results/air.txt", delim_whitespace=True, skiprows=21)
water_low = pd.read_csv("Low Re Results/water.txt", delim_whitespace=True, skiprows=21)
water_high = pd.read_csv("High Re Results/water.txt", delim_whitespace=True, skiprows=21)
hf_low = pd.read_csv("Low Re Results/hydraulic.txt", delim_whitespace=True, skiprows=21)
hf_high = pd.read_csv("High Re Results/hydraulic.txt", delim_whitespace=True, skiprows=21)

hg_x_low = hg_low["x/dh"].values
hg_x_high = hg_high["x/dh"].values
air_x_low = air_low["x/dh"].values
air_x_high = air_high["x/dh"].values
water_x_low = water_low["x/dh"].values
water_x_high = water_high["x/dh"].values
hf_x_low = hf_low["x/dh"].values
hf_x_high = hf_high["x/dh"].values

hg_cf2_low = hg_low["cf2"].values
hg_cf2_high = hg_high["cf2"].values
air_cf2_low = air_low["cf2"].values
air_cf2_high = air_high["cf2"].values
water_cf2_low = water_low["cf2"].values
water_cf2_high = water_high["cf2"].values
hf_cf2_low = hf_low["cf2"].values
hf_cf2_high = hf_high["cf2"].values

hg_nu_low = hg_low["nu"].values
hg_nu_high = hg_high["nu"].values
air_nu_low = air_low["nu"].values
air_nu_high = air_high["nu"].values
water_nu_low = water_low["nu"].values
water_nu_high = water_high["nu"].values
hf_nu_low = hf_low["nu"].values
hf_nu_high = hf_high["nu"].values

air145_low = []
air146_low = []
air147_low = []
air148_low = []
air149_low = []
for i in range(len(air_x_low)):
    air145_low.append(eq14_5(Re_d_min, Pr_air, air_cf2_low[i]))
    air146_low.append(eq14_6(Re_d_min, Pr_air))
    air147_low.append(eq14_7(Re_d_min, Pr_air))
    air148_low.append(eq14_8(Re_d_min, Pr_air, air_cf2_low[i]))
    air149_low.append(eq14_9(Re_d_min, Pr_air))
plt.plot(air_x_low, air_nu_low, label="TEXSTAN")
plt.plot(air_x_low, air145_low, label="Eq. 14-5")
plt.plot(air_x_low, air146_low, label="Eq. 14-6")
plt.plot(air_x_low, air147_low, label="Eq. 14-7")
plt.plot(air_x_low, air148_low, label="Eq. 14-8")
plt.plot(air_x_low, air149_low, label="Eq. 14-9")
plt.xlabel("x/D_h")
plt.xlim([0, 300])
plt.ylim([80, 150])
plt.ylabel("Nu")
plt.legend()
plt.title("Numerical and Correlation Results for Pr=0.7, Re=50,000")
plt.show()

air145_high = []
air146_high = []
air147_high = []
air148_high = []
air149_high = []
for i in range(len(air_x_low)):
    air145_high.append(eq14_5(Re_d_max, Pr_air, air_cf2_high[i]))
    air146_high.append(eq14_6(Re_d_max, Pr_air))
    air147_high.append(eq14_7(Re_d_max, Pr_air))
    air148_high.append(eq14_8(Re_d_max, Pr_air, air_cf2_high[i]))
    air149_high.append(eq14_9(Re_d_max, Pr_air))
plt.plot(air_x_high, air_nu_high, label="TEXSTAN")
plt.plot(air_x_high, air145_high, label="Eq. 14-5")
plt.plot(air_x_high, air146_high, label="Eq. 14-6")
plt.plot(air_x_high, air147_high, label="Eq. 14-7")
plt.plot(air_x_high, air148_high, label="Eq. 14-8")
plt.plot(air_x_high, air149_high, label="Eq. 14-9")
plt.xlabel("x/D_h")
plt.ylabel("Nu")
plt.xlim([0, 300])
plt.ylim([140, 250])
plt.legend()
plt.title("Numerical and Correlation Results for Pr=0.7, Re=100,000")
plt.show()

hg_nu10_low = []
hg_nu10_high = []
for i in range(len(hg_x_low)):
    hg_nu10_low.append(eq14_10(Re_d_min, Pr_hg))
    hg_nu10_high.append(eq14_10(Re_d_max, Pr_hg))
plt.plot(hg_x_low, hg_nu_low, label="TEXSTAN Re=50,000")
plt.plot(hg_x_high, hg_nu_high, label="TEXSTAN Re=100,000")
plt.plot(hg_x_low, hg_nu10_low, label="Eq. 14-10 Re=50,000")
plt.plot(hg_x_high, hg_nu10_high, label="Eq. 14-10 Re=100,000")
plt.xlabel("x/D_h")
plt.ylabel("Nu")
plt.xlim([0, 300])
plt.ylim([0, 25])
plt.legend()
plt.title("Numerical and Correlation Results for Pr=0.01")
plt.show()

water_nu8_low = []
water_nu8_high = []
for i in range(len(hg_x_low)):
    water_nu8_low.append(eq14_8(Re_d_min, Pr_water, hf_cf2_low[i]))
    water_nu8_high.append(eq14_8(Re_d_max, Pr_water, hf_cf2_high[i]))
plt.plot(water_x_low, water_nu_low, label="TEXSTAN Re=50,000")
plt.plot(water_x_high, water_nu_high, label="TEXSTAN Re=100,000")
plt.plot(water_x_low, water_nu8_low, label="Eq. 14-8 Re=50,000")
plt.plot(water_x_high, water_nu8_high, label="Eq. 14-8 Re=100,000")
plt.xlabel("x/D_h")
plt.ylabel("Nu")

plt.legend()
plt.title("Numerical and Correlation Results for Pr=10")
plt.show()
hf_nu8_low = []
hf_nu8_high = []
for i in range(len(hg_x_low)):
    hf_nu8_low.append(eq14_8(Re_d_min, Pr_hf, hf_cf2_low[i]))
    hf_nu8_high.append(eq14_8(Re_d_max, Pr_hf, hf_cf2_high[i]))
plt.plot(hf_x_low, hf_nu_low, label="TEXSTAN Re=50,000")
plt.plot(hf_x_high, hf_nu_high, label="TEXSTAN Re=100,000")
plt.plot(hf_x_low, hf_nu8_low, label="Eq. 14-8 Re=50,000")
plt.plot(hf_x_high, hf_nu8_high, label="Eq. 14-8 Re=100,000")
plt.xlabel("x/D_h")
plt.ylabel("Nu")
plt.legend()
plt.title("Numerical and Correlation Results for Pr=100")
plt.show()

hg_nu_low_scaled = []
hg_nu_high_scaled = []
air_nu_low_scaled = []
air_nu_high_scaled = []
water_nu_low_scaled = []
water_nu_high_scaled = []
hf_nu_low_scaled = []
hf_nu_high_scaled = []
nu_inf_hg_low = hg_nu_low[-1]
nu_inf_hg_high = hg_nu_high[-1]
nu_inf_air_low = air_nu_low[-1]
nu_inf_air_high = air_nu_high[-1]
nu_inf_water_low = water_nu_low[-1]
nu_inf_water_high = water_nu_high[-1]
nu_inf_hf_low = hf_nu_low[-1]
nu_inf_hf_high = hf_nu_high[-1]
for i in range(len(air_nu_low)):
    hg_nu_low_scaled.append(hg_nu_low[i] / nu_inf_hg_low)
    hg_nu_high_scaled.append(hg_nu_high[i] / nu_inf_hg_high)
    air_nu_low_scaled.append(air_nu_low[i] / nu_inf_air_low)
    air_nu_high_scaled.append(air_nu_high[i] / nu_inf_air_high)
    water_nu_low_scaled.append(water_nu_low[i] / nu_inf_water_low)
    water_nu_high_scaled.append(water_nu_high[i] / nu_inf_water_high)
    hf_nu_low_scaled.append(hf_nu_low[i] / nu_inf_hf_low)
    hf_nu_high_scaled.append(hf_nu_high[i] / nu_inf_hf_high)

# Figure 14-6
plt.plot(hg_x_low, hg_nu_low_scaled, label='Re=50,000')
plt.plot(hg_x_low, hg_nu_high_scaled, label='Re=100,000')
plt.legend()
plt.xlabel("x/D")
plt.ylabel("Nu_x/Nu_inf")
plt.xlim([0, 40])
plt.ylim([1.0, 2.0])
plt.title("Influence of Re at constant Pr=0.01 for Liquid Metal")
plt.show()

# Figure 14-7
plt.plot(hg_x_high, hg_nu_high_scaled, label='Pr=0.01')
plt.plot(air_x_high, air_nu_high_scaled, label='Pr=0.7')
plt.plot(water_x_high, water_nu_high_scaled, label='Pr=10')
plt.plot(hf_x_high, hf_nu_high_scaled, label='Pr=100')
plt.xlabel("x/D")
plt.ylabel("Nu_x/Nu_inf")
plt.legend()
plt.xlim([0, 40])
plt.ylim([1.0, 1.3])
plt.title("Influence of Pr at constant Re=100,000")
plt.show()

# Figure 14-8
plt.plot(air_x_low, air_nu_low_scaled, label='Re=50,000')
plt.plot(air_x_low, air_nu_high_scaled, label='Re=100,000')
plt.legend()
plt.xlabel("x/D")
plt.ylabel("Nu_x/Nu_inf")
plt.xlim([0, 40])
plt.ylim([1.0, 1.2])
plt.title("Influence of Re at constant Pr=0.7 for Air")
plt.show()

skip = 25
locations = ["0", "5", "50", "100", "end"]
for i in range(5):
    air_low_profiles = pd.read_csv("Low Re Results/air_profiles.txt", delim_whitespace=True, skiprows=skip, nrows=83)
    plt.plot(air_low_profiles["y(i)"].values, air_low_profiles["f(1,i)"].values, label=f"{locations[i]}")
    skip += 87
plt.xlabel("y (m)")
plt.ylabel("T (K)")
plt.legend()
plt.title("Temperature Profiles at x/D Locations")
plt.show()
