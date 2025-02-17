# Chapter 10: Speech Signal Analysis

In this chapter, we apply signal processing techniques specifically to analyze speech signals. We'll use Python libraries such as librosa to load, process, and visualize speech data. By the end of this chapter, you'll be able to examine the waveform, compute spectrograms, and extract features like MFCCs (Mel-Frequency Cepstral Coefficients) that are essential for applications like speech recognition and speaker identification.

---

## 10.1 Overview

In this chapter, you will learn:
- How to load a speech signal from an audio file using librosa.
- How to visualize the time-domain waveform of a speech signal.
- How to compute and visualize the spectrogram of a speech signal.
- How to extract MFCCs and understand their role in capturing auditory features.
- How to interactively explore and analyze speech signal features.

---

## 10.2 Loading and Visualizing Speech Signals

We'll start by loading a speech signal using the librosa library. For demonstration purposes, we can use an example audio file provided by librosa (in practice, replace this with an actual speech file).

### Code Example: Loading and Visualizing the Waveform

```python
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load an example speech signal (for demonstration; replace with your speech file)
speech_signal, fs = librosa.load(librosa.ex('trumpet'), sr=None)

# Plot the waveform of the speech signal
plt.figure(figsize=(12, 4))
librosa.display.waveshow(speech_signal, sr=fs)
plt.title("Speech Signal Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
```

### 10.3 Spectrogram and Time-Frequency Representation
The spectrogram reveals how the frequency content of a speech signal evolves over time. It is computed using the Short-Time Fourier Transform (STFT).

## Code Example: Computing and Visualizing the Spectrogram
```python 
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Compute the STFT of the speech signal
D = librosa.stft(speech_signal)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db, sr=fs, x_axis='time', y_axis='hz', cmap='magma')
plt.title("Speech Signal Spectrogram")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(format='%+2.0f dB')
plt.show()
```

### 10.4 Extracting MFCCs
Mel-Frequency Cepstral Coefficients (MFCCs) are features that capture perceptually important characteristics of speech. They are widely used in speech recognition and other audio analysis applications.

## Code Example: Computing and Visualizing MFCCs
```python 
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Compute MFCCs from the speech signal
mfccs = librosa.feature.mfcc(y=speech_signal, sr=fs, n_mfcc=13)

# Plot the MFCCs
plt.figure(figsize=(10, 6))
librosa.display.specshow(mfccs, sr=fs, x_axis='time', cmap='viridis')
plt.title("MFCCs of Speech Signal")
plt.xlabel("Time (s)")
plt.ylabel("MFCC Coefficient Index")
plt.colorbar(label="Coefficient Value")
plt.show()
```

### 10.5 Interactive Exploration
We encourage you to experiment with:

- Different Audio Files: Load various speech signals or other types of audio to compare their waveforms, spectrograms, and MFCCs.
- Parameter Tuning: Modify the number of MFCC coefficients, STFT window lengths, or hop lengths to see how these changes affect the representations.
- Feature Analysis: Explore how the extracted MFCCs vary over time, and consider how these features might be used in tasks like speech recognition or speaker identification.

### 10.6 Exercises
1. Waveform and Spectrogram Analysis:

- Load a different speech audio file using librosa.
- Plot its waveform and compute its spectrogram.
- Compare the time-domain and frequency-domain representations and discuss any differences.

2. MFCC Experiment:

- Compute MFCCs using various numbers of coefficients (e.g., 13, 20, 40).
- Visualize how the number of coefficients affects the MFCC representation.
- Discuss what these features might indicate about the characteristics of the speech signal.

3. Feature Extraction for Classification:

- Use a small dataset of speech signals from different speakers.
- Extract MFCCs from each signal and compute summary statistics (e.g., mean, variance).
- Consider how these features could be used for speaker identification or speech recognition.

### 10.7 Summary
In this chapter, you learned:

- How to load and visualize a speech signal using Python libraries.
- How to compute and interpret the spectrogram of a speech signal.
- The process of extracting MFCCs and their significance in speech processing.
- Interactive methods to explore and analyze speech signal features.
- These techniques are fundamental for many applications in speech processing, from recognition to speaker identification. In the next chapter, we will explore Chapter 11: Advanced Topics and Applications, where we cover more sophisticated signal processing methods and real-world applications.
