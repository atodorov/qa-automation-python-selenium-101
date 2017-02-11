import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_turn_a_number_into_list_of_digits(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

if __name__ == '__main__':
    unittest.main()
