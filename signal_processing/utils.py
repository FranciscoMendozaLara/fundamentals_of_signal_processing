# signal_processing/utils.py

import numpy as np
import pywt

def compute_wavelet_transform(data, scales, wavelet='cmor', sampling_period=1.0):
    """
    Compute the continuous wavelet transform.
    
    Parameters:
        data (np.ndarray): Input signal.
        scales (np.ndarray): Array of scales.
        wavelet (str): Wavelet name (default 'cmor').
        sampling_period (float): Sampling period.
    
    Returns:
        tuple: (coefficients, frequencies)
    """
    coefficients, frequencies = pywt.cwt(data, scales, wavelet, sampling_period=sampling_period)
    return coefficients, frequencies
