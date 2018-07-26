import unittest
from solution import *

class SolutionTests(unittest.TestCase):
    def test_char_histogram(self):
        self.assertEqual(char_histogram("Python!"), { 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1 })
        self.assertEqual(char_histogram("AAAAaaa!!!"), { 'A': 4, 'a': 3, '!': 3 })

    def test_count_consonants(self):
        self.assertEqual(count_consonants("Python"), 4)
        # It's a volcano name!
        self.assertEqual(count_consonants("Theistareykjarbunga"), 11)
        self.assertEqual(count_consonants("grrrrgh!"), 7)
        self.assertEqual(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"), 44)
        self.assertEqual(count_consonants("A nice day to code!"), 6)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Python"), 2)
        # It's a volcano name!
        self.assertEqual(count_vowels("Theistareykjarbunga"), 8)
        self.assertEqual(count_vowels("grrrrgh!"), 0)
        self.assertEqual(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"), 22)
        self.assertEqual(count_vowels("A nice day to code!"), 8)
        # empty string returns 0
        self.assertEqual(0, count_vowels(""))

    def test_count_vowels_with_none(self):
        with self.assertRaises(AttributeError):
            count_vowels(None)

    def test_count_negative_value(self):
        with self.assertRaises(Exception):
            count_vowels(-765)

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

    def test_fib_number(self):
        self.assertEqual(fib_number(3), 112)
        self.assertEqual(fib_number(10), 11235813213455)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), [1])
        self.assertEqual(fibonacci(2), [1, 1])
        self.assertEqual(fibonacci(3), [1, 1, 2])
        self.assertEqual(fibonacci(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_palindrome(self):
        self.assertTrue(palindrome(121))
        self.assertTrue(palindrome("kapak"))
        self.assertEqual(palindrome("abba"), True)
        self.assertEqual(palindrome("baba"), False)

    def test_prime_number(self):
        self.assertEqual(True, prime_number(1))
        self.assertEqual(True, prime_number(2))

        self.assertEqual(False, prime_number(9))
        self.assertTrue(prime_number(7))
        self.assertEqual(False, prime_number(8))

    def test_sum_all_digits_of_a_number(self):
        self.assertEqual(sum_of_digits(1325132435356), 43)
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(6), 6)
        self.assertEqual(sum_of_digits(-10), 1)

    def test_sum_of_digits_with_string_parameter(self):
        self.assertRaises(TypeError, sum_of_digits, "Pesho")
        # which is the same as
        with self.assertRaises(TypeError):
            sum_of_digits("Pesho")

    def test_turn_a_number_into_list_of_digits(self):
        self.assertEqual(to_digits(123), [1, 2, 3])
        self.assertEqual(to_digits(99999), [9, 9, 9, 9, 9])
        self.assertEqual(to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_turn_a_list_of_digits_into_a_number(self):
        self.assertEqual(to_number([1, 2, 3]), 123)
        self.assertEqual(to_number([3, 2, 1]), 321)
        self.assertEqual(to_number([9, 9, 9, 9, 9]), 99999)

if __name__ == '__main__':
    unittest.main()
