import solution
import unittest

class TestSolution(unittest.TestCase):
    def test_f_c(self):
        self.assertTrue(solution.f_c.__doc__)

        for i in range(-10, 10):
            self.assertEqual(4, solution.f_c(i))

    def test_f_x(self):
        for x in range(-10, 10):
            for a in range(-10, 10):
                for b in range(-10, 10):
                    self.assertEqual(a*x + b, solution.f_x(x, a, b))

    def test_sum(self):
        for x in range(-10, 10):
            expected = 0
            for i in range(1, 4):
                expected += solution.f_x(x, i, i)

            self.assertEqual(expected, solution.sum(x))


if __name__ == '__main__':
    unittest.main()

