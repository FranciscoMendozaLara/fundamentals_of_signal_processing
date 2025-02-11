import numpy as np
import matplotlib.pyplot as plt

# Fourier Transform Example
# Let’s consider a simple signal:

# x(t)=sin⁡(2πf1t)+sin⁡(2πf2t) 
# Time Domain: You see a waveform oscillating over time.
# Frequency Domain: The Fourier Transform will show two spikes at f1 and f2, 
# indicating the signal contains two frequencies.

# Time domain signal
fs = 1000  # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second of data
f1, f2 = 5, 100  # Frequencies in Hz
x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)  # Composite signal

# Compute Fourier Transform
X = np.fft.fft(x)  # Fast Fourier Transform
freqs = np.fft.fftfreq(len(X), 1/fs)  # Frequency axis

# Plot time domain and frequency domain
plt.figure(figsize=(12, 6))

# Time domain
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title("Time Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Frequency domain
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs)//2], np.abs(X[:len(X)//2]))  # Positive frequencies
plt.title("Frequency Domain (Fourier Transform)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
