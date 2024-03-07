import numpy as np
import math
from pyfluids import Fluid, FluidsList, Input

class PipeSetup:
    def __init__(self, rho, D, mu, k, Pr, type):
        self.rho = rho
        self.D = D
        self.mu = mu
        self.k = k
        self.Pr = Pr
        self.type = type
        self.equation = None
        self.equation_list = ["14-7", "8-17 (Laminar)", "14-10", "14-9", "14-8", "14-6"]
        self.Re = rho * D * 8 / mu
        self.nu = self.get_nu()
        self.h = self.nu * k / D


    def get_Re(self):
        return self.Re

    def get_nu(self):
        if self.type == 0 and self.Re > 2300:
            self.equation = self.equation_list[0]
            return 0.022 * (self.Pr**0.5) * (self.Re**0.8)
        elif self.Re < 2300:
            self.equation = self.equation_list[1]
            return 4.364
        elif self.type == 2:
            self.equation = self.equation_list[2]
            return 6.3 + 0.0167 * self.Re**0.85 * self.Pr**0.93
        elif 10**4 < self.Re < 10**6:
            a = 0.88 - 0.24 / (4 + self.Pr)
            b = 0.333 + 0.5 * math.exp(-0.6 * self.Pr)
            self.equation = self.equation_list[3]
            return 5 + 0.015 * self.Re**a * self.Pr**b
        elif 2300 < self.Re < 5e6:
            self.equation = self.equation_list[4]
            if 10**4 < self.Re < 5 * 10**4:
                cf2 = 0.039 * self.Re**(-0.25)
            elif 3 * 10**4 < self.Re < 10**6:
                cf2 = 0.023 * self.Re**(-0.2)
            else:
                cf2 = (2.236 * math.log(self.Re) - 4.639)**(-2)
            return ((self.Re - 1000) * self.Pr * cf2) / (1.0 + 12.7 * math.sqrt(cf2 * (self.Pr**2/3 - 1.0)))
        else:
            self.equation = self.equation_list[5]
            return (0.023 * self.Re**0.8 * self.Pr) / (0.88 + 2.03 * (self.Pr**2/3 - 0.78) * self.Re**(-0.1))

    def get_h(self):
        return self.h

    def print_properties(self):
        print(f"rho = {self.rho:.4f}, D = {self.D}, mu = {self.mu:.7f}, k = {self.k:.5f}, Pr = {self.Pr:.3f}")

    def get_results(self):
        print(f"Re = {self.Re:.2f}, Nu = {self.nu:.2f}, h = {self.h:.2f}, solved using Eq. {self.equation}")


def interpolate(T, T1, T2, props1, props2):
    ratio = (T - T1) / (T2 - T1)
    props = []
    for i in range(len(props1)):
        props.append((props2[i] - props1[i]) * ratio + props1[i])
    return props


# Fluid types 0=gas, 1=liquid, 2=liquid metal
# Initialize properties for air at 90C 1atm
print("a) Air, 90 C, 1 atm")
case_a = PipeSetup(rho=0.973, D=0.025, mu=2.139e-5, k=0.03024, Pr=0.713, type=0)
case_a.print_properties()
case_a.get_results()

# Initialize setup for case b
print("\nb) Air 90 C, 1 atm, D = 0.6cm")
case_b = PipeSetup(rho=0.973, D=0.006, mu=2.139e-5, k=0.03024, Pr=0.713, type=0)
case_b.print_properties()
case_b.get_results()

# Interpolate Properties and initialize object for Hydrogen at 90 C (case c)
print("\nc) Hydrogen 90 C, 1 atm")
hydrogen_props = interpolate(90+273.15, 350, 400, [0.0702, 99.4e-7, 20.33, 0.703], [0.0614, 10.91e-6, 22.12, 0.715])
case_c = PipeSetup(rho=hydrogen_props[0], D=0.025, mu=hydrogen_props[1], k=hydrogen_props[2], Pr=hydrogen_props[3], type=0)
case_c.print_properties()
case_c.get_results()

# Interpolate Properties and initialize object for Liquid Oxygen at -200 C (case d)
print("\nd) Liquid Oxygen at -200 C")
lox_props = interpolate(73, 68, 76, [1246, 38.8e-5, 0.179, 3.61], [1209, 30.0e-5, 0.17, 2.95])
case_d = PipeSetup(rho=lox_props[0], D=0.025, mu=lox_props[1], k=lox_props[2], Pr=lox_props[3], type=1)
case_d.print_properties()
case_d.get_results()

# Interpolate Properties and initialize object for Liquid Water at 38 C (case e)
print("\ne) Liquid Water at 38 C")
lw_props = interpolate(38, 30, 40, [995.6, 79.77e-5, 0.615, 5.42], [992.2, 65.31e-5, 0.629, 4.34])
case_e = PipeSetup(rho=lw_props[0], D=0.025, mu=lw_props[1], k=lw_props[2], Pr=lw_props[3], type=1)
case_e.print_properties()
case_e.get_results()

# Initialize object for Liquid Sodium at 200 C(case f)
print("\nf) Liquid Sodium at 200 C")
case_f = PipeSetup(rho=905, D=0.025, mu=0.450/1000, k=81.5, Pr=0.0074, type=2)
case_f.print_properties()
case_f.get_results()

# Interpolate Properties and initialize object for Engine Oil at 90 C (case g)
print("\ng) Engine Oil at 90 C")
oil_props = interpolate(90, 75, 100, [855, 39.4e-3, 13.8e-2, 598], [840, 17.2e-3, 13.6e-2, 280])
case_g = PipeSetup(rho=oil_props[0], D=0.025, mu=oil_props[1], k=oil_props[2], Pr=oil_props[3], type=1)
case_g.print_properties()
case_g.get_results()

# Get Air properties at 10atm 90 C
print("\nh) Air at 90 C, 1000 kpa")
air = Fluid(FluidsList.Air).with_state(
    Input.pressure(1000e3), Input.temperature(90)
)
case_h = PipeSetup(rho=air.density, D=0.025, mu=air.dynamic_viscosity, k=air.conductivity, Pr=air.prandtl, type=0)
case_h.print_properties()
case_h.get_results()
