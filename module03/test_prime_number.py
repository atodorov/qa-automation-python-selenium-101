import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_prime_number(self):
        self.assertEquals(False, prime_number(9))
        self.assertTrue(prime_number(7))
        self.assertEquals(False, prime_number(8))

if __name__ == '__main__':
    unittest.main()
