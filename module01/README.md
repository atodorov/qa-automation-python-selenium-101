# Module 01: Structure of a Python program

## Preparation

* Read chapter 02 from Dive into Python!

## Starting the Python interpreter

An interactive session (useful for trying out things) can be started from the
terminal by typing:

    $ python
    Python 3.5.1 (default, Sep 15 2016, 08:30:32)
    [GCC 4.8.3 20140911 (Red Hat 4.8.3-9)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print("Hello World")
    Hello World
    >>>

To exit the interactive interpreter type `exit()` or press Ctrl+D.

## Starting Python programs

Any Python program can be started by passing the file name as argument to the
Python intepreter. In the terminal type:

    $ python myprogram.py

## Program structure

Each Python program consists of several basic blocks:

- module imports
- statements
- function definitions
- class definitions
- an optional main block!

For example:

    import os

    name = 'Alex'

    def sayHello(who):
        print "Hello %s" % who

    class Person(object):
        pass

    if __name__ == "__main__":
        sayHello(name)
        sayHello('Maria')


Program blocks are recognized by their indentation level. There are no `begin` or `end`
keywords. In Python we use 4 spaces for indentation!

## Variables

Variables are used to store data in the program. You can assign values to variables by
using the assignment operator (`=`) like so:

    name = 'Ivan'
    print('Hello', name)

    name = 'Alex'
    print('Good afternoon', name)


Try this program in the interactive interpreter!


## Functions

Functions are sequence of operations which can be applied multiple times
onto different arguments. For example a function that can send email
will perform the exact same operations every time but the message and the
recipient can be controlled via arguments.

Functions are defined as follows:

    def functionName([list of parameters]):
        """
            Doc-string documenting what this function does.
        """
        <function body>
        return <value>

The function name and list of parameters is called a function signature!

Functions return result via the `return <value>` statement. When `return`
is executed the function execution completes immediately. If no `return`
statement is specified then the default return value is `None`!

For example a function to calculate the perimeter of a square will look like this:

    def perimeter_of_square(side):
        return 4 * side

A function to calculate perimeter of triangle will look like this:

    def perimeter_of_triangle(a, b, c):
        return a + b + c


In the example above the variables `a`, `b` and `c` are called parameters. Parameter
variables are accessible everywhere inside the function body. When we want to perform
a calculation for a particular triangle then we call(execute) the function like this:

    >>> perimeter_of_triangle(1, 2, 3)
    6
    >>> perimeter_of_triangle(2, 4, 6)
    12

The values `1`, `2`, `3` are called arguments! They are assigned to the parameter variables
when the function is executed.



## Comments and doc-strings

Everything after a `#` (hash sign) is a comment and is ignored by the Python interpreter!
After defining a function, module or class you can use a triple quoted string to provide
description of what that object does. This is called the doc-string of the object and is
used by the integrated help system in Python. For example:

    >>> import os
    >>> help(os)
    >>> # ^^^ press q to quit
    >>>
    >>> def perimeter_of_triangle(a, b, c):
    ...     '''Calculates the primeter of a triangle'''
    ...     return a + b + c
    ... 
    >>> help(perimeter_of_triangle)
    
    Help on function perimeter_of_triangle in module __main__:
    
    perimeter_of_triangle(a, b, c)
        Calculates the primeter of a triangle
    (END)


## Modules and imports

Shared functionality is defined inside Python modules. A module may be:

- a `file_name.py` or
- a directory with an `__init__.py` file inside

Modules are loaded and used into the program via:

    import mymodule
    from another_module import sayHello

    mymodule.whatTimeIsIt()
    sayHello('Alex')

After a module has been imported you can read its documentation with

    help(mymodule)

All modules from the Python standard library are documented at https://docs.python.org

The module search path is defined in the `sys.path` variable! This is a list of
directories in which modules are searched (from first to last). It can also be used
to alter the search path to include non-standard directories!


## Main block

A program may have an optional main block. It is defined as an if statement at the
top-most level:

    if __name__ == "__main__":
        <body of the main block>

Main blocks are executed only if the file is executed as a program,
e.g. `python myfile.py`. If the file is loaded as a module, e.g. `import myfile`
the main block is not executed.

The main block is optional. You can execute functions and assign to variables
at the top-most level as well. However this will have undesired effects if
your files are imported as modules!


## Tasks & homework

* Create a program named `solution.py`
* Define a function with the following signature `def f_c(X)` which
  returns the constant 4 for any input parameter.
* Document what the function `f_c` does
* Write a function `f_x(x, a, b)` which implements the formula `f(x) = a*x + b`!
* Write a function `sum(x)` which returns the sum of `f_x()` called 3 times with
  parameters `x, 1, 1`, `x, 2, 2`, `x, 3, 3`!

**TIP:** Use `test.py` to validate your solution is correct.

