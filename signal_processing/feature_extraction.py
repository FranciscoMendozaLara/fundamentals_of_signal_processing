# signal_processing/feature_extraction.py

import numpy as np
from scipy.signal import hilbert, welch
from scipy.stats import entropy

def envelope_correlation(eeg_signal, audio_envelope):
    """
    Compute the correlation between the envelope of an EEG signal and an audio envelope.
    
    Parameters:
        eeg_signal (np.ndarray): The EEG signal.
        audio_envelope (np.ndarray): The auditory envelope.
    
    Returns:
        float: Correlation coefficient.
    """
    eeg_envelope = np.abs(hilbert(eeg_signal))
    return np.corrcoef(audio_envelope, eeg_envelope)[0, 1]

def spectral_entropy(eeg, fs):
    """
    Calculate the spectral entropy of an EEG signal.
    
    Parameters:
        eeg (np.ndarray): EEG signal.
        fs (int): Sampling frequency.
    
    Returns:
        float: Spectral entropy.
    """
    freqs, psd = welch(eeg, fs, nperseg=fs*2)
    psd_norm = psd / np.sum(psd)
    return entropy(psd_norm)
