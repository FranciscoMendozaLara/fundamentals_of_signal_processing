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

