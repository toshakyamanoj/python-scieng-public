import numpy as np
import matplotlib.pyplot as plt


def sinc(x):
    z = np.where(x == 0.0, 1.0, np.sin(x) / x)
    return z


x = np.linspace(-10, 10, 255)
y = sinc(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y)
ax.axhline(color="gray", zorder=-1)
ax.axvline(color="gray", zorder=-1)
plt.show()

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

sinc function written to process NumPy array
inputs fast and efficiently
"""
