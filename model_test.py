# Testing Package
import unittest

# File to be tested
import model as model


# Class that holds the tests
class TestPrime(unittest.TestCase):
    def setUp(self):
        pass

    def test_format_time(self):
        self.assertEqual("00:00:00", model.format_time(0))
        self.assertEqual("00:00:05", model.format_time(5))
        self.assertEqual("00:01:00", model.format_time(60))
        self.assertEqual("00:01:15", model.format_time(75))
        self.assertEqual("00:10:00", model.format_time(600))
        self.assertEqual("01:00:00", model.format_time(600 * 6))
        self.assertEqual("1 day 00:00:01", model.format_time(86401))
        self.assertEqual("2 days 00:00:02", model.format_time(86401 * 2))


if __name__ == '__main__':
    unittest.main()