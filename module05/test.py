import sys
import unittest
import unittest.mock
from io import StringIO

import test_calculator

class TestCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        """
            Will fail if the test_calculator module doesn't have a
            CalculatorTestCase class defined!
        """
        self.test_case_class = test_calculator.CalculatorTestCase
        self.calculator_functions = ['add', 'subtract', 'multiply', 'divide']

    def test_attributes_exist(self):
        """
            Validate that all test methods for the calculator.py program
            follow the naming convention test_<function_name>
        """
        for attr in self.calculator_functions:
            self.assertTrue(hasattr(self.test_case_class, 'test_%s' % attr))

    def test_calculator_tests_must_pass(self):
        """
            Validate that when executed the test cases for the calculator
            will actually PASS. We do this by executing them.
        """
        suite = unittest.TestSuite()
        for attr in self.calculator_functions:
            suite.addTest(self.test_case_class('test_%s' % attr))

        result = unittest.TestResult()

        suite.run(result)
        self.assertTrue(result.wasSuccessful())

    def test_calculator_tests_call_expected_calculator_functions(self):
        """
            Validate that calculator tests will actually execute
            the expected functions from the calculator module. We do this
            by mocking the functions, executing the test methods and
            verifying that the test method actually called the mocked
            function!
        """
        for attr in self.calculator_functions:
            with unittest.mock.patch('test_calculator.calculator.%s' % attr) as calc_func:
                t = self.test_case_class('test_%s' % attr)
                result = t.run()

                # NOTE: we should get an error like this
                # AssertionError: 5 != <MagicMock name='add()'>
                # when executing the calculator test methods
                self.assertFalse(result.wasSuccessful())

                # however we make sure that all functions in the calculator module
                # have actually been called
                self.assertTrue(calc_func.called)

    def test_calculator_interactive_not_executed_when_imported(self):
        """
            Verify that the interactive commands are not executed when
            the calculator module is imported. We do this by mocking
            the input function to deal away with interactiveness in the test
            and mocking sys.stdout to assert that nothing was printed!
        """
        if 'calculator' in sys.modules:
            # force import of the calculator module
            # b/c already imported from test_calculator
            del sys.modules['calculator']

        with unittest.mock.patch('sys.stdout', new_callable=StringIO) as _stdout, \
             unittest.mock.patch('builtins.input', return_value=1) as _input:
            import calculator
            # print was never called
            self.assertEqual('', _stdout.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
