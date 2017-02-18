import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(3), [1, 1, 2])
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

if __name__ == '__main__':
    unittest.main()
