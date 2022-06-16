import unittest

from exer7 import BankAccount


class BankAccountTestCase(unittest.TestCase):
    '''Test withdraw and deposit for exer7'''
    def setUp(self):
        self.account = BankAccount(name="Jake", balance=50000)

    def test_withdraw_in_bank_account(self):
        """Test if withdraw works"""
        amount = 5000
        actual = self.account.withdraw(amount)
        self.assertEqual(actual, 45000)

    def test_deposit_in_bank_account(self):
        amount = 3000
        actual = self.account.deposit(amount)
        self.assertEqual(actual, 53000)


def main():
    unittest.main()


if __name__ == '__main__':
    main()