import numpy as np
import matplotlib.pyplot as plt

# Simulate a non-stationary EEG signal
fs = 250  # Sampling frequency
duration = 10  # Signal duration in seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)
eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))

# Segment the signal into 1-second windows
segment_length = fs  # Number of samples per segment (1 second)
segments = np.array_split(eeg_signal, duration)

# Plot original and segmented signals
plt.figure(figsize=(12, 6))

# Original signal
plt.subplot(2, 1, 1)
plt.plot(t, eeg_signal)
plt.title("Original EEG Signal (Non-Stationary)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot segments
plt.subplot(2, 1, 2)
for i, segment in enumerate(segments):
    plt.plot(np.arange(i, i + 1, 1/fs), segment)
plt.title("Segmented EEG Signal (1-Second Windows)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
