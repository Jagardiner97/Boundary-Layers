import numpy as np
from pyfluids import Fluid, FluidsList, Input

class PipeSetup:
    def __init__(self, rho, D, mu, k, Pr):
        self.rho = rho
        self.D = D
        self.mu = mu
        self.k = k
        self.Pr = Pr
        self.Re = rho * D * 8 / mu

    def get_Re(self):
        return self.Re


def interpolate(T, T1, T2, props1, props2):
    ratio = (T - T1) / (T2 - T1)
    props = []
    for i in range(len(props1)):
        props.append((props2[i] - props1[i]) * ratio + props1[i])
    return props


# Initialize properties for air at 90C 1atm
case_a = PipeSetup(rho=0.973, D=0.025, mu=2.139e-5, k=0.03024, Pr=0.713)
print(f"a): Re={case_a.get_Re():.1f}")
print(10**4)
case_b = PipeSetup(rho=0.973, D=0.006, mu=2.139e-5, k=0.03024, Pr=0.713)

# Interpolate Properties and initialize object for Hydrogen at 90 C (case c)
hydrogen_props = interpolate(90+273.15, 350, 400, [0.0702, 99.4e-7, 20.33, 0.703], [0.0614, 10.91e-6, 22.12, 0.715])
case_c = PipeSetup(rho=hydrogen_props[0], D=0.025, mu=hydrogen_props[1], k=hydrogen_props[2], Pr=hydrogen_props[3])

# Interpolate Properties and initialize object for Liquid Oxygen at -200 C (case d)
lox_props = interpolate(73, 68, 76, [1246, 38.8e-5, 0.179, 3.61], [1209, 30.0e-5, 0.17, 2.95])
case_d = PipeSetup(rho=lox_props[0], D=0.025, mu=lox_props[1], k=lox_props[2], Pr=lox_props[3])

# Interpolate Properties and initialize object for Liquid Water at 38 C (case e)
lw_props = interpolate(38, 30, 40, [995.6, 79.77e-5, 0.615, 5.42], [992.2, 65.31e-5, 0.629, 4.34])
case_e = PipeSetup(rho=lw_props[0], D=0.025, mu=lw_props[1], k=lw_props[2], Pr=lw_props[3])

# Initialize object for Liquid Sodium at 200 C(case f)
case_f = PipeSetup(rho=905, D=0.025, mu=0.450/1000, k=81.5, Pr=0.0074)

# Interpolate Properties and initialize object for Engine Oil at 90 C (case g)
oil_props = interpolate(90, 75, 100, [855, 39.4e-3, 13.8e-2, 598], [840, 17.2e-3, 13.6e-2, 280])
case_g = PipeSetup(rho=oil_props[0], D=0.025, mu=oil_props[1], k=oil_props[2], Pr=oil_props[3])

# Get Air properties at 10atm 90 C
air = Fluid(FluidsList.Air).with_state(
    Input.pressure(1000e3), Input.temperature(90)
)
case_h = PipeSetup(rho=air.density, D=0.025, mu=air.dynamic_viscosity, k=air.conductivity, Pr=air.prandtl)

print("test")
