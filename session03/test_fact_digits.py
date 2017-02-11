import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_fact_digits(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)

if __name__ == '__main__':
    unittest.main()
