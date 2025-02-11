# signal_processing/eeg.py

import numpy as np
from scipy.signal import butter, lfilter, welch

def simulate_eeg(fs, duration):
    """
    Simulate an EEG signal composed of delta, theta, alpha, beta, gamma bands with noise.
    
    Parameters:
        fs (int): Sampling frequency (Hz)
        duration (int): Duration in seconds
    
    Returns:
        tuple: (t, eeg_signal)
            - t: time vector (numpy.ndarray)
            - eeg_signal: simulated EEG signal (numpy.ndarray)
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    delta = 1.5 * np.sin(2 * np.pi * 2 * t)
    theta = 1.0 * np.sin(2 * np.pi * 6 * t)
    alpha = 0.8 * np.sin(2 * np.pi * 10 * t)
    beta  = 0.5 * np.sin(2 * np.pi * 20 * t)
    gamma = 0.3 * np.sin(2 * np.pi * 40 * t)
    noise = 0.2 * np.random.randn(len(t))
    eeg_signal = delta + theta + alpha + beta + gamma + noise
    return t, eeg_signal

def band_power(eeg, fs, band):
    """
    Calculate the power in a specific frequency band using Welch's method.
    
    Parameters:
        eeg (np.ndarray): EEG signal.
        fs (int): Sampling frequency.
        band (tuple): Frequency band (fmin, fmax)
    
    Returns:
        float: power in the band.
    """
    fmin, fmax = band
    freqs, psd = welch(eeg, fs, nperseg=fs*2)
    return np.sum(psd[(freqs >= fmin) & (freqs <= fmax)])

def highpass_filter(data, cutoff, fs, order=4):
    """
    Apply a high-pass Butterworth filter to remove drift.
    
    Parameters:
        data (np.ndarray): Input signal.
        cutoff (float): Cutoff frequency in Hz.
        fs (int): Sampling frequency.
        order (int): Filter order.
    
    Returns:
        np.ndarray: Filtered signal.
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high')
    return lfilter(b, a, data)
