#!/usr/bin/env python
"""
Example 11: Detrending a Signal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend

def main():
    fs = 250
    duration = 10
    t = np.linspace(0, duration, fs * duration, endpoint=False)
    eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))
    trend = 0.5 * t
    eeg_with_trend = eeg_signal + trend
    eeg_detrended = detrend(eeg_with_trend)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, eeg_with_trend)
    plt.title("Original EEG Signal with Trend")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(t, eeg_detrended)
    plt.title("Detrended EEG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
