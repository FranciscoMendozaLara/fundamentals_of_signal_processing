import numpy as np
import matplotlib.pyplot as plt

# Generate a high-frequency sine wave
fs_true = 1000  # True signal sampling frequency (Hz)
f_signal = 50   # Signal frequency (Hz)
t = np.linspace(0, 1, fs_true, endpoint=False)  # 1 second of data
signal = np.sin(2 * np.pi * f_signal * t)  # Sine wave

# Simulate sampling at different rates
fs_low = 30  # Low sampling frequency (Hz)
fs_high = 200  # High sampling frequency (Hz)

t_low = np.linspace(0, 1, int(fs_low), endpoint=False)  # Low-rate time points
t_high = np.linspace(0, 1, int(fs_high), endpoint=False)  # High-rate time points

signal_low = np.sin(2 * np.pi * f_signal * t_low)  # Low-rate sampled signal
signal_high = np.sin(2 * np.pi * f_signal * t_high)  # High-rate sampled signal

# Plot the original and sampled signals
plt.figure(figsize=(12, 8))

# Original signal
# A 50 Hz sine wave is the true signal.
plt.subplot(3, 1, 1)
plt.plot(t, signal, label='Original Signal (50 Hz)', color='blue')
plt.title("Original Signal (Continuous)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

# Low-rate sampling at 30 Hz (aliasing)
# The signal is sampled below the Nyquist rate (2×50=100 Hz).
# The reconstructed signal appears distorted due to aliasing.
plt.subplot(3, 1, 2)
plt.plot(t, signal, label='Original Signal', alpha=0.5, color='blue')
plt.stem(t_low, signal_low, linefmt='r-', markerfmt='ro', basefmt='r-', label='Low Sampling (30 Hz)')
plt.title("Aliasing Due to Low Sampling Rate (30 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# High-rate sampling at 200 Hz(no aliasing)
# The signal is sampled well above the Nyquist rate.
# The reconstructed signal matches the original.
plt.subplot(3, 1, 3)
plt.plot(t, signal, label='Original Signal', alpha=0.5, color='blue')
plt.stem(t_high, signal_high, linefmt='g-', markerfmt='go', basefmt='g-', label='High Sampling (200 Hz)')
plt.title("Proper Sampling Rate (200 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
