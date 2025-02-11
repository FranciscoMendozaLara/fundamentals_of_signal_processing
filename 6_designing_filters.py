import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, firwin, freqz

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

# Function to design and apply a Butterworth IIR filter
def iir_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    filtered_signal = lfilter(b, a, data)
    return filtered_signal

# Function to design and apply an FIR filter
def fir_filter(data, lowcut, highcut, fs, numtaps=101):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    taps = firwin(numtaps, [low, high], pass_zero=False)
    filtered_signal = lfilter(taps, 1.0, data)
    return filtered_signal

# Simulate EEG signal (reuse from earlier)
fs = 250  # Sampling frequency in Hz
duration = 10  # Signal duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Apply filters
lowcut, highcut = 8, 13  # Alpha band
eeg_iir = iir_filter(eeg, lowcut, highcut, fs)
eeg_fir = fir_filter(eeg, lowcut, highcut, fs)

# Plot the results
plt.figure(figsize=(12, 8))

# Original EEG signal
plt.subplot(3, 1, 1)
plt.plot(t, eeg, label="Original EEG")
plt.title("Original EEG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# IIR filtered signal
plt.subplot(3, 1, 2)
plt.plot(t, eeg_iir, label="IIR Filtered (Alpha Band)", color='g')
plt.title("IIR Filtered EEG Signal (Alpha Band)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# FIR filtered signal
plt.subplot(3, 1, 3)
plt.plot(t, eeg_fir, label="FIR Filtered (Alpha Band)", color='r')
plt.title("FIR Filtered EEG Signal (Alpha Band)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
