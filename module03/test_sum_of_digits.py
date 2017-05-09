import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_sum_all_digits_of_a_number(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)
        self.assertEqual(sum_of_digits(-10), 1)

    def test_check_string(self):
        self.assertRaises(RuntimeError, sum_of_digits, "Pesho")
        # which is the same as
        with self.assertRaises(RuntimeError):
            sum_of_digits("Pesho")


if __name__ == '__main__':
    unittest.main()
