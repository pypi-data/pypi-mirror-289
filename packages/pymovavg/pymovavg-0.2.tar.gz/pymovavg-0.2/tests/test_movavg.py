# tests/test_movavg.py

import unittest
from pymovavg import movavg

class TestMovavg(unittest.TestCase):
    
    def test_mean_moving_average(self):
        signal = [1, 5, 3, 8, 6]
        window_size = 3
        result = movavg(signal, window_size, mode='mean')
        expected = [1.0, 3.0, 4.666666666666667, 5.666666666666667, 6.0]
        self.assertAlmostEqual(result, expected, places=6)
    
    def test_median_moving_average(self):
        signal = [1, 5, 3, 8, 6]
        window_size = 3
        result = movavg(signal, window_size, mode='median')
        expected = [1.0, 3.0, 5.0, 6.0, 6.0]
        self.assertEqual(result, expected)
    
    def test_empty_signal(self):
        with self.assertRaises(ValueError):
            movavg([], 3, mode='mean')
    
    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            movavg([1, 2, 3], 3, mode='invalid')

if __name__ == '__main__':
    unittest.main()
