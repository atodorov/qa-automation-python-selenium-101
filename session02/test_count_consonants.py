import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)
        # It's a volcano name!
        self.assertEqual(count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(count_consonants("grrrrgh!"), 7)
        self.assertEqual(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"), 44)
        self.assertEqual(count_consonants("A nice day to code!"), 6)

if __name__ == '__main__':
    unittest.main()
