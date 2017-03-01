import sys
import solution
import unittest

try:
    # works on Python 2.7
    import mock
except ImportError:
    # works on Python 3
    from unittest import mock

try:
    # works on Python 2.7
    from StringIO import StringIO
except ImportError:
    # works on Python 3
    from io import StringIO

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

    @mock.patch.object(solution, 'print', create=True)
    def test_print_doc_on_python3(self, _print):
        if sys.version_info.major < 3:
            return

        # execute the method under test
        solution.print_doc(solution.helloFrom)

        # validate that print was called only once
        self.assertEqual(_print.call_count, 1)

        # validate that print was called with the doc-string of solution.helloFrom
        _print.assert_called_with(solution.helloFrom.__doc__)

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_doc_on_python2(self, _stdout):
        if sys.version_info.major > 2:
            return

        # execute the method under test
        solution.print_doc(solution.helloFrom)

        # validate that print was called with the doc-string of solution.helloFrom
        self.assertEqual(_stdout.getvalue().strip(), solution.helloFrom.__doc__.strip())

if __name__ == '__main__':
    unittest.main()

