import unittest
from solution import Bill, BatchBill, CashDesk


class TestBill(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(5)

    def test_bill_str(self):
        self.assertEqual(str(self.bill), "A 5$ bill")

    def test_bill_int(self):
        self.assertEqual(int(self.bill), 5)

    def test_bill_eq(self):
        bill2 = Bill(10)
        bill3 = Bill(5)
        self.assertNotEqual(self.bill, bill2)
        self.assertEqual(False, self.bill == bill2)
        self.assertEqual(self.bill, bill3)

    def test_type_of_amount(self):
        with self.assertRaises(TypeError):
            Bill("10")

    def test_value_of_amount(self):
        with self.assertRaises(ValueError):
            Bill(-5)


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.bill5 = Bill(5)
        self.bill10 = Bill(10)
        self.batch = BatchBill([self.bill5, self.bill10])

    def test_batchbill_init(self):
        self.assertIn(self.bill5, self.batch)
        self.assertIn(self.bill10, self.batch)

    def test_batchbill_total(self):
        self.assertEqual(self.batch.total(), 15)


class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(10)
        self.batch = BatchBill([Bill(5), Bill(10), Bill(15)])
        self.desk = CashDesk()

    def test_take_money_from_bill(self):
        self.desk.take_money(self.bill)
        self.assertEqual(self.desk.total(), 10)

    def test_take_money_from_batch(self):
        self.desk.take_money(self.batch)
        self.assertEqual(self.desk.total(), 30)

    def test_cashdesk_total(self):
        self.desk.take_money(self.bill)
        self.desk.take_money(self.batch)
        self.assertEqual(
            self.desk.total(), 40)

    def test_cashdesk_inspect_value(self):
        self.desk.take_money(self.bill)
        self.desk.take_money(self.batch)

        expected = """We have a total of 40$ in the desk
We have the following count of bills, sorted in ascending order:
5$ bills - 1
10$ bills - 2
15$ bills - 1"""

        self.assertEqual(self.desk.inspect(), expected)

if __name__ == '__main__':
    unittest.main()
