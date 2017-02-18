import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_turn_a_list_of_digits_into_a_number(self):
        self.assertEqual(to_number([1, 2, 3]), 123)
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)

if __name__ == '__main__':
    unittest.main()
