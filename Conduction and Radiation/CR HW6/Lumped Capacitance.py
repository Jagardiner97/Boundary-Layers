import numpy as np
import matplotlib.pyplot as plt
from scipy.special import lambertw

r = 0.0015
rho = 7500
c = 820
k = 75
q_dot = 0.1
delta_t = 10
h_min = 30
h_max = 300
As = np.pi * 4 * r**2
V = np.pi * 4 / 3 * r**3

def convection(c, rho, T, V, qdot, As, t):
    B = c * T * V * rho
    A = lambertw(-np.exp(-qdot * t / (c * T * V * rho)) * qdot * t / B)
    return (B * A + qdot * T) / (As * t * T)

def time(rho, V, As, c, h, delta_t, q_dot):
    return -rho * V * c / (h * As) * np.log(1 - h * delta_t * As / q_dot)


t_min = time(rho, V, As, c, h_min, delta_t, q_dot)
t_max = time(rho, V, As, c, h_max, delta_t, q_dot)

print("t_min:", t_min)
print("t_max:", t_max)

times = []
hs = []
h = h_min
while h <= h_max:
    hs.append(h)
    t = time(rho, V, As, c, h, delta_t, q_dot)
    times.append(t)
    h += 3
plt.plot(times, hs)
plt.xlabel("time (s)")
plt.ylabel("h (W/m^2*K)")
plt.title("h vs t")
plt.show()

ts = np.linspace(t_min, t_max, 100)
h_calculated = []
for time in ts:
    h_calculated.append(convection(c, rho, delta_t, V, q_dot, As, time))
plt.plot(ts, h_calculated)
plt.xlabel("time (s)")
plt.ylabel("h (W/m^2 * K)")
plt.title("h calculated from t")
plt.show()

print(convection(c, rho, delta_t, V, q_dot, As, t_min))
print("V", V)
print("As", As)
