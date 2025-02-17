# Chapter 9: Feature Extraction in Signal Processing

In this chapter, we explore methods for extracting meaningful features from signals—an essential step in many applications such as biomedical signal analysis, speech recognition, and machine learning. We will cover techniques including band power calculation, cepstrum analysis, and the extraction of Mel-Frequency Cepstral Coefficients (MFCCs).

---

## 9.1 Overview

In this chapter, you will learn:
- How to compute the power within specific frequency bands (band power) in a signal.
- How to perform cepstrum analysis to reveal periodic structures in the frequency spectrum.
- The fundamentals of Mel filter banks and MFCCs to extract auditory features.
- How to use interactive Python examples to practice these techniques.

---

## 9.2 Band Power Analysis

Band power refers to the energy contained in a specified frequency band of a signal. This is particularly useful in EEG analysis, where different frequency bands (e.g., Delta, Theta, Alpha, Beta, Gamma) are linked to various cognitive states.

### Code Example: Calculating Band Power

```python
import numpy as np
from scipy.signal import welch
from signal_processing.eeg import simulate_eeg

# Simulation parameters
fs = 250
duration = 10
t, eeg = simulate_eeg(fs, duration)

# Define the frequency band (e.g., Alpha band: 8-13 Hz)
band = (8, 13)

# Compute the power spectral density using Welch's method
freqs, psd = welch(eeg, fs, nperseg=fs*2)
band_power = np.sum(psd[(freqs >= band[0]) & (freqs <= band[1])])

print(f"Alpha Band Power (8-13 Hz): {band_power:.2f}")
```

### 9.3 Cepstrum Analysis
Cepstrum analysis is used to detect periodicity in the frequency spectrum of a signal. It is particularly useful in applications such as pitch detection and speech processing.

## Code Example: Visualizing the Cepstrum
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# Generate a signal: a sine wave modulated by an exponential decay
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
source = np.sin(2 * np.pi * 50 * t)
filter_response = np.exp(-t)
signal = source * filter_response

# Compute the Fourier Transform
spectrum = np.abs(fft(signal))

# Compute the log-magnitude spectrum
log_spectrum = np.log(spectrum + 1e-10)

# Compute the Cepstrum
cepstrum = np.abs(ifft(log_spectrum))

# Plot the log-magnitude spectrum and cepstrum
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(log_spectrum[:fs//2])
plt.title("Log-Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Log Amplitude")

plt.subplot(2, 1, 2)
plt.plot(cepstrum[:fs//2])
plt.title("Cepstrum")
plt.xlabel("Quefrency (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
```

### 9.4 Mel Filter Banks and MFCCs
Mel filter banks approximate the human ear's frequency resolution, and MFCCs (Mel-Frequency Cepstral Coefficients) are widely used features in speech and audio processing.

## Code Example: Computing MFCCs
```python
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Generate an auditory signal (e.g., a 220 Hz tone)
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
y = np.sin(2 * np.pi * 220 * t)

# Compute MFCCs using librosa
mfccs = librosa.feature.mfcc(y=y, sr=fs, n_mfcc=13)

# Plot the MFCCs
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
plt.colorbar(label="MFCC Coefficients")
plt.title("MFCCs")
plt.xlabel("Time (s)")
plt.ylabel("MFCC Index")
plt.show()
```

### 9.5 Interactive Exploration
We encourage you to experiment with:

Varying the Frequency Bands: Compute band power for different EEG frequency bands (e.g., Delta, Theta, Alpha, Beta, Gamma) and compare the results.
Cepstrum Analysis: Modify the source signal or filter response to observe changes in the cepstrum.
MFCC Extraction: Use different auditory signals or real-world audio files to compute and analyze MFCCs. Experiment with changing the number of coefficients.

### 9.6 Exercises
1. Band Power Calculation:

- Simulate an EEG signal and compute the power for each EEG band (Delta, Theta, Alpha, Beta, Gamma).
- Plot the band power values and discuss any patterns you observe.

2. Cepstrum Analysis:

- Generate a composite signal that contains multiple sine waves.
- Compute and plot its cepstrum.
- Identify any periodic structures in the cepstrum and relate them to the signal components.

3. MFCC Experiment:

- Load a real audio file using librosa.
- Compute its MFCCs.
- Analyze how the MFCC features change over time and discuss what these changes might indicate about the audio content.

### 9.7 Summary
In this chapter, you learned:

Band Power Analysis: How to compute the energy in specific frequency bands, useful for EEG and other signals.
Cepstrum Analysis: How to detect periodicities in the frequency spectrum.
Mel Filter Banks and MFCCs: How to extract auditory features that mimic human hearing.
Practical examples and exercises were provided to reinforce these techniques.
Feature extraction transforms raw signals into meaningful representations, which is critical for further analysis and pattern recognition. In the next chapter, we will dive into Chapter 10: Speech Signal Analysis, where we apply these feature extraction methods to the analysis of speech signals.