# Chapter 8: Stationarity, Segmentation, and Detrending

In this chapter, we focus on techniques for handling non-stationary signals. Many real-world signals exhibit changes in their statistical properties over time, meaning they are non-stationary. Understanding stationarity, segmenting signals into portions that are approximately stationary, and detrending signals to remove slow-varying trends are key techniques for effective signal analysis.

---

## 8.1 Overview

In this chapter, you will learn:
- The difference between stationary and non-stationary signals.
- Techniques for segmenting a long signal into shorter segments that are approximately stationary.
- Methods for detrending a signal to remove slow, unwanted trends.
- How to apply these concepts using interactive Python examples.

---

## 8.2 Stationary vs. Non-Stationary Signals

**Stationary signals** have statistical properties (such as mean, variance, and autocorrelation) that remain constant over time. In contrast, **non-stationary signals** exhibit time-varying statistics. Many signal processing techniques assume stationarity; therefore, when dealing with non-stationary signals, it is often useful to:
- **Segment the signal:** Divide it into smaller time windows where stationarity approximately holds.
- **Detrend the signal:** Remove slow trends to better analyze the underlying fluctuations.

---

## 8.3 Signal Segmentation

**Segmentation** involves dividing a long, non-stationary signal into shorter segments that can be treated as stationary for analysis purposes.

### Code Example: Segmenting a Signal

```python
import numpy as np
import matplotlib.pyplot as plt

# Simulate a non-stationary signal: amplitude increases over time
fs = 250  # Sampling frequency (Hz)
duration = 10  # Total duration in seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)
signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))

# Define segment length (e.g., 1 second)
segment_length = fs  # Number of samples in 1 second

# Segment the signal into 1-second windows
segments = np.array_split(signal, duration)

# Plot the original signal and segmented signals
plt.figure(figsize=(12, 8))

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Original Non-Stationary Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Plot segments with each segment in a different color
plt.subplot(2, 1, 2)
for i, seg in enumerate(segments):
    seg_t = np.linspace(i, i+1, len(seg), endpoint=False)
    plt.plot(seg_t, seg, label=f"Segment {i+1}")
plt.title("Segmented Signal (1-Second Windows)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.tight_layout()
plt.show()
```

### 8.4 Detrending a Signal
Detrending is the process of removing slow-varying trends from a signal to focus on its underlying fluctuations. This is particularly useful when a trend masks the important features of the signal.

## Code Example: Detrending a Signal
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import detrend

# Simulate a signal with a trend
fs = 250  # Sampling frequency (Hz)
duration = 10  # Duration in seconds
t = np.linspace(0, duration, fs * duration, endpoint=False)
signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))
trend = 0.5 * t  # A slow linear trend

# Create the signal with trend
signal_with_trend = signal + trend

# Detrend the signal
signal_detrended = detrend(signal_with_trend)

# Plot the original signal with trend and the detrended signal
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, signal_with_trend)
plt.title("Signal with Trend")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(t, signal_detrended)
plt.title("Detrended Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

```

### 8.5 Interactive Exploration
We encourage you to experiment with:

Different Segment Lengths: Try segmenting the signal into windows of varying lengths (e.g., 0.5 s, 1 s, 2 s) and observe how well each segment approximates stationarity.
Various Detrending Methods: Explore alternative detrending techniques (e.g., removing a polynomial trend) to see which best reveals the underlying signal fluctuations.
Combined Analysis: First detrend a non-stationary signal, then segment it, and apply spectral analysis (like FFT) to each segment to compare their frequency content.

### 8.6 Exercises
Segmentation Experiment:

Simulate a non-stationary signal with a known trend.
Segment the signal into different window lengths (e.g., 0.5 s, 1 s, 2 s).
Plot the segments and discuss which segmentation best approximates stationarity.
Detrending Comparison:

Create a signal with a non-linear trend (e.g., quadratic).
Apply different detrending methods (linear detrending, polynomial detrending) and compare the results.
Evaluate which method best reveals the underlying fluctuations.
Combined Analysis:

Take a long, non-stationary signal.
Detrend the signal, then segment it.
Perform spectral analysis (e.g., FFT) on each segment and compare the frequency content across segments.

### 8.7 Summary
In this chapter, you learned:

Stationarity: The importance of recognizing whether a signal's statistical properties remain constant over time.
Segmentation: How dividing a non-stationary signal into shorter, more stationary segments can facilitate analysis.
Detrending: Techniques for removing trends from a signal to better reveal its underlying behavior.
By effectively segmenting and detrending signals, you can apply standard signal processing techniques more accurately. In the next chapter, we will explore Chapter 9: Feature Extraction in Signal Processing, where we will discuss methods to quantify and extract meaningful features from signals.