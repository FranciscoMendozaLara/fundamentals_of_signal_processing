# Chapter 7: Time-Frequency Analysis: Spectrograms and Wavelet Transforms

In this chapter, we explore advanced techniques for analyzing signals that change over time. While the Fourier Transform provides a global frequency representation, many real-world signals are non-stationary—meaning their frequency content changes over time. Two powerful tools to address this are the spectrogram and the wavelet transform.

---

## 7.1 Overview

In this chapter, you will learn:
- How to generate a spectrogram using the Short-Time Fourier Transform (STFT).
- The fundamentals of wavelet transforms for time-frequency analysis.
- How to interpret time-frequency representations.
- Interactive examples in Python to visualize and analyze signals.

---

## 7.2 Spectrograms

A **spectrogram** is a visual representation of the spectrum of frequencies in a signal as they vary with time. It is computed by applying the Short-Time Fourier Transform (STFT) to a signal.

### Code Example: Generating a Spectrogram

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
from signal_processing.eeg import simulate_eeg

# Simulate an EEG signal for demonstration
fs = 250          # Sampling frequency (Hz)
duration = 10     # Duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Compute the spectrogram
f, t_spec, Sxx = spectrogram(eeg, fs, nperseg=256, noverlap=128, scaling='density')

# Plot the spectrogram
plt.figure(figsize=(12, 6))
plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='gouraud')
plt.title("Spectrogram of Simulated EEG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="Power (dB)")
plt.ylim(0, 60)  # Focus on EEG frequency bands
plt.show()
```

In this example, the spectrogram shows how the power at different frequency bands changes over time.

### 7.3 Wavelet Transforms
The Continuous Wavelet Transform (CWT) provides a multi-resolution time-frequency representation of a signal. Unlike the STFT, which uses a fixed window size, the wavelet transform uses scalable windows, offering better time resolution for high frequencies and better frequency resolution for low frequencies.

## Code Example: Performing a Wavelet Transform
```python
import numpy as np
import matplotlib.pyplot as plt
import pywt
from signal_processing.eeg import simulate_eeg

# Simulate an EEG signal
fs = 250          # Sampling frequency (Hz)
duration = 10     # Duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Define scales for the wavelet transform
scales = np.arange(1, 128)

# Perform the Continuous Wavelet Transform (CWT)
coefficients, frequencies = pywt.cwt(eeg, scales, 'cmor', sampling_period=1/fs)

# Plot the wavelet scalogram (magnitude of the coefficients)
plt.figure(figsize=(12, 6))
plt.imshow(np.abs(coefficients), extent=[0, duration, frequencies[-1], frequencies[0]], 
           aspect='auto', cmap='jet')
plt.colorbar(label='Magnitude')
plt.title("Wavelet Transform Scalogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.ylim(0, 60)  # Focus on frequencies of interest
plt.show()
```
This example demonstrates how the wavelet transform provides a time-frequency representation, revealing both transient and long-lasting features in the signal.

### 7.4 Interactive Exploration
We encourage you to:

Experiment with Parameters: Modify the window length and overlap in the spectrogram computation, or adjust the scales in the wavelet transform to see how the time-frequency resolution changes.
Compare Methods: Visualize the same signal using both spectrograms and wavelet scalograms. Observe the differences in resolution and detail.
Apply to Real Data: Use these techniques on other signals (e.g., speech, music, or sensor data) to explore their dynamic frequency content.

### 7.5 Exercises
Spectrogram Exploration:

Simulate a signal that contains two or more frequency components that change over time.
Generate and plot its spectrogram.
Identify periods where each frequency component is dominant.
Wavelet Analysis:

Use the CWT to analyze a non-stationary signal (e.g., one with transient events).
Experiment with different wavelet types (e.g., 'cmor', 'mexh') and scales.
Discuss how the choice of wavelet and scales affects the time-frequency representation.
Comparison Exercise:

For a given signal, compute both the spectrogram and the wavelet transform.
Compare the time-frequency resolutions and discuss the strengths and limitations of each method.

### 7.6 Summary
In this chapter, you learned:

Spectrograms: How the Short-Time Fourier Transform is used to compute and visualize spectrograms.
Wavelet Transforms: How wavelet analysis offers a flexible time-frequency representation.
The advantages and trade-offs of each method for analyzing non-stationary signals.
How to use interactive Python examples to visualize these concepts.
Time-frequency analysis is a critical tool in understanding signals with varying frequency content. In the next chapter, we will dive into Chapter 8: Stationarity, Segmentation, and Detrending, where we will explore methods for handling non-stationary signals and segmenting them for further analysis.