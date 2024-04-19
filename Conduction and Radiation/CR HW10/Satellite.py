# Import libraries
import math
import matplotlib.pyplot as plt
import numpy as np

# Surface Properties
d_sat = 1
d_earth = 1.29e7
T_earth = 300
R_earth_to_sun = 1.497e11
d_sun = 1.39e9
T_sun = 5780
T_space = 3

# View Factors
F_12 = 0.3417
F_13 = 0.000005389

def surface_resistance(epsilon, diameter):
    surface_area = diameter * diameter
    return (1 - epsilon) / (surface_area * epsilon)

def T_to_Eb(temperature):
    return math.pow(temperature, 4) * 5.67e-8

def Eb_to_T(Eb):
    Eb = Eb / 5.67e-8
    return math.pow(Eb, 0.25)

def space_resistance(diameter, view_factor):
    surface_area = diameter * diameter
    return 1 / (surface_area * view_factor)


# Calculate Resistances and Blackbody radiation
R_12 = space_resistance(d_sat, F_12)
R_13 = space_resistance(d_sat, F_13)
Eb_2 = T_to_Eb(T_earth)
Eb_3 = T_to_Eb(T_sun)

def satellite_temp(q_sat, epsilon_sat, day=1):
    R_s1 = surface_resistance(epsilon_sat, d_sat)
    c1 = 1 / (R_s1 + R_12)
    c2 = 1 / (R_s1 + R_13)
    Eb_1 = (q_sat + Eb_2 * c1 + day * Eb_3 * c2) / (c1 + day * c2)
    return Eb_to_T(Eb_1)


# Determine the Steady State Temperatures
print("Steady State Satellite Temperatures:")
print(f"Day: {satellite_temp(100, 0.5, 1):.2f}")
print(f"Night: {satellite_temp(100, 0.5, 0):.2f}")

# Plot Steady State Day Side Temperature as a Function of epsilon_sat
e_sat = np.linspace(0.01, 1, 100)
temps = []
q0_temps = []
for eps in e_sat:
    temps.append(satellite_temp(100, eps, 1))
    q0_temps.append(satellite_temp(0, eps, 1))
plt.plot(e_sat, temps, label="q_sat=100")
plt.plot(e_sat, q0_temps, label="q_sat=0")
plt.legend()
plt.xlabel("epsilon_sat")
plt.ylabel("Temperature (K)")
plt.title("Steady State Day Side Satellite Temperature vs Satellite Emissivity")
plt.show()

