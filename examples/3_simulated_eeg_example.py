#!/usr/bin/env python
"""
Example 3: Simulated EEG and its Fourier Transform
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_processing.eeg import simulate_eeg

def analyze_eeg(eeg, fs):
    freqs = np.fft.fftfreq(len(eeg), 1/fs)
    spectrum = np.fft.fft(eeg)
    return freqs, np.abs(spectrum)

def main():
    fs = 250
    duration = 10
    t, eeg = simulate_eeg(fs, duration)
    freqs, spectrum = analyze_eeg(eeg, fs)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, eeg)
    plt.title("Simulated EEG Signal (Time Domain)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2])
    plt.title("Frequency Spectrum (Fourier Transform)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
