"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Author: Jashan
Date: 07/26/2025
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_init_valid(self):
        account_number = 12345
        client_number = 67890
        initial_balance = 100.50

        account = BankAccount(account_number, client_number, initial_balance)
        
        self.assertEqual(account.account_number, account_number)
        self.assertEqual(account.client_number, client_number)
        self.assertEqual(account.balance, initial_balance)


    def test_init_invalid_account_number(self):
        invalid_account_number = "12345"
        client_number = 67890
        initial_balance = 100.50

        with self.assertRaises(ValueError) as context:
            BankAccount(invalid_account_number, client_number, initial_balance)
        self.assertEqual(str(context.exception), "Account number must be an integer.")
    
    def test_init_invalid_client_number(self):
        account_number = 12345
        invalid_client_number = "67890"
        initial_balance = 100.50

        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, invalid_client_number, initial_balance)
        self.assertEqual(str(context.exception), "Client number must be an integer.")

    def test_init_invalid_balance(self):
        account_number = 12345
        client_number = 67890
        invalid_initial_balance = "0.0"

        account = BankAccount(account_number, client_number, invalid_initial_balance)

        self.assertEqual(account.balance, 0.0)

    def test_deposit_valid(self):
        account = BankAccount(12345, 67890, 100.50)
        deposit_amount = 50.00

        account.deposit(deposit_amount)

        self.assertEqual(account.balance, 150.5)

    def test_deposit_invalid_type(self):
        account = BankAccount(12345, 67890, 100.50)
        invalid_amount = "invalid"

        with self.assertRaises(ValueError) as context:
            account.deposit("invalid")
        self.assertEqual(str(context.exception), "Deposit amount: invalid must be numeric.")

    def test_deposit_negative_amount(self):
        account = BankAccount(12345, 67890, 100.50)
        invalid_amount = -50.00

        with self.assertRaises(ValueError) as context:
            account.deposit(invalid_amount)
        self.assertEqual(str(context.exception), "Deposit amount: $-50.00 must be positive.")

    def test_withdraw_valid(self):
        account = BankAccount(12345, 67890, 100.50)
        withdraw_amount = 50.00

        account.withdraw(withdraw_amount)

        self.assertEqual(account.balance, 50.50)

    def test_withdraw_invalid_type(self):
        account = BankAccount(12345, 67890, 100.50)
        invalid_amount = "invalid"

        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)
        self.assertEqual(str(context.exception), "Withdraw amount: invalid must be numeric.")

    def test_withdraw_negative_amount(self):
        account = BankAccount(12345, 67890, 100.50)
        invalid_amount = -50.00

        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)
        self.assertEqual(str(context.exception), "Withdraw amount: $-50.00 must be positive.")

    def test_withdraw_exceeding_balance(self):
        account = BankAccount(12345, 67890, 100.50)
        exceeding_amount = 150.00

        with self.assertRaises(ValueError) as context:
            account.withdraw(exceeding_amount)
        self.assertEqual(str(context.exception), "Withdraw amount: $150.00 must not exceed the account balance: $100.50.")

    def test_update_balance_valid_positive(self):
        account = BankAccount(12345, 67890, 100.50)
        amount_to_add = 50.00

        account.update_balance(amount_to_add)

        self.assertEqual(account.balance, 150.5)

    def test_update_balance_valid_negative(self):
        account = BankAccount(12345, 67890, 100.50)
        amount_to_deduct = -50.00

        account.update_balance(amount_to_deduct)

        self.assertEqual(account.balance, 50.50)

    def test_update_balance_invalid(self):
        account = BankAccount(12345, 67890, 100.50)
        invalid_amount = "invalid"

        account.update_balance(invalid_amount)

        self.assertEqual(account.balance, 100.50)

    def test_str_output(self):
        account = BankAccount(12345, 67890, 100.50)

        result = str(account)

        self.assertEqual(result, "Account Number: 12345 Balance: $100.50")

    def test_rounding_of_balance(self):
        account = BankAccount(12345, 67890, 100.5555555)

        rounded_balance = round(account.balance, 2)

        self.assertEqual(rounded_balance, 100.56)


if __name__ == "__main__":
    unittest.main()