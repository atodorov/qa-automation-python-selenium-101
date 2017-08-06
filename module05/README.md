# Module 05: Testing in Python

## Preparation

* Read Chapter [26.4. unittest - Unit testing framework](https://docs.python.org/3/library/unittest.html);


In Python tests should inherit the standard `unittest.TestCase` class. Notable
methods are:

* `setUp(self)` - initialization of test environment; This is called immediately before calling the test method;
* `tearDown(self)` - clean up of test environment; Method called immediately after the test method has been called
  and the result recorded. This is called even if the test method raised an exception, so the implementation in
  subclasses may need to be particularly careful about checking internal state;
* `setUpClass()` - A class method called before tests in an individual class run. setUpClass is called with
  the class as the only argument and must be decorated as a `@classmethod`;
* `tearDownClass()`- A class method called after tests in an individual class have run. tearDownClass is called
  with the class as the only argument and must be decorated as a `@classmethod`;
* `runTest(self)` - if all tests go into one method or
* `test_XYZ(self)` - for testing specific functionality
* `assertXYZ(...)` - for asserting various conditions

The standard documentation contains the
[list of assert methods](https://docs.python.org/3/library/unittest.html#assert-methods)!

You can write asserts using several different styles:

    assert 4 == 4
    self.assertEqual(4, 4)
    self.assertTrue(4 == 4)
    self.assertTrue(-1)

    assert 4 < 5
    self.assertTrue(4 < 5)


## Demonstration of setUp/tearDown and test execution

Execute `test_example.py` to see the order of execution of all set-up/tear-down and test methods!


## Flaky tests

These are tests which randomly fail without an obvious reason. The root cause behind them
is either timing issues (async JavaScript in a web context) or mismatch between the actual
environment the test is running into (DB records, files on disk, etc) and the environment
the tester imagined when the test was created! Execute `test_example.py` several times quickly
to trigger a flaky failure.

## Object oriented principles for testers

    class MyTestCase(unittest.TestCase):
        """
            This is a class definition. A class describes how something works
            but it doesn't physically exist! A class is an abstration, it tells
            us what the general behavior is via it's methods (functions inside the class)
            and attributes (variables inside the object).
    
    
            An object is an instance of a class. An object exists into memory and is
            assigned to a variable. We can create objects as we like, execute their
            methods (via obj_name.method_name(<params>)) and
            access their attributes (via obj_name.attr_name).
    
    
            In Python all tests must inherit from unittest.TestCase. This means
            that the unittest.TestCase class must be inside the inheritance list
            when defining the class as shown above!
        """
    
        def setUp(self):
            """
                All methods of the class receive a first parameter called self.
                Python does this automatically but we have to declare it!
    
                The self variable represents the current instance of this class.
                We can use it to access attributes and call other methods of the same
                class!
            """
            # here we assign a value to the name attribute.
            # self.name is accessible outside this method
            self.name = 'Gosho'
    
            # on the other hand ime is a local variable.
            # it will not be accessible outside this method
            ime = 'Ivan'
    
        def test_something(self):
            # we can access object attributes and other methods
            # using the self variable
            print(self.name)
    
            # but we can't access variables defined outside the current method
            # if you uncomment the statement below it will raise
            # NameError: name 'ime' is not defined
            #print(ime)


NOTE: When testing in Python we don't instantiate (create objects) from the
test classes by hand. The test runner does this for us automatically when the
`unittest.main()` statement is executed in the main block.


More general information about OOP can be found in [module04](../module04) of this guide!


## Tasks & homework

* Examine the `calculator.py` program and
  * write tests for all of its functions. Use the
    `test_calculator.py::CalculatorTestCase::test_<function_name>` naming scheme for your
    test methods!
  * Modify `calculator.py` to avoid executing the interactive commands when testing
  * **TIP**: use `test.py` to verify that your tests are correct!


* Examine the existing test suite (for all previous tasks) in details. What other tests can be
written ? Write them!
