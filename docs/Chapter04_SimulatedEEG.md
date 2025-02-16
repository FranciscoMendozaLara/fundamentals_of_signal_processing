# Chapter 4: Simulated and Analyzing EEG Signals

In this chapter, we explore one of the most fascinating applications of signal processing: Electroencephalography (EEG). EEG signals, which record electrical activity in the brain, offer insights into various cognitive and physiological states. Here, we'll simulate EEG signals, analyze them in both the time and frequency domains, and introduce key techniques used in biomedical signal processing.

---

## 4.1 Overview

In this chapter, you will:
- Learn the basics of EEG signals and the significance of their different frequency bands.
- Understand how to simulate an EEG signal using Python.
- Analyze EEG signals in the time and frequency domains.
- Explore practical applications of EEG signal processing through interactive examples.

---

## 4.2 Introduction to EEG Signals

EEG (Electroencephalography) is a non-invasive method to record electrical activity in the brain. EEG signals are characterized by various frequency bands, each associated with different brain states:

- **Delta (0.5–4 Hz):** Dominant during deep sleep.
- **Theta (4–8 Hz):** Linked with drowsiness or meditation.
- **Alpha (8–13 Hz):** Associated with relaxation and calmness.
- **Beta (13–30 Hz):** Reflects active thinking or alertness.
- **Gamma (30–100 Hz):** Involved in higher cognitive functions.

These bands overlap to form the complex signals observed in EEG recordings.

---

## 4.3 Simulating EEG Signals

We can simulate an EEG signal by combining sine waves corresponding to these frequency bands and adding random noise to mimic real-world variability. In our project, the function `simulate_eeg(fs, duration)`—found in our `signal_processing/eeg.py` module—generates such a signal.

**Example Code:**

```python
from signal_processing.eeg import simulate_eeg
import matplotlib.pyplot as plt

# Parameters for simulation
fs = 250          # Sampling frequency (Hz)
duration = 10     # Duration in seconds

# Simulate EEG signal
t, eeg = simulate_eeg(fs, duration)

# Plot the simulated EEG signal in the time domain
plt.figure(figsize=(12, 6))
plt.plot(t, eeg)
plt.title("Simulated EEG Signal (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


## 4.4 Time-Domain Analysis

The time-domain view of an EEG signal shows how the amplitude varies over time. By examining these fluctuations, you can gain insights into transient events, artifacts, or rhythmic patterns inherent to brain activity.

**Key Points:**
- **Signal Variability:** Notice the complex pattern formed by the superposition of multiple frequency components.
- **Noise:** Real EEG signals contain noise, which is simulated here with random variations.

---

## 4.5 Frequency-Domain Analysis

Using Fourier analysis, we can decompose the simulated EEG signal into its constituent frequencies. This is crucial for understanding the power distribution across different EEG bands.

**Example Code:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Compute the Fourier Transform of the EEG signal
X = np.fft.fft(eeg)
freqs = np.fft.fftfreq(len(eeg), 1/fs)

# Plot the frequency spectrum (only positive frequencies)
plt.figure(figsize=(12, 6))
plt.plot(freqs[:len(freqs)//2], np.abs(X[:len(X)//2]))
plt.title("Frequency Spectrum of Simulated EEG")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
