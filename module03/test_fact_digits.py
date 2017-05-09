import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_fact_digits(self):
        self.assertEqual(fact_digits(111), 3)
        self.assertEqual(fact_digits(145), 145)
        self.assertEqual(fact_digits(999), 1088640)

    def test_factoriel_increases_in_range_1_10(self):
        previous = 0

        for x in range(1, 10):
            result = fact_digits(x)
            # print x, result, previous
            # self.assertTrue(result > previous)
            assert result > previous
            previous = result


if __name__ == '__main__':
    unittest.main()
