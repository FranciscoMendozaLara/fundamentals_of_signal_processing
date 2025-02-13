#!/usr/bin/env python
"""
Example 8: Wavelet Transform Example
"""

import numpy as np
import matplotlib.pyplot as plt
import pywt
from signal_processing.eeg import simulate_eeg

def main():
    fs = 250
    duration = 10
    t, eeg = simulate_eeg(fs, duration)
    scales = np.arange(1, 128)
    coefficients, frequencies = pywt.cwt(eeg, scales, 'cmor', sampling_period=1/fs)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(np.abs(coefficients), extent=[0, duration, frequencies[-1], frequencies[0]], 
               aspect='auto', cmap='jet')
    plt.colorbar(label='Magnitude')
    plt.title("Wavelet Transform Scalogram")
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.ylim(0, 60)
    plt.show()

if __name__ == '__main__':
    main()
