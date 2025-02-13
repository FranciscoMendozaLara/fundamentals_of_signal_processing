#!/usr/bin/env python
"""
Example 13: Calculating Band Power in EEG
"""

import numpy as np
from signal_processing.eeg import simulate_eeg, band_power
from signal_processing.config import BANDS, FS, DURATION

def main():
    t, eeg = simulate_eeg(FS, DURATION)
    print("Band Power Calculations:")
    for band_name, band_range in BANDS.items():
        power = band_power(eeg, FS, band_range)
        print(f"{band_name} band power: {power:.2f}")

if __name__ == '__main__':
    main()
