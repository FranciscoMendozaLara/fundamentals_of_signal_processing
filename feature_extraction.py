import numpy as np
from scipy.signal import hilbert
from scipy.stats import entropy

def envelope_correlation(eeg_signal, audio_envelope):
    """
    Computes the correlation between the EEG envelope and an auditory envelope.
    """
    eeg_envelope = np.abs(hilbert(eeg_signal))
    return np.corrcoef(audio_envelope, eeg_envelope)[0, 1]

def spectral_entropy(eeg, fs):
    """
    Calculates the spectral entropy of an EEG signal.
    """
    from scipy.signal import welch
    freqs, psd = welch(eeg, fs, nperseg=fs*2)
    psd_norm = psd / np.sum(psd)
    return entropy(psd_norm)
