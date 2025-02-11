import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load a speech audio file
speech_signal, fs = librosa.load(librosa.example('trumpet'), sr=None)  # Example audio, replace with speech

# Compute Mel spectrogram
mel_spectrogram = librosa.feature.melspectrogram(y=speech_signal, sr=fs, n_mels=40, fmax=fs/2)
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

# Compute MFCCs
mfccs = librosa.feature.mfcc(S=log_mel_spectrogram, sr=fs, n_mfcc=13)

# Plot all in one figure
plt.figure(figsize=(12, 12))

# Plot waveform
plt.subplot(3, 1, 1)
librosa.display.waveshow(speech_signal, sr=fs)
plt.title("Speech Signal Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot log Mel spectrogram
plt.subplot(3, 1, 2)
librosa.display.specshow(log_mel_spectrogram, sr=fs, x_axis='time', y_axis='mel', cmap='viridis')
plt.colorbar(label="Log Power (dB)")
plt.title("Log Mel Spectrogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Mel)")

# Plot MFCCs
plt.subplot(3, 1, 3)
librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
plt.colorbar(label="MFCC Coefficients")
plt.title("MFCCs")
plt.xlabel("Time (s)")
plt.ylabel("MFCC Index")

plt.tight_layout()
plt.show()
