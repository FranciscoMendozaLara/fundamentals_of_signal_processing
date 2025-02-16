# Chapter 5: Filtering Techniques for Signal Processing

In this chapter, we explore digital filtering—the process of isolating or removing specific frequency components from a signal. Filtering is a fundamental operation in signal processing, enabling you to enhance useful information, remove noise, or extract particular features from a signal.

---

## 5.1 Overview

In this chapter, you will learn:
- The basics of digital filtering and why it is important.
- Different types of filters, such as lowpass, highpass, bandpass, and bandstop.
- The differences between IIR (Infinite Impulse Response) and FIR (Finite Impulse Response) filters.
- How to design and apply filters using Python with interactive examples.

---

## 5.2 Basics of Digital Filtering

Digital filters are algorithms or systems that modify the characteristics of a signal by attenuating or amplifying certain frequency components. Common applications include:
- **Noise Reduction:** Removing unwanted frequency components.
- **Feature Extraction:** Isolating a frequency band of interest.
- **Signal Enhancement:** Emphasizing certain signal characteristics for further analysis.

A digital filter is typically characterized by its:
- **Cutoff frequencies:** The boundaries that define the passband and stopband.
- **Filter order:** Determines the steepness of the filter's frequency response.
- **Response Type:** Whether the filter is lowpass, highpass, bandpass, or bandstop.

---

## 5.3 Types of Filters

### Lowpass Filter
Allows frequencies below a specified cutoff to pass through while attenuating higher frequencies.

### Highpass Filter
Allows frequencies above a specified cutoff to pass through while attenuating lower frequencies.

### Bandpass Filter
Allows frequencies within a specific range to pass through while attenuating frequencies outside this range.

### Bandstop Filter
Attenuates frequencies within a specific range while allowing frequencies outside that range to pass through.

---

## 5.4 IIR vs. FIR Filters

### IIR Filters
- **Pros:** Generally require fewer coefficients (lower order) to achieve a desired response, making them computationally efficient.
- **Cons:** Can have nonlinear phase responses and may be unstable if not carefully designed.

### FIR Filters
- **Pros:** Always stable and can be designed to have a linear phase response, which preserves the shape of the filtered signal.
- **Cons:** Often require a higher order (more coefficients) compared to IIR filters, which can increase computational load.

---

## 5.5 Python Code Examples for Filtering

### Example: Bandpass Filter Using a Butterworth Filter (IIR)

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from signal_processing.eeg import simulate_eeg

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

# Simulate an EEG signal
fs = 250          # Sampling frequency (Hz)
duration = 10     # Duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Apply a bandpass filter to isolate the Alpha band (8-13 Hz)
alpha_band = bandpass_filter(eeg, 8, 13, fs)

# Plot the original and filtered signals
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, eeg, label="Original EEG")
plt.title("Original EEG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, alpha_band, label="Alpha Band (8-13 Hz)", color='red')
plt.title("Filtered EEG Signal - Alpha Band")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

### Example: FIR Filter Design Using firwin
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter
from signal_processing.eeg import simulate_eeg

def fir_filter(data, lowcut, highcut, fs, numtaps=101):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    taps = firwin(numtaps, [low, high], pass_zero=False)
    return lfilter(taps, 1.0, data)

# Simulate an EEG signal
fs = 250          # Sampling frequency (Hz)
duration = 10     # Duration in seconds
t, eeg = simulate_eeg(fs, duration)

# Apply an FIR filter to isolate the Beta band (13-30 Hz)
beta_band = fir_filter(eeg, 13, 30, fs)

# Plot the original and filtered signals
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, eeg, label="Original EEG")
plt.title("Original EEG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, beta_band, label="Beta Band (13-30 Hz)", color='green')
plt.title("Filtered EEG Signal - Beta Band")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
```

## 5.6 Interactive Exploration

We encourage you to experiment with:
- **Different Filter Parameters:** Modify cutoff frequencies, filter order, or number of taps to see how the filtered signal changes.
- **Comparing IIR and FIR Filters:** Apply both types of filters to the same signal and compare their responses.
- **Analyzing Frequency Responses:** Use functions like `freqz` from `scipy.signal` to plot the frequency response of your filters.


## 5.7 Exercises

1. **Filter Design Comparison:**
   - Simulate an EEG signal and design both an IIR bandpass filter and an FIR bandpass filter to isolate the Alpha band (8–13 Hz).
   - Compare the time-domain responses and frequency responses of both filters.

2. **Lowpass and Highpass Filtering:**
   - Design a lowpass filter to remove high-frequency noise from a signal.
   - Design a highpass filter to eliminate slow-varying trends.
   - Apply both filters to a simulated signal and analyze the results.

3. **Parameter Tuning:**
   - Experiment with different filter orders (for IIR) and number of taps (for FIR) to understand their effects on the filter's performance.
   - Observe and document the impact on both the time-domain signal and the frequency-domain spectrum.

## 5.8 Summary

In this chapter, you learned:
- The fundamental principles of digital filtering.
- The differences between lowpass, highpass, bandpass, and bandstop filters.
- The advantages and disadvantages of IIR versus FIR filters.
- How to design and implement filters in Python using both IIR (Butterworth) and FIR (firwin) methods.
- How to interactively explore and experiment with filter parameters to achieve desired signal processing outcomes.

Filtering is a key technique in signal processing that enhances or extracts information from raw signals. Mastering these techniques will serve as a foundation for advanced topics such as feature extraction and pattern recognition in subsequent chapters.


Next, we will continue to **Chapter 6: Sampling, Aliasing, and Signal Reconstruction**, where we will delve into the concepts of signal sampling and the challenges associated with aliasing.

