# signal_processing/filters.py

import numpy as np
from scipy.signal import butter, lfilter, firwin

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """
    Apply a Butterworth bandpass filter.
    
    Parameters:
        data (np.ndarray): Input signal.
        lowcut (float): Low cutoff frequency in Hz.
        highcut (float): High cutoff frequency in Hz.
        fs (int): Sampling frequency.
        order (int): Filter order.
    
    Returns:
        np.ndarray: Filtered signal.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

def iir_filter(data, lowcut, highcut, fs, order=4):
    """
    Apply an IIR bandpass filter (same as bandpass_filter using Butterworth).
    """
    return bandpass_filter(data, lowcut, highcut, fs, order=order)

def fir_filter(data, lowcut, highcut, fs, numtaps=101):
    """
    Apply an FIR bandpass filter.
    
    Parameters:
        data (np.ndarray): Input signal.
        lowcut (float): Low cutoff frequency in Hz.
        highcut (float): High cutoff frequency in Hz.
        fs (int): Sampling frequency.
        numtaps (int): Number of FIR filter taps.
    
    Returns:
        np.ndarray: Filtered signal.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    taps = firwin(numtaps, [low, high], pass_zero=False)
    return lfilter(taps, 1.0, data)
