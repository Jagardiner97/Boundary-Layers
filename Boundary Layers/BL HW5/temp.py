import matplotlib.pyplot as plt
import math
import numpy as np

def get_y(x_range, n_terms):
    y = []
    for x_val in x_range:
        y_x = 0
        for n in range(n_terms):
            y_x += 2 / (math.pi * (2 * n - 1)) * math.sin((2 * n - 1) * x_val)
        y.append(y_x)
    return y

def y_actual(x_range):
    y = []
    for x_val in x_range:
        if x_val <=0:
            y.append(-0.5)
        else:
            y.append(0.5)
    return y


x = np.linspace(-math.pi, math.pi, 100)
ns = [1, 3, 7, 10]
y_act = y_actual(x)
plt.plot(x, y_act, label="f(x)")
for num_terms in ns:
    plt.plot(x, get_y(x, num_terms), label=f"s_{num_terms}(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Comparing f(x) to the Approximations")
plt.show()
