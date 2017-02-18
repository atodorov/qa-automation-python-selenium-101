import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)
        self.assertEqual(fib_number(10), 11235813213455)

if __name__ == '__main__':
    unittest.main()
