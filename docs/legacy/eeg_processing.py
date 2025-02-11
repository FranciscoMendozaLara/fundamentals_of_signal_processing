import numpy as np
from scipy.signal import butter, lfilter

def simulate_eeg(fs, duration):
    """
    Simulates an EEG signal with components from delta, theta, alpha, beta, and gamma bands,
    plus random noise.

    Parameters:
        fs (int): Sampling frequency in Hz.
        duration (int): Duration of the signal in seconds.

    Returns:
        tuple: (time, eeg_signal)
            - time (numpy.ndarray): Time vector.
            - eeg_signal (numpy.ndarray): Simulated EEG signal.
    """
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    delta = 1.5 * np.sin(2 * np.pi * 2 * t)
    theta = 1.0 * np.sin(2 * np.pi * 6 * t)
    alpha = 0.8 * np.sin(2 * np.pi * 10 * t)
    beta = 0.5 * np.sin(2 * np.pi * 20 * t)
    gamma = 0.3 * np.sin(2 * np.pi * 40 * t)
    noise = 0.2 * np.random.randn(len(t))
    eeg_signal = delta + theta + alpha + beta + gamma + noise
    return t, eeg_signal

def band_power(eeg, fs, band):
    """
    Calculates the power of a specific frequency band in an EEG signal.
    """
    from scipy.signal import welch
    fmin, fmax = band
    freqs, psd = welch(eeg, fs, nperseg=fs*2)
    return np.sum(psd[(freqs >= fmin) & (freqs <= fmax)])

def highpass_filter(data, cutoff, fs, order=4):
    """
    Applies a high-pass filter to the signal.
    """
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return lfilter(b, a, data)
