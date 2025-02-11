import pywt
import numpy as np
import matplotlib.pyplot as plt

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

# Perform Continuous Wavelet Transform (CWT)
scales = np.arange(1, 128)
coefficients, frequencies = pywt.cwt(eeg, scales, 'cmor', sampling_period=1/fs)

# Plot wavelet scalogram
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(coefficients), extent=[0, duration, frequencies[-1], frequencies[0]], aspect='auto', cmap='jet')
plt.colorbar(label='Magnitude')
plt.title("Wavelet Transform Scalogram")
plt.ylabel("Frequency (Hz)")
plt.xlabel("Time (s)")
plt.ylim(0, 60)  # Focus on EEG bands
plt.show()
