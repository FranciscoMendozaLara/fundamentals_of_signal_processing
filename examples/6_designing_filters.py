#!/usr/bin/env python
"""
Example 6: Designing Filters (IIR and FIR)
"""

import numpy as np
import matplotlib.pyplot as plt
from signal_processing.eeg import simulate_eeg
from signal_processing.filters import iir_filter, fir_filter

def main():
    fs = 250
    duration = 10
    t, eeg = simulate_eeg(fs, duration)
    lowcut, highcut = 8, 13  # Alpha band
    eeg_iir = iir_filter(eeg, lowcut, highcut, fs)
    eeg_fir = fir_filter(eeg, lowcut, highcut, fs)

    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, eeg, label="Original EEG")
    plt.title("Original EEG Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(t, eeg_iir, label="IIR Filtered (Alpha Band)", color='g')
    plt.title("IIR Filtered EEG Signal (Alpha Band)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, eeg_fir, label="FIR Filtered (Alpha Band)", color='r')
    plt.title("FIR Filtered EEG Signal (Alpha Band)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
