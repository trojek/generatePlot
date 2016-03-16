import unittest
from plot import count_mean

class PlotTestCase(unittest.TestCase):
    """Tests for 'plot.py'."""

    def test_mean_from_list(self):
        self.assertEqual(count_mean([2, 10, 3, 7,18]), 8)

if __name__ == '__main__':
    unittest.main()
