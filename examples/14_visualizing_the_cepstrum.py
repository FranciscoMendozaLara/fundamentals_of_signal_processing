#!/usr/bin/env python
"""
Example 14: Visualizing the Cepstrum
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

def main():
    fs = 1000
    t = np.linspace(0, 1, fs, endpoint=False)
    source = np.sin(2 * np.pi * 50 * t)
    filter_response = np.exp(-t)
    signal = source * filter_response
    spectrum = np.abs(fft(signal))
    log_spectrum = np.log(spectrum + 1e-10)
    cepstrum = np.abs(ifft(log_spectrum))

    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, signal)
    plt.title("Time-Domain Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(3, 1, 2)
    plt.plot(log_spectrum[:fs//2])
    plt.title("Log-Magnitude Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Log Magnitude")

    plt.subplot(3, 1, 3)
    plt.plot(cepstrum[:fs//2])
    plt.title("Cepstrum")
    plt.xlabel("Quefrency (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
