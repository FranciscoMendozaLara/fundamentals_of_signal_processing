#!/usr/bin/env python
"""
Example 17: Apply DCT to MFCCs
"""

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def main():
    fs = 16000
    t = np.linspace(0, 1, fs, endpoint=False)
    audio_signal = np.sin(2 * np.pi * 440 * t)
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_signal, sr=fs, n_mels=40, fmax=8000)
    log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)
    mfccs = librosa.feature.mfcc(S=log_mel_spectrogram, sr=fs, n_mfcc=13)

    plt.figure(figsize=(10, 6))
    librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
    plt.colorbar(label="MFCC Coefficients")
    plt.title("MFCCs")
    plt.show()

if __name__ == '__main__':
    main()
