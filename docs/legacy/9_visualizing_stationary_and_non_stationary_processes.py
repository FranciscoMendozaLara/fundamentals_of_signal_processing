import numpy as np
import matplotlib.pyplot as plt

# Generate a stationary process (constant mean, variance)
fs = 1000
t = np.linspace(0, 10, fs * 10)
stationary_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))

# Generate a non-stationary process (varying amplitude and frequency)
nonstationary_signal = (1 + 0.5 * t) * np.sin(2 * np.pi * (1 + 0.2 * t) * t) + 0.5 * np.random.randn(len(t))

# Plot both signals
plt.figure(figsize=(12, 6))

# Stationary signal
plt.subplot(2, 1, 1)
plt.plot(t, stationary_signal)
plt.title("Stationary Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Non-stationary signal
plt.subplot(2, 1, 2)
plt.plot(t, nonstationary_signal)
plt.title("Non-Stationary Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
