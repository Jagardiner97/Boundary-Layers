import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
x = []
y = []
v = []
u = []
for i in range(1, 1000+1):
    if i < 10:
        filename = f'piv-data/B0000{i}.dat'
    elif i < 100:
        filename = f'piv-data/B000{i}.dat'
    elif i < 1000:
        filename = f'piv-data/B00{i}.dat'
    else:
        filename = f'piv-data/B0{i}.dat'
    data = pd.read_csv(filename, header=None, delimiter=" ", skiprows=3)
    if len(x) == 0:
        x_raw = data.iloc[:, 0]
        for x_val in x_raw:
            x_adjusted = -1 * x_val
            if x_adjusted not in x:
                x.append(x_adjusted)
    if len(y) == 0:
        y_raw = data.iloc[:, 1].values
        for y_val in y_raw:
            if y_val not in y:
                y.append(y_val)
    vx = data.iloc[:, 2].values
    vy = data.iloc[:, 3].values
    v_row = []
    u_row = []
    for j in range(len(vx)):
        x_index = len(u_row)
        if x_index % len(x) == 0 and x_index != 0:
            v.append(v_row)
            u.append(u_row)
            v_row = []
            u_row = []
        v_row.append(vx[i])
        u_row.append(vy[i])
print(f"Done in {time.time()-start:.2f} s")
print(f"x: {len(x)}")
print(f"y: {len(y)}")
