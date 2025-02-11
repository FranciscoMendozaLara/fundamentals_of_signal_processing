import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend

# Simulate a non-stationary EEG signal
fs = 250  # Sampling frequency
duration = 10  # Signal duration in seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)
eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))

# Simulate a signal with a slow trend
trend = 0.5 * t
eeg_with_trend = eeg_signal + trend

# Detrend the signal
eeg_detrended = detrend(eeg_with_trend)

# Plot the original and detrended signals
plt.figure(figsize=(12, 6))

# Original signal with trend
plt.subplot(2, 1, 1)
plt.plot(t, eeg_with_trend)
plt.title("Original EEG Signal with Trend")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Detrended signal
plt.subplot(2, 1, 2)
plt.plot(t, eeg_detrended)
plt.title("Detrended EEG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
