import unittest
from solution import *

class FirstDayTests(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        # It's a volcano name!
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(count_vowels("grrrrgh!"), 0)
        self.assertEqual(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22)
        self.assertEqual(count_vowels("A nice day to code!"), 8)

        with self.assertRaises(ValueError):
           count_vowels("")

class Count_Vowels(unittest.TestCase):
    def test_with_none(self):
        with self.assertRaises(TypeError):
            count_vowels(None)

    def test_negative_value(self):
        with self.assertRaises(AssertionError):
            count_vowels(-765)

        with self.assertRaises(Exception):
            count_vowels(-765)


if __name__ == '__main__':
    unittest.main()
