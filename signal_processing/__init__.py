# signal_processing/__init__.py
from .config import *
from .eeg import simulate_eeg, band_power, highpass_filter
from .filters import bandpass_filter, iir_filter, fir_filter
from .feature_extraction import envelope_correlation, spectral_entropy
from .phd_filter import simulate_measurements, phd_filter
from .utils import compute_wavelet_transform
