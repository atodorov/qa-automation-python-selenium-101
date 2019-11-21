import unittest
from datetime import datetime

class ExampleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass executes only once. CREATE DATABASE;")

    def setUp(self):
        print("    setUp executes before every test method!")

    def tearDown(self):
        print("    tearDown executes after every test method!")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass executes only once. DROP DATABASE;")

    def test_first_method(self):
        print("        This is the first test. It will PASS")
        assert True

    def test_second_method(self):
        print("        This is the second test. It will FAIL")
        assert False

    def test_zzzzz(self):
        print("        This is the last test. It will PASS")
        assert True


class FlakyTest(unittest.TestCase):
    '''
        Execute this several times quickly to make it fail!
    '''
    def do_fail(self):
        if datetime.now().second % 3 == 0:
            raise Exception('I am a flaky test')

    def test_myself(self):
        self.do_fail()

if __name__ == "__main__":
    unittest.main()
