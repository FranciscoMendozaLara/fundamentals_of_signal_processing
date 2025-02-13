#!/usr/bin/env python
"""
Example 12: High-Pass Filter to Remove Drift
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_processing.eeg import highpass_filter

def main():
    fs = 250
    duration = 10
    t = np.linspace(0, duration, fs * duration, endpoint=False)
    eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))
    cutoff = 1  # Remove frequencies below 1 Hz
    eeg_filtered = highpass_filter(eeg_signal, cutoff, fs)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, eeg_signal)
    plt.title("Original EEG Signal (Non-Stationary)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(t, eeg_filtered)
    plt.title("High-Pass Filtered EEG Signal (Drift Removed)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
