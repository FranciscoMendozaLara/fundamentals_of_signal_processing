# signal_processing/config.py

# Sampling and duration settings
FS = 250           # Sampling frequency in Hz
DURATION = 10      # Duration of signals (seconds)

# EEG frequency bands (Hz)
BANDS = {
    "Delta": (0.5, 4),
    "Theta": (4, 8),
    "Alpha": (8, 13),
    "Beta": (13, 30),
    "Gamma": (30, 100),
}
