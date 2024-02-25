import numpy as np
import matplotlib.pyplot as plt

Ac = 0.1
P = 0.05
k = 5
rho = 5000
c = 500
L = 0.09
Tl = 20
qh = 100
alpha = k / (rho * c)
tau_diff = L**2 / (4 * alpha)
sum_lim = [10, 50, 300]

def theta(x, t, sum_lim):
    temp = 0
    for i in range(1, sum_lim+1):
        iterm = i * 2 - 1
        ai = 2 * L * qh / (iterm * np.pi * k * Ac)
        lambda_i = iterm * np.pi / (2 * L)
        temp += ai * np.cos(lambda_i * x) * np.exp(-lambda_i**2 * alpha * t)
    return temp

def dtheta(x, t, sum_lim):
    temp = 0
    for i in range(1, sum_lim):
        iterm = i * 2 - 1
        a = qh / (k * Ac)
        lamda_i = iterm * np.pi / (2 * L)
        xterm = a * np.sin(lamda_i * x)
        tterm = np.exp(-lamda_i**2 * alpha * t)
        temp += xterm * tterm
    return temp


xrange = np.linspace(0, L, 50)
for limit in sum_lim:
    t_0 = []
    t_inf = []
    t_05tdiff = []
    t_2tdiff = []
    xl = []
    for xval in xrange:
        t_0.append(theta(xval, 0, limit) + 20)
        t_inf.append(theta(xval, 1e9, limit) + 20)
        t_05tdiff.append(theta(xval, 0.5 * tau_diff, limit) + 20)
        t_2tdiff.append(theta(xval, 2 * tau_diff, limit) + 20)
        xl.append(xval/L)

    plt.plot(xl, t_0, label="t=0")
    plt.plot(xl, t_05tdiff, label="t=0.5tau_diff")
    plt.plot(xl, t_2tdiff, label="t=2tau_diff")
    plt.plot(xl, t_inf, label="t->inf")
    plt.xlabel("x/L")
    plt.ylabel("T (C)")
    plt.ylim((0, 75))
    plt.legend()
    plt.title(f"Temperature Profiles in the Rod: {limit} Term Solution")
    plt.show()

times = np.linspace(0, 5 * tau_diff, 100)
qconv = []
for tval in times:
    qconv.append(k * Ac * dtheta(L, tval, 50))
plt.plot(times, qconv, label="q_tip")
plt.xlabel("t (s)")
plt.ylabel("q_tip (W)")
plt.title("Convection from Tip vs Time")
plt.show()
