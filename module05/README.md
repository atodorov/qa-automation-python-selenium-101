# Module 05: Unit testing in Python

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

Execute `test.py` to see the order of execution of all set-up/tear-down and test methods!


## Flaky tests

These are tests which randomly fail without an obvious reason. The root cause behind them
is either timing issues (async JavaScript in a web context) or mismatch between the actual
environment the test is running into (DB records, files on disk, etc) and the environment
the tester imagined when the test was created! Execute `test.py` several times quickly
to trigger a flaky failure.

## Tasks & homework

* Return to Module 04 and re-examine the Bank Account task.
Define test scenarios for the `transfer_to()` method and implement
them using unit tests.
* Examine the existing test suite (for all previous tasks) in details. What other tests can be
written ? Write them!
