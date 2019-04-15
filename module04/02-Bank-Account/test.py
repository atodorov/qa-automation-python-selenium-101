import unittest
from datetime import datetime
from solution import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Rado", 0, "$")

    def test_can_create_bank_account(self):
        ''''
            Sanity test that nothing went wrong in the init method.
            Not really a very practical one but students are full of suprprizes
        '''
        self.assertTrue(isinstance(self.account, BankAccount))
        # which is the same as
        self.assertIsInstance(self.account, BankAccount)

    def test_initial_zero_balance(self):
        self.assertEqual(self.account.balance(), 0)

    def test_good_example_of_using_with_block(self):
        account = BankAccount("Test", 100, "BGN")
        # .... 100 more lines of code
        #raise ValueError('Can you find me!')
        # and few more
        with self.assertRaises(ValueError):
            account.deposit(-10)

    def test_bad_example_of_using_with_block(self):
        with self.assertRaises(ValueError):
            account = BankAccount("Test", 100, "")
            # DON'T stuff everything inside a with block
            # b/c you may catch exceptions which are not coming
            # from the method under test and you will never know
            # about them
            raise ValueError('Can you find me!')
            # .... 100 more lines of code
            account.deposit(-10)

    def test_negative_initial_amount(self):
        with self.assertRaises(ValueError):
            acc = BankAccount("Test", -100, "$")
            BankAccount("Test", 100, "")

        # this is not possible b/c acc is available only
        # inside the with block.
        # print acc

        with self.assertRaises(ValueError):
            BankAccount("Test", 100, "")

    def test_init_with_empty_currency(self):
        with self.assertRaises(ValueError):
            BankAccount("Test", 100, "")

    def test_deposit_in_empty_account(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance(), 500)

    def test_deposit_in_not_empty_account(self):
        account = BankAccount("Ivo", 1000, "$")
        account.deposit(500)
        self.assertEqual(account.balance(), 1500)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_from_not_empty_account(self):
        self.account.deposit(100)
        result = self.account.withdraw(50)

        self.assertTrue(result)
        self.assertEqual(self.account.balance(), 50)

    def test_withdraw_from_empty_account(self):
        result = self.account.withdraw(50)

        self.assertIsNotNone(result)
        self.assertFalse(result)

    def test_history(self):
        account = BankAccount("Test", 0, "$")
        account.deposit(20)
        account.balance()
        int(account)
        expected = ["Account was created", "Deposited 20$",
                    "Balance check -> 20$", "__int__ check -> 20$"]

        self.assertEqual(account.history(), expected)


class TestBankAccount_transfer_to(unittest.TestCase):
    '''
        It is also possible to create test classes that test a single
        method. In this case we want a separate class for testing the
        BankAccount.transfer_to() method because there are several
        scenarios and we want to better organize them.
    '''
    def setUp(self):
        self.account = BankAccount('For testing', 100, 'BGN')

    def test_transfer_to_without_parameters(self):
        # raises when other account is missing
        with self.assertRaises(TypeError):
            self.account.transfer_to(1)

        # can be written as
        self.assertRaises(TypeError, self.account.transfer_to, 1)

        # raises when how_miuch is missing
        other_account = BankAccount('with zero balance', 0, '$')
        with self.assertRaises(TypeError):
            self.account.transfer_to(other_account)
        # this is not necessary ????
        self.assertEqual(other_account.balance(), 0)
        self.assertEqual(self.account.balance(), 100)

    def test_transfer_between_different_currencies_not_possible(self):
        leva_account = BankAccount('For testing', 100, 'BGN')
        dollar_account = BankAccount('In dollars', 10, '$')

        with self.assertRaises(TypeError):
            leva_account.transfer_to(dollar_account, 50)

        self.assertEqual(leva_account.balance(), 100)
        self.assertEqual(dollar_account.balance(), 10)

    def test_transfer_negative_amount(self):
        account_1 = BankAccount('For testing', 100, '$')
        account_2 = BankAccount('In dollars', 10, '$')

        with self.assertRaises(ValueError):
            account_1.transfer_to(account_2, -50)

        self.assertEqual(account_1.balance(), 100)
        self.assertEqual(account_2.balance(), 10)


    def test_transfer_positive_mount_should_work(self):
        account_1 = BankAccount('For testing', 100, '$')
        account_2 = BankAccount('In dollars', 10, '$')

        account_1.transfer_to(account_2, 50)

        self.assertEqual(account_1.balance(), 50)
        self.assertEqual(account_2.balance(), 60)

    def test_transfer_more_than_vailable_balance_should_fail(self):
        account_1 = BankAccount('For testing', 100, '$')
        account_2 = BankAccount('In dollars', 10, '$')

        with self.assertRaises(Exception):
            account_1.transfer_to(account_2, 150)

        self.assertEqual(account_1.balance(), 100)
        self.assertEqual(account_2.balance(), 10)


if __name__ == '__main__':
    unittest.main()
