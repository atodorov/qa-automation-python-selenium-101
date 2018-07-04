# Module 03: If statements and loops

## Preparation

* Read sections 8.1, 8.2 and 8.3 from chapter 8
[Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
from Python's documentation to learn the syntax and semantics of `if`, `while`
and `for` statements.

## Control flow

In Python `if` and `while` statements are used to control program flow by
examining boolean conditions. Comparison operators are described in
[6.10 Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons),
boolean operations are described in 
[6.11 Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations).

The `for` statement is used to iterate over sequences. The basic sequence types are
`list` and `str` as well as `tuple`.

If statements and for loops are the backbone of most Python programs and
are quite handy when writing tests. All tasks below require the usage of both.



## Tasks & homework

* Implement all solutions into a file named `solution.py`

### Sum of all digits of a number

* Given an integer, implement a function, called `sum_of_digits(n)` that calculates the sum of n's digits.
* If a negative number is given, our function should work as if it was positive.
* Keep in mind that in Python, there is a special operator for integer division!

        >>> 5 / 2
        2.5
        >>> 5 // 2
        2
        >>> 5 % 2
        1

* Function signature

        def sum_of_digits(n):
            pass

### Turn a number into a list of digits

* Implement a function, called `to_digits(n)`, which takes an integer `n` and returns a list, containing the digits of `n`.
* Signature

        def to_digits(n):
            pass


### Turn a list of digits into a number

* Implement a function, called `to_number(digits)`, which takes a list of integers - digits and returns the number, containing those digits.
* Signature

        def to_number(digits):
            pass


### Vowels in a string

* Implement a function, called `count_vowels(str)`, which returns the count of all vowels in the string `str`.
**Count uppercase vowels as well!** The English vowels are `aeiouy`.
* Signature

        def count_vowels(str):
            pass


### Consonants in a string

* Implement a function, called `count_consonants(str)`, which returns the count of all consonants in the string `str`.
**Count uppercase consonants as well!** The English consonants are `bcdfghjklmnpqrstvwxz`.
* Signature

        def count_consonants(str):
            pass

### Prime Number

* Check if a given number is prime in `prime_number(number)` and return boolean result.
* For the purposes of this task consider 1 to be a prime number as well.
* Hint:

        >>> 5 % 2
        1

* Signature

        def prime_number(n):
            pass

### Factorial Digits

* Implement a function `fact_digits(n)`, that takes an integer and returns the sum of the factorials of each digit of `n`.
* For example, if n = 145, we want 1! + 4! + 5!
* Signature

        def fact_digits(n):
            pass

* Hint - use the functions that you have defined previously. What other functions
do you need ?

### First nth members of Fibonacci

* Implement a function, called `fibonacci(n)` that returns a list with the first `n` members of the Fibonacci sequence.
* Signature

        def fibonacci(n):
            pass

### Fibonacci number

* Implement a function, called `fib_number(n)`, which takes an integer `n` and returns a number,
which is formed by concatenating the first `n` Fibonacci numbers.
For example, if `n = 3`, the result is `112`.
* Signature

        def fib_number(n):
            pass

* Hint - use the functions that you have defined previously. What other functions
do you need?

### Palindrome

* Implement a function, called `palindrome(obj)`,
which takes a number or a string and checks if it is a representation is a palindrome.
For example, the integer `121` and the string `"kapak"` are palindromes. The function should work with both.
* Hint - check Python's [str()](https://docs.python.org/3/library/stdtypes.html#str) function
* Signature

        def palindrome(n):
            pass

### Char Histogram

* Implement a funcion, called `char_histogram(string)`, which takes a string and returns a dictionary,
where each key is a character from `string` and its value is the number of occurrences of that char in `string`.
* Signature

        def char_histogram(string):
            pass


**TIP:** Use `test.py` to validate your solution is correct.
