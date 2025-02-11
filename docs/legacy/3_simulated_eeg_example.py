import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from eeg_processing import simulate_eeg

# EEG and Fourier Transform
# In EEG signal processing:

# Frequency Bands:
# - Delta (0.5–4 Hz): Deep sleep.
# - Theta (4–8 Hz): Drowsiness or meditation.
# - Alpha (8–13 Hz): Relaxation.
# - Beta (13–30 Hz): Active thinking.
# - Gamma (30–100 Hz): Higher cognitive functions.

# How It Helps:
# Fourier Transform helps isolate these bands, making it easier to identify 
# patterns like attention or relaxation states.

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

# Apply Fourier Transform to the EEG signal
def analyze_eeg(eeg, fs):
    freqs = np.fft.fftfreq(len(eeg), 1/fs)
    spectrum = np.fft.fft(eeg)
    return freqs, np.abs(spectrum)

# Parameters
fs = 250  # Sampling frequency in Hz
duration = 10  # Signal duration in seconds

# Simulate EEG signal
t, eeg = simulate_eeg(fs, duration)

# Analyze the signal using FFT
freqs, spectrum = analyze_eeg(eeg, fs)

# Plot the results
plt.figure(figsize=(12, 6))

# Time domain
plt.subplot(2, 1, 1)
plt.plot(t, eeg)
plt.title("Simulated EEG Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Frequency domain
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs)//2], spectrum[:len(freqs)//2])  # Positive frequencies
plt.title("Frequency Spectrum (Fourier Transform)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
