#!/usr/bin/env python
"""
Example 2: Visualizing the Fourier Transform
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    fs = 1000  # Sampling frequency
    t = np.linspace(0, 1, fs, endpoint=False)
    f1, f2 = 5, 100
    x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    X = np.fft.fft(x)
    freqs = np.fft.fftfreq(len(x), 1/fs)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.title("Time Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(freqs[:len(freqs)//2], np.abs(X[:len(X)//2]))
    plt.title("Frequency Domain (Fourier Transform)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
