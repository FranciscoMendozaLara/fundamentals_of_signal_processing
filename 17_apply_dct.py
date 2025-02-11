import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Generate a signal
fs = 16000
t = np.linspace(0, 1, fs, endpoint=False)
audio_signal = np.sin(2 * np.pi * 440 * t)  # 440 Hz tone

# Compute the Mel spectrogram
mel_spectrogram = librosa.feature.melspectrogram(y=audio_signal, sr=fs, n_mels=40, fmax=8000)

# Log Mel spectrogram
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

# Compute MFCCs
mfccs = librosa.feature.mfcc(S=log_mel_spectrogram, sr=fs, n_mfcc=13)

# Plot MFCCs
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
plt.colorbar(label="MFCC Coefficients")
plt.title("MFCCs")
plt.show()
