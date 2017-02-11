import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(prime_number(7))
        self.assertFalse(prime_number(8))

if __name__ == '__main__':
    unittest.main()
