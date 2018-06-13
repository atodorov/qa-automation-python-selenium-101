import copy
import unittest
from solution import *

class TestSolution(unittest.TestCase):
    def test_num_add(self):
        int_result = num_add(1, 2)
        # validate type of result b/c Python will consider 3 and 3.0 equal!
        self.assertTrue(isinstance(int_result, int))
        self.assertEqual(int_result, 3)
        self.assertEqual(num_add(2, 1), 3)

        float_result = num_add(1.5, 2.5)
        self.assertTrue(isinstance(float_result, float))
        self.assertEqual(float_result, 4.0)

    def test_num_sub(self):
        self.assertEqual(num_sub(1, 2), -1)
        self.assertEqual(num_sub(2, 1), 1)
        self.assertEqual(num_sub(1.5, 2.5), -1.0)

    def test_num_mul(self):
        self.assertEqual(num_mul(3, 2), 6)
        self.assertEqual(num_mul(2, 3), 6)
        self.assertEqual(num_mul(2.5, 4), 10.0)

    def test_num_div(self):
        self.assertEqual(num_div(3, 2), 1.5)
        self.assertEqual(num_div(2, 3), 0.6666666666666666)
        self.assertEqual(num_div(3.0, 2), 1.5)

    def test_num_floor(self):
        self.assertEqual(num_floor(10, 4), 2)
        self.assertEqual(num_floor(4, 10), 0)

    def test_num_rem(self):
        self.assertEqual(num_rem(10, 4), 2)
        self.assertEqual(num_rem(10, 5), 0)
        self.assertEqual(num_rem(4, 10), 4)

    def test_boolean_constants(self):
        self.assertTrue(IS_TRUE)
        self.assertTrue(isinstance(IS_TRUE, bool))
        self.assertFalse(IS_FALSE)
        self.assertTrue(isinstance(IS_FALSE, bool))

    def test_pancake_ingredients(self):
        for key in PANCAKE_INGREDIENTS.keys():
            self.assertTrue(key in ['flour', 'eggs', 'milk', 'butter', 'salt'])
        self.assertEqual(PANCAKE_INGREDIENTS['flour'], 2)
        self.assertEqual(PANCAKE_INGREDIENTS['eggs'], 4)
        self.assertEqual(PANCAKE_INGREDIENTS['milk'], 200)
        self.assertFalse(PANCAKE_INGREDIENTS['butter'])
        self.assertEqual(PANCAKE_INGREDIENTS['salt'], 0.001)

    def test_ingredient_exists(self):
        self.assertIs(ingredient_exists('flour', PANCAKE_INGREDIENTS), True)
        self.assertIs(ingredient_exists('FLOUR', PANCAKE_INGREDIENTS), False)
        self.assertTrue(ingredient_exists('salt', PANCAKE_INGREDIENTS))
        self.assertFalse(ingredient_exists('sugar', PANCAKE_INGREDIENTS))

        # test that the global PANCAKE_INGREDIENTS variable is not used
        # but rather the parameter of this function is used inside its body!
        coffee_recipe = {
            'sugar': 1,
            'water': 200,
            'coffee': 1,
            'heat': True
        }
        self.assertTrue(ingredient_exists('sugar', coffee_recipe))

    def test_fatten_pancakes(self):
        TEST_INGREDIENTS = PANCAKE_INGREDIENTS.copy()
        TEST_INGREDIENTS['canary'] = 404

        fat_ingredients = fatten_pancakes(TEST_INGREDIENTS)

        # test that result is a new dictionary
        self.assertNotEqual(id(fat_ingredients), id(TEST_INGREDIENTS))

        self.assertEqual(fat_ingredients['flour'], 2)
        self.assertEqual(fat_ingredients['eggs'], 6)
        self.assertEqual(fat_ingredients['milk'], 200)
        self.assertTrue(fat_ingredients['butter'])
        self.assertEqual(fat_ingredients['salt'], 0.001)

        # test that the input parameter was used
        self.assertEqual(fat_ingredients['canary'], 404)

        # test that PANCAKE_INGREDIENTS didn't change
        self.test_pancake_ingredients()

    def test_add_sugar(self):
        TEST_INGREDIENTS = PANCAKE_INGREDIENTS.copy()
        TEST_INGREDIENTS['canary'] = 404

        with_sugar = add_sugar(TEST_INGREDIENTS)

        # test that result is a new dictionary
        self.assertNotEqual(id(with_sugar), id(TEST_INGREDIENTS))

        self.assertEqual(with_sugar['flour'], 2)
        self.assertEqual(with_sugar['eggs'], 4)
        self.assertEqual(with_sugar['milk'], 200)
        self.assertFalse(with_sugar['butter'])
        self.assertEqual(with_sugar['salt'], 0.001)
        self.assertTrue(with_sugar['sugar'])

        # test that the input parameter was used
        self.assertEqual(with_sugar['canary'], 404)

        # test that PANCAKE_INGREDIENTS didn't change
        self.test_pancake_ingredients()

    def test_remove_salt(self):
        TEST_INGREDIENTS = PANCAKE_INGREDIENTS.copy()
        TEST_INGREDIENTS['canary'] = 404

        no_salt = remove_salt(TEST_INGREDIENTS)

        # test that result is a new dictionary
        self.assertNotEqual(id(no_salt), id(TEST_INGREDIENTS))

        self.assertFalse('salt' in no_salt.keys())

        self.assertEqual(no_salt['flour'], 2)
        self.assertEqual(no_salt['eggs'], 4)
        self.assertEqual(no_salt['milk'], 200)
        self.assertFalse(no_salt['butter'])

        # test that the input parameter was used
        self.assertEqual(no_salt['canary'], 404)

        # test that PANCAKE_INGREDIENTS didn't change
        self.test_pancake_ingredients()

    def test_fibonacci_numbers(self):
        self.assertEqual(FIBONACCI_NUMBERS, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])

    def test_add_fibonacci(self):
        NUMBERS = copy.deepcopy(FIBONACCI_NUMBERS)
        self.assertEqual(NUMBERS, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(add_fibonacci(NUMBERS)[-1], 233)
        self.assertEqual(add_fibonacci(NUMBERS)[-1], 377)
        self.assertEqual(add_fibonacci(NUMBERS)[-1], 610)

    def test_fib_exists(self):
        # validate input parameter is in use
        self.assertIs(fib_exists([1, 1], 2), False)

        self.assertIs(fib_exists(FIBONACCI_NUMBERS, 0), False)
        self.assertIs(fib_exists(FIBONACCI_NUMBERS, 1), True)
        self.assertTrue(fib_exists(FIBONACCI_NUMBERS, 144))

    def test_which_fib(self):
        # validate input parameter is in use
        with self.assertRaises(ValueError):
            which_fib([1, 1], 2)

        self.assertEqual(which_fib(FIBONACCI_NUMBERS, 1), 1)
        self.assertEqual(which_fib(FIBONACCI_NUMBERS, 55), 10)

        with self.assertRaises(ValueError):
            which_fib(FIBONACCI_NUMBERS, 99999)


if __name__ == '__main__':
    unittest.main()
