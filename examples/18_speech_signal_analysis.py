#!/usr/bin/env python
"""
Example 18: Speech Signal Analysis
"""

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def main():
    # Load an example audio file (replace with actual speech in production)
    speech_signal, fs = librosa.load(librosa.ex('trumpet'), sr=None)
    mel_spectrogram = librosa.feature.melspectrogram(y=speech_signal, sr=fs, n_mels=40, fmax=fs/2)
    log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)
    mfccs = librosa.feature.mfcc(S=log_mel_spectrogram, sr=fs, n_mfcc=13)

    plt.figure(figsize=(12, 12))
    
    # Waveform
    plt.subplot(3, 1, 1)
    librosa.display.waveshow(speech_signal, sr=fs)
    plt.title("Speech Signal Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    
    # Log Mel Spectrogram
    plt.subplot(3, 1, 2)
    librosa.display.specshow(log_mel_spectrogram, sr=fs, x_axis='time', y_axis='mel', cmap='viridis')
    plt.colorbar(label="Log Power (dB)")
    plt.title("Log Mel Spectrogram")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Mel)")
    
    # MFCCs
    plt.subplot(3, 1, 3)
    librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
    plt.colorbar(label="MFCC Coefficients")
    plt.title("MFCCs")
    plt.xlabel("Time (s)")
    plt.ylabel("MFCC Index")
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
