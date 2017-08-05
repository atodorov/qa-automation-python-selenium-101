# Module 02: Data types and data structures

## Preparation

* Read chapter 03 from Dive into Python;
* Read chapter [Built-in types](https://docs.python.org/3/library/stdtypes.html)
from Python's documentation.

## Main data types

Data types represent values with common properties. For example `int` represents all
integer numbers. You can perform comparison and mathematical operations on `int` numbers.
`str` is the type representing text values.

In Python the main data types are `int`, `float`, `boolean`, `str`, `list`, `dict`,
`tuple` and `set`! Operators for these types are defined in the documentation and will
be used in the tasks below. We will explain them as we go along!


## DateTime types

Python has special types for working with dates and times. They live in the
[datetime module](https://docs.python.org/3/library/datetime.html).

    >>> from datetime import datetime, timedelta
    >>> datetime.now()
    datetime.datetime(2017, 8, 5, 23, 43, 50, 500589)
    >>> datetime.now().isoformat()
    '2017-08-05T23:44:02.508418'
    >>> datetime.now().year
    2017
    >>> datetime.now() - timedelta(days=7)
    datetime.datetime(2017, 7, 29, 23, 44, 33, 101454)


## Tasks & homework

* Implement a function `num_add(a, b)` which adds two numbers together
* Implement a function `num_sub(a, b)` which subtracts two numbers
* Implement a function `num_mul(a, b)` which multiplies two numbers
* Implement a function `num_div(a, b)` which divides the two numbers
* Implement a function `num_floor(a, b)` which implements floor division
* Implement a function `num_rem(a, b)` which implements remainder division
* Define boolean constant `IS_TRUE`
* Define boolean constant `IS_FALSE`
* Define the `PANCAKE_INGREDIENTS` dictionary to include the following keys and values

        flour - 2
        eggs - 4
        milk - 200
        butter - False
        salt - 0.001

* Implement a function `ingredient_exists(ingr, dict)` which returns boolean if the
ingredient `ingr` exists in the dictionary `dict
* Implement a function `fatten_pancakes(dict)` which returns a dictionary. The return
value contains the pancake ingredients where `eggs == 6` and `butter == True`.
**NOTE:** don't change the `PANCAKE_INGREDIENTS` constant! Use `dict.copy()` method!
* Implement a function `add_sugar(dict)` which adds 'sugar' to the list of ingredients
and returns a new dictionary
* Implement a function `remove_salt(dict)` which removes 'salt' from the list of
igredients and returns a new dictionary
* Define a list called `FIBONACCI_NUMBERS` which contains the first 12 Fibonacci numbers:

        1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

* Implement a function `add_fibonacci(lst)` which extends the list of numbers with
the next [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
* Implement a function `fib_exists(lst, n)` which returns boolean. The function checks
if the number `n` exists in the Fibonacci sequence `lst`
* Implement a function `which_fib(lst, n)` which returns integer. This is the index
of the number `n` inside the sequence `lst` counting from 1.

**TIP:** Use the `test.py` file to validate your solution is correct.
