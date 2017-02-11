# Session 01: Structure of a Python program

## Preparation

* Read chapter 02 from Dive into Python!

## Program structure

Each Python program consists of module imports, statements, function definitions,
class definitions and an optional main block! For example:

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


## Function signatures

Functions are defined as follows:

    def functionName([list of parameters]):
        """
            Doc-string documenting what this function does.
        """
        <function body>

Functions return result via the `return <value>` statement.

## Comments and doc-strings

Everything after a `#` (hash sign) is a comment and is ignored by the Python interpreter!

## Modules and imports

Shared functionality is defined inside a Python module. A module may be:

- a `file_name.py` or
_ a directory with an `__init__.py` file inside

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

## Starting Python programs

In the terminal type:

    $ python myprogram.py


## Tasks & homework

* Create a program named `solution.py`
* Define a variable named `employee` with a value of `Ivan`
* Define a function with the following signature:

        def helloFrom():
            pass

* Document what this function does
* Extend the function to accept only one parameter
* Define a function body which returns the string `Hello from <value_of_the_parameter>`

**TIP:** Use `test.py` to validate your solution is correct.
