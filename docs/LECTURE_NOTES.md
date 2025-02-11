# Fundamentals of Signal Processing with Python

Welcome to the **Fundamentals of Signal Processing with Python** course! This repository contains a series of lectures and hands-on examples designed to guide you through the essential concepts and techniques in signal processing. Throughout the course, you will learn how to simulate, analyze, and process signals using Python and popular scientific libraries.

## Table of Contents

1. [Introduction to Signals and Systems](#introduction-to-signals-and-systems)
2. [Fourier Transform and Frequency Domain Analysis](#fourier-transform-and-frequency-domain-analysis)
3. [Simulated EEG Signal and Analysis](#simulated-eeg-signal-and-analysis)
4. [Filtering Techniques for EEG Signals](#filtering-techniques-for-eeg-signals)
5. [Aliasing and Sampling](#aliasing-and-sampling)
6. [Designing Filters: IIR and FIR](#designing-filters-iir-and-fir)
7. [Time-Frequency Analysis: Spectrogram and Wavelet Transform](#time-frequency-analysis-spectrogram-and-wavelet-transform)
8. [Stationarity, Segmentation, and Detrending](#stationarity-segmentation-and-detrending)
9. [Feature Extraction: Band Power, Cepstrum, and MFCCs](#feature-extraction-band-power-cepstrum-and-mfccs)
10. [Speech Signal Analysis](#speech-signal-analysis)
11. [Advanced Topics: Feature Extraction and PH Filters](#advanced-topics-feature-extraction-and-ph-filters)
12. [Conclusion and Further Resources](#conclusion-and-further-resources)

---

## 1. Introduction to Signals and Systems

### What is a Signal?
A **signal** is a function that conveys information about a phenomenon. Signals can be:
- **Continuous or Discrete:** Depending on whether the data is defined for every time instant or only at specific intervals.
- **Represented in Different Domains:** Most commonly in the time domain or frequency domain.

### Convolution
**Convolution** is a key operation in linear time-invariant (LTI) systems. It describes how an input signal is modified by a system characterized by its impulse response.

- **Example Concept:**
  - **Input Signal (\(x(t)\)):** For example, a unit step function.
  - **Impulse Response (\(h(t)\)):** For example, an exponential decay.
  - **Output Signal (\(y(t)\)):** Obtained by convolving \(x(t)\) and \(h(t)\).

> **Code Reference:** [1_visualizing_convolution.py](./examples/1_visualizing_convolution.py)

**Example Code:**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

t = np.linspace(0, 10, 1000)
x = np.heaviside(t, 1)               # Unit step function
h = np.exp(-t) * np.heaviside(t, 1)    # Exponential decay
dt = t[1] - t[0]
y = convolve(x, h, mode='full')[:len(t)] * dt

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Input: x(t)')
plt.plot(t, h, label='Impulse Response: h(t)')
plt.plot(t, y, label='Output: y(t)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Convolution of x(t) and h(t)')
plt.legend()
plt.grid(True)
plt.show()
