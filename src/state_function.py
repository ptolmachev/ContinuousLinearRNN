'''
description of sigma(h) state function which is a piecewise linear function with the slopes k and lambda'
'''

import numpy as np

def s(lmbd, k, h):
    bounds = (-1.0 / lmbd, 1.0 / lmbd)
    c = (1 - k / lmbd) #
    x = 1.0 * (h <= bounds[0])
    z = 1.0 * (h >= bounds[1])
    y = (np.ones_like(h) - x - z)
    return (k * h - c) * x + (lmbd * h) * y + (k * h + c) * z

def der_s(lmbd, k, h):
    bounds = (-1.0 / lmbd, 1.0 / lmbd)
    x = 1.0 * (h <= bounds[0])
    z = 1.0 * (h >= bounds[1])
    y = (np.ones_like(h) - x - z)
    return k * (x + z) + lmbd * h * y

if __name__ == '__main__':
    from matplotlib import pyplot as plt
    x = np.linspace(-10,10, 100)
    plt.plot(x, s(0.5, 0.1, x))
    plt.show()




