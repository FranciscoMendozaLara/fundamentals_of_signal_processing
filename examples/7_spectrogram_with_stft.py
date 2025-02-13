#!/usr/bin/env python
"""
Example 7: Spectrogram with STFT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from signal_processing.eeg import simulate_eeg

def main():
    fs = 250
    duration = 10
    t, eeg = simulate_eeg(fs, duration)
    f, t_spec, Sxx = spectrogram(eeg, fs, nperseg=256, noverlap=128, scaling='density')

    plt.figure(figsize=(12, 6))
    plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
    plt.title("Spectrogram of Simulated EEG Signal")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.colorbar(label="Power (dB)")
    plt.ylim(0, 60)
    plt.show()

if __name__ == '__main__':
    main()
