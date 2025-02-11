import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# How It Works

# 1. Bandpass Filter Design:
# - The butter function creates a filter with specified cutoff frequencies (lowcut and highcut).
# - The filter is applied to the EEG signal using lfilter.

# 2. Filtering EEG Bands:
# - Delta (0.5–4 Hz): Deep sleep.
# - Theta (4–8 Hz): Drowsiness or meditation.
# - Alpha (8–13 Hz): Relaxation.
# - Beta (13–30 Hz): Active thinking.
# - Gamma (30–100 Hz): Higher cognitive functions.

# 3. Visualization:
# - Each subplot shows the filtered signal corresponding to one frequency band.
# - This makes it easy to observe how much energy is present in each band.

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

# Function to create a bandpass filter
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')  # Bandpass filter coefficients
    filtered_signal = lfilter(b, a, data)
    return filtered_signal

# Simulate EEG signal
fs = 250  # Sampling frequency in Hz
duration = 10  # Signal duration in seconds
t, eeg = simulate_eeg(fs, duration)  # Using the simulate_eeg function from earlier

# Filter specific bands
delta_band = bandpass_filter(eeg, 0.5, 4, fs)  # Delta: 0.5-4 Hz
theta_band = bandpass_filter(eeg, 4, 8, fs)    # Theta: 4-8 Hz
alpha_band = bandpass_filter(eeg, 8, 13, fs)   # Alpha: 8-13 Hz
beta_band = bandpass_filter(eeg, 13, 30, fs)   # Beta: 13-30 Hz
gamma_band = bandpass_filter(eeg, 30, 100, fs) # Gamma: 30-100 Hz

# Plot the filtered signals
plt.figure(figsize=(12, 10))

# Original EEG Signal
plt.subplot(6, 1, 1)
plt.plot(t, eeg, label='Original EEG Signal')
plt.title('Original EEG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Filtered bands
plt.subplot(6, 1, 2)
plt.plot(t, delta_band, label='Delta Band (0.5-4 Hz)', color='r')
plt.title('Delta Band (0.5-4 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 3)
plt.plot(t, theta_band, label='Theta Band (4-8 Hz)', color='g')
plt.title('Theta Band (4-8 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 4)
plt.plot(t, alpha_band, label='Alpha Band (8-13 Hz)', color='b')
plt.title('Alpha Band (8-13 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 5)
plt.plot(t, beta_band, label='Beta Band (13-30 Hz)', color='m')
plt.title('Beta Band (13-30 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(6, 1, 6)
plt.plot(t, gamma_band, label='Gamma Band (30-100 Hz)', color='c')
plt.title('Gamma Band (30-100 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()