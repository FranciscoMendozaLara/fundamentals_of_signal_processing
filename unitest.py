import unittest
from eeg_processing import simulate_eeg

class TestSimulateEEG(unittest.TestCase):
    def test_signal_length(self):
        fs = 250
        duration = 10
        t, eeg = simulate_eeg(fs, duration)
        self.assertEqual(len(t), fs * duration)
        self.assertEqual(len(eeg), fs * duration)

if __name__ == "__main__":
    unittest.main()
