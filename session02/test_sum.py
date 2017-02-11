import unittest
import solution

class TestSum(unittest.TestCase):
    def TestSum(self):
        self.assertEqual(4, solution.sum(2, 2))
        self.assertEqual(5, solution.sum(2, 3))
        self.assertEqual(0, solution.sum(2, -2))
        self.assertEqual(-1, solution.sum(-3, 2))

if __name__ == '__main__':
    unittest.main()
