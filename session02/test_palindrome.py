import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(palindrome(121))
        self.assertTrue(palindrome("kapak"))
        self.assertFalse(palindrome("baba"))

if __name__ == '__main__':
    unittest.main()
