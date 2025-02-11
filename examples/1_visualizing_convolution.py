#!/usr/bin/env python
"""
Example 1: Visualizing Convolution
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

def main():
    t = np.linspace(0, 10, 1000)
    x = np.heaviside(t, 1)               # Unit step function
    h = np.exp(-t) * np.heaviside(t, 1)    # Exponential decay
    dt = t[1] - t[0]
    y = convolve(x, h, mode='full')[:len(t)] * dt

    plt.figure(figsize=(10, 6))
    plt.plot(t, x, label='Input: x(t)')
    plt.plot(t, h, label='Impulse Response: h(t)')
    plt.plot(t, y, label='Output: y(t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Convolution of x(t) and h(t)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
