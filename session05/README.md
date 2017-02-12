# Unit teesting in Python

## Preparation

* Read Chapter [26.4. unittest - Unit testing framework](https://docs.python.org/3/library/unittest.html);


In Python tests should inherit the standard `unittest.TestCase` class. Notable
methods are:

* `setUp(self)` - initialization of test environment
* `tearDown(self)` - clean up of test environment
* `runTest(self)` - if all tests go into one method or
* `test_XYZ(self)` - for testing specific functionality
* `assertXYZ(...)` - for asserting various conditions

The standard documentation contains the
[list of assert methods](https://docs.python.org/3/library/unittest.html#assert-methods)!

## Tasks & homework

* Return to Session 04 and re-examine the Bank Account task.
Define test scenarios for the `transfer_to()` method and implement
them using unit tests.
* Examine the existing test suite in details. What other tests can be
written ? Write them!
