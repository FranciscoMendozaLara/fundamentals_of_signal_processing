#!/usr/bin/env python
"""
Example 15: Mel Filter Bank and MFCC Extraction
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def main():
    fs = 1000
    t = np.linspace(0, 1, fs, endpoint=False)
    y = np.sin(2 * np.pi * 220 * t)  # A simple tone
    mel_filters = librosa.filters.mel(sr=fs, n_fft=1024, n_mels=10, fmin=0, fmax=fs/2)

    plt.figure(figsize=(10, 6))
    for i, filter_bank in enumerate(mel_filters):
        plt.plot(filter_bank, label=f'Filter {i+1}')
    plt.title("Mel Filter Bank")
    plt.xlabel("Frequency Bin")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()

    mfccs = librosa.feature.mfcc(y=y, sr=fs, n_mfcc=13)
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
    plt.colorbar(label="MFCC Coefficients")
    plt.title("MFCCs")
    plt.xlabel("Time (s)")
    plt.ylabel("MFCC Index")
    plt.show()

if __name__ == '__main__':
    main()
