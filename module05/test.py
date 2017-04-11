import unittest

class ExampleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpClass executes only once. CREATE DATABASE;"
        print

    def setUp(self):
        print "    setUp executes before every test method!"

    def tearDown(self):
        print "    tearDown executes after every test method!"

    @classmethod
    def tearDownClass(cls):
        print
        print "tearDownClass executes only once. DROP DATABASE;"

    def test_first_method(self):
        print "        This is the first test. It will PASS"
        assert True

    def test_second_method(self):
        print "        This is the second test. It will FAIL"
        assert False

    def test_zzzzz(self):
        print "        This is the last test. It will PASS"
        assert True

if __name__ == "__main__":
    unittest.main()
