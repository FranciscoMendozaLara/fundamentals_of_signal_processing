import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Simulate a non-stationary EEG signal
fs = 250  # Sampling frequency
duration = 10  # Signal duration in seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)
eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))

# High-pass filter design
def highpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return lfilter(b, a, data)

# Apply high-pass filter
cutoff = 1  # Remove components below 1 Hz
eeg_filtered = highpass_filter(eeg_signal, cutoff, fs)

# Plot original and filtered signals
plt.figure(figsize=(12, 6))

# Original signal
plt.subplot(2, 1, 1)
plt.plot(t, eeg_signal)
plt.title("Original EEG Signal (Non-Stationary)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# High-pass filtered signal
plt.subplot(2, 1, 2)
plt.plot(t, eeg_filtered)
plt.title("High-Pass Filtered EEG Signal (Drift Removed)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
