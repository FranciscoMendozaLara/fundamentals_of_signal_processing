import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Create a function to simulate an EEG signal
def simulate_eeg(fs, duration):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    # Simulate EEG bands with different frequencies and amplitudes
    delta = 1.5 * np.sin(2 * np.pi * 2 * t)  # Delta: 2 Hz
    theta = 1.0 * np.sin(2 * np.pi * 6 * t)  # Theta: 6 Hz
    alpha = 0.8 * np.sin(2 * np.pi * 10 * t)  # Alpha: 10 Hz
    beta = 0.5 * np.sin(2 * np.pi * 20 * t)  # Beta: 20 Hz
    gamma = 0.3 * np.sin(2 * np.pi * 40 * t)  # Gamma: 40 Hz
    noise = 0.2 * np.random.randn(len(t))    # Add random noise
    eeg = delta + theta + alpha + beta + gamma + noise
    return t, eeg

# Simulate EEG signal (reuse from earlier)
fs = 250  # Sampling frequency
duration = 10  # Signal duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Compute spectrogram using STFT
f, t_spec, Sxx = spectrogram(eeg, fs, nperseg=256, noverlap=128, scaling='density')

# Plot the spectrogram
plt.figure(figsize=(12, 6))
plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title("Spectrogram of Simulated EEG Signal")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.colorbar(label="Power (dB)")
plt.ylim(0, 60)  # Focus on 0–60 Hz range (EEG bands)
plt.show()
