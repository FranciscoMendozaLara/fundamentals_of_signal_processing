#!/usr/bin/env python
"""
Example 4: Filtering Simulated EEG Bands
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_processing.eeg import simulate_eeg
from signal_processing.filters import bandpass_filter

def main():
    fs = 250
    duration = 10
    t, eeg = simulate_eeg(fs, duration)

    # Filter the EEG into different bands
    delta_band = bandpass_filter(eeg, 0.5, 4, fs)
    theta_band = bandpass_filter(eeg, 4, 8, fs)
    alpha_band = bandpass_filter(eeg, 8, 13, fs)
    beta_band  = bandpass_filter(eeg, 13, 30, fs)
    gamma_band = bandpass_filter(eeg, 30, 100, fs)

    plt.figure(figsize=(12, 10))
    plt.subplot(6, 1, 1)
    plt.plot(t, eeg, label='Original EEG Signal')
    plt.title('Original EEG Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6, 1, 2)
    plt.plot(t, delta_band, color='r', label='Delta (0.5-4 Hz)')
    plt.title('Delta Band (0.5-4 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6, 1, 3)
    plt.plot(t, theta_band, color='g', label='Theta (4-8 Hz)')
    plt.title('Theta Band (4-8 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6, 1, 4)
    plt.plot(t, alpha_band, color='b', label='Alpha (8-13 Hz)')
    plt.title('Alpha Band (8-13 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6, 1, 5)
    plt.plot(t, beta_band, color='m', label='Beta (13-30 Hz)')
    plt.title('Beta Band (13-30 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6, 1, 6)
    plt.plot(t, gamma_band, color='c', label='Gamma (30-100 Hz)')
    plt.title('Gamma Band (30-100 Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
