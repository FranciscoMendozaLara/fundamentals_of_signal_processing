# Chapter 6: Sampling, Aliasing, and Signal Reconstruction

In this chapter, we explore the essential concepts of sampling, aliasing, and signal reconstruction. These topics are crucial for understanding how continuous-time signals are converted to discrete-time signals, how to avoid misinterpretation of signal frequencies, and how to accurately reconstruct the original signal from its samples.

---

## 6.1 Overview

In this chapter, you will learn:
- The process of sampling and its importance in digital signal processing.
- The Nyquist-Shannon Sampling Theorem and its implications.
- How aliasing occurs when a signal is undersampled.
- Techniques for reconstructing a continuous signal from its discrete samples.
- Interactive examples to illustrate these concepts in Python.

---

## 6.2 Sampling

**Sampling** is the process of converting a continuous-time signal \( x(t) \) into a discrete-time signal \( x[n] \) by taking measurements at regular intervals (sampling period \( T \)).

- **Continuous-Time Signal:** \( x(t) \)
- **Discrete-Time Signal:** \( x[n] = x(nT) \), where \( n \) is an integer.
- **Sampling Frequency:** \( f_s = \frac{1}{T} \)

Sampling allows us to work with digital data, but it must be done correctly to capture all the relevant information from the original signal.

---

## 6.3 The Nyquist-Shannon Sampling Theorem

The **Nyquist-Shannon Sampling Theorem** states that a continuous-time signal can be perfectly reconstructed from its samples if the sampling frequency \( f_s \) is greater than twice the maximum frequency component in the signal (the Nyquist rate):

\[
f_s > 2f_{\text{max}}
\]

This condition ensures that no frequency components are lost during sampling.

---

## 6.4 Aliasing

**Aliasing** is a phenomenon that occurs when a signal is sampled at a rate lower than the Nyquist rate. When aliasing occurs, higher frequency components of the signal "fold" into lower frequencies, causing distortion and misinterpretation.

### Code Example: Aliasing Demonstration

```python
import numpy as np
import matplotlib.pyplot as plt

# True sampling frequency and signal parameters
fs_true = 1000  # True sampling frequency (Hz)
f_signal = 50   # Signal frequency (Hz)
t = np.linspace(0, 1, fs_true, endpoint=False)
signal = np.sin(2 * np.pi * f_signal * t)

# Simulate undersampling
fs_low = 30  # Undersampled frequency (Hz)
t_low = np.linspace(0, 1, int(fs_low), endpoint=False)
signal_low = np.sin(2 * np.pi * f_signal * t_low)

# Plot original signal vs undersampled signal
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Original Signal (50 Hz)", color='blue')
plt.title("Original Continuous Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(t_low, signal_low, linefmt='r-', markerfmt='ro', basefmt='r-', use_line_collection=True)
plt.title("Undersampled Signal (30 Hz Sampling)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
```

### 6.5 Signal Reconstruction
Signal Reconstruction involves approximating the original continuous-time signal from its discrete samples. When the sampling theorem is satisfied, reconstruction is typically achieved through interpolation methods, such as sinc interpolation.

## Code Example: Simple Reconstruction Using Interpolation
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Assume we have a properly sampled signal
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)
signal = np.sin(2 * np.pi * 50 * t)

# Create discrete samples (simulate digital acquisition)
n = np.arange(0, fs, 10)  # Downsample by a factor of 10 for demonstration
t_samples = t[n]
signal_samples = signal[n]

# Use cubic interpolation for reconstruction
f_interp = interp1d(t_samples, signal_samples, kind='cubic')
t_reconstructed = np.linspace(0, 1, fs)
signal_reconstructed = f_interp(t_reconstructed)

# Plot the original, sampled, and reconstructed signals
plt.figure(figsize=(12, 8))
plt.plot(t, signal, label="Original Signal", color='blue', alpha=0.5)
plt.stem(t_samples, signal_samples, linefmt='r-', markerfmt='ro', basefmt='r-', label="Samples", use_line_collection=True)
plt.plot(t_reconstructed, signal_reconstructed, label="Reconstructed Signal", color='green', linestyle='--')
plt.title("Signal Reconstruction from Samples")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
```

### 6.6 Interactive Exploration
We encourage you to experiment with:

Varying the Sampling Frequency: Modify 
$𝑓_𝑠$ and observe how the signal reconstruction quality changes.
Aliasing Effects: Intentionally undersample a signal to see aliasing in action, and then increase the sampling rate to eliminate it.
Reconstruction Methods: Compare different interpolation methods (e.g., linear, cubic, sinc) for reconstructing the signal.

### 6.7 Exercises
Sampling Rate Experiment:

Simulate a continuous sine wave with a known frequency.
Sample the signal at various sampling rates (both above and below the Nyquist rate).
Plot and compare the discrete signals and their reconstructed versions.
Aliasing Observation:

Create a composite signal containing two different frequencies.
Sample the signal at a rate below the Nyquist rate for one of the frequency components.
Analyze the resulting frequency spectrum and identify the aliasing effect.
Reconstruction Challenge:

Given a set of discrete samples from a continuous signal, use different interpolation methods to reconstruct the signal.
Compare the accuracy of the reconstruction visually and compute the error between the original and reconstructed signals.

### 6.8 Summary
In this chapter, you learned:

Sampling: The process of converting a continuous signal into a discrete signal.
Nyquist-Shannon Sampling Theorem: The critical criterion that determines the minimum sampling frequency needed to accurately represent a signal.
Aliasing: How insufficient sampling can lead to distortion in the frequency domain.
Signal Reconstruction: Methods to recover the original signal from its samples, emphasizing the importance of proper sampling.
These concepts are fundamental for all digital signal processing tasks, ensuring that you can correctly acquire and interpret signals. In the next chapter, we will explore Chapter 7: Time-Frequency Analysis: Spectrograms and Wavelet Transforms, where we delve into advanced techniques for analyzing signals that vary over time.