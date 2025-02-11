# EEG configuration
FS = 250  # Sampling frequency in Hz
DURATION = 10  # Signal duration in seconds
BANDS = {
    "Delta": (0.5, 4),
    "Theta": (4, 8),
    "Alpha": (8, 13),
    "Beta": (13, 30),
    "Gamma": (30, 100),
}
