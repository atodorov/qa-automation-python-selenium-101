import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_employee(self):
        self.assertEqual(solution.employee, 'Ivan')

    def test_helloFrom_docstring_exists(self):
        self.assertTrue(solution.helloFrom.__doc__)

    def test_helloFrom_without_parameters(self):
        with self.assertRaises(TypeError):
            solution.helloFrom()

    def test_helloFrom_with_two_parameters(self):
        with self.assertRaises(TypeError):
            solution.helloFrom('Ivan', 'Alex')

    def test_helloFrom_with_Ivan(self):
        self.assertEqual(solution.helloFrom('Ivan'), 'Hello from Ivan')
        self.assertEqual(solution.helloFrom('Alex'), 'Hello from Alex')

if __name__ == '__main__':
    unittest.main()

