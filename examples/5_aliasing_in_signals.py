#!/usr/bin/env python
"""
Example 5: Aliasing in Signals
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    fs_true = 1000      # True sampling rate
    f_signal = 50       # Signal frequency
    t = np.linspace(0, 1, fs_true, endpoint=False)
    signal = np.sin(2 * np.pi * f_signal * t)

    # Simulate low and high sampling rates
    fs_low = 30
    fs_high = 200
    t_low = np.linspace(0, 1, int(fs_low), endpoint=False)
    t_high = np.linspace(0, 1, int(fs_high), endpoint=False)
    signal_low = np.sin(2 * np.pi * f_signal * t_low)
    signal_high = np.sin(2 * np.pi * f_signal * t_high)

    plt.figure(figsize=(12, 8))
    
    # Original continuous signal
    plt.subplot(3, 1, 1)
    plt.plot(t, signal, label='Original Signal (50 Hz)', color='blue')
    plt.title("Original Signal (Continuous)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    
    # Aliasing with low-rate sampling
    plt.subplot(3, 1, 2)
    plt.plot(t, signal, alpha=0.5, color='blue', label='Original Signal')
    plt.stem(t_low, signal_low, linefmt='r-', markerfmt='ro', basefmt='r-', label='Low Sampling (30 Hz)')
    plt.title("Aliasing Due to Low Sampling Rate (30 Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    
    # Proper high-rate sampling
    plt.subplot(3, 1, 3)
    plt.plot(t, signal, alpha=0.5, color='blue', label='Original Signal')
    plt.stem(t_high, signal_high, linefmt='g-', markerfmt='go', basefmt='g-', label='High Sampling (200 Hz)')
    plt.title("Proper Sampling Rate (200 Hz)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
