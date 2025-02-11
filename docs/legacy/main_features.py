import numpy as np
import matplotlib.pyplot as plt
from eeg_processing import simulate_eeg, band_power, highpass_filter
from feature_extraction import envelope_correlation, spectral_entropy
from config import FS, DURATION

# Simulate EEG
fs = FS
duration = DURATION
t, eeg = simulate_eeg(fs, duration)

# Filter EEG
eeg_filtered = highpass_filter(eeg, cutoff=1, fs=fs)

# Compute features
audio_envelope = abs(np.sin(2 * np.pi * 5 * t))  # Example envelope
correlation = envelope_correlation(eeg_filtered, audio_envelope)
entropy = spectral_entropy(eeg_filtered, fs)

print(f"Envelope Correlation: {correlation:.2f}")
print(f"Spectral Entropy: {entropy:.2f}")
