import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv('piv-data/B00001.dat', delimiter=' ', header=None, skiprows=3)
data2 = pd.read_csv('piv-data/B00002.dat', delimiter=' ', header=None, skiprows=3)

for j in range(4):
    x1 = data1.iloc[:,j]
    x2 = data2.iloc[:,j]

    diffs = []
    for i in range(max(len(x1), len(x2))):
        diff = x1[i] - x2[i]
        if diff != 0:
            diffs.append([i, diff])
    print(diffs)
