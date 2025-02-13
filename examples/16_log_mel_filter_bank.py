#!/usr/bin/env python
"""
Example 16: Log Mel Filter Bank
"""

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def main():
    fs = 16000
    t = np.linspace(0, 1, fs, endpoint=False)
    audio_signal = np.sin(2 * np.pi * 440 * t)  # 440 Hz tone
    mel_spectrogram = librosa.feature.melspectrogram(y=audio_signal, sr=fs, n_mels=40, fmax=8000)
    log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

    plt.figure(figsize=(10, 6))
    librosa.display.specshow(log_mel_spectrogram, sr=fs, x_axis='time', y_axis='mel', cmap='viridis')
    plt.colorbar(label="Log Power")
    plt.title("Log Mel Spectrogram")
    plt.show()

if __name__ == '__main__':
    main()
