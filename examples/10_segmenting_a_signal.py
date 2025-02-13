#!/usr/bin/env python
"""
Example 10: Segmenting a Signal
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    fs = 250
    duration = 10
    t = np.linspace(0, duration, fs * duration, endpoint=False)
    eeg_signal = (1 + 0.1 * t) * np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(len(t))
    segment_length = fs  # 1-second windows
    segments = np.array_split(eeg_signal, duration)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, eeg_signal)
    plt.title("Original EEG Signal (Non-Stationary)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

    plt.subplot(2, 1, 2)
    for i, segment in enumerate(segments):
        seg_t = np.linspace(i, i + 1, len(segment), endpoint=False)
        plt.plot(seg_t, segment, label=f"Segment {i+1}")
    plt.title("Segmented EEG Signal (1-Second Windows)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
