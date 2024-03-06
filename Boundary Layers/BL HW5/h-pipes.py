import numpy as np


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


case_a = PipeSetup(rho=0.973, D=0.025, mu=2.139e-5, k=0.03024, Pr=0.713)
print(f"a): Re={case_a.get_Re():.1f}")
print(10**4)
