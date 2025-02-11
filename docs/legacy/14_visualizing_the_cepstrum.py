import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# Generate a signal: source (sinusoid) + filter (exponential decay)
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
source = np.sin(2 * np.pi * 50 * t)  # Pitch at 50 Hz
filter_response = np.exp(-t)  # Simple filter
signal = source * filter_response

# Compute the Fourier Transform
spectrum = np.abs(fft(signal))

# Log-magnitude spectrum
log_spectrum = np.log(spectrum + 1e-10)  # Add small value to avoid log(0)

# Compute the Cepstrum
cepstrum = np.abs(ifft(log_spectrum))

# Plot signal, log spectrum, and cepstrum
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title("Time-Domain Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(log_spectrum[:fs//2])
plt.title("Log-Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Log Magnitude")

plt.subplot(3, 1, 3)
plt.plot(cepstrum[:fs//2])
plt.title("Cepstrum")
plt.xlabel("Quefrency (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
