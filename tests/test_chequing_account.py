"""
Description: Unit tests for the ChequingAccount class.
Author: Jashan
Date: 07/26/2025
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):
    """            
    Unit test for the ChequingAccount class
    """

    def setUp(self) -> None:
        """
        Setup method to initialize common variables for the tests.
        """
        self.account_number = 112233
        self.client_number = 889900
        self.balance = 500.0
        self.date_created = date.today()
        self.overdraft_limit = -100.0
        self.overdraft_rate = 0.05
       
        self.account = ChequingAccount(account_number = self.account_number, client_number = self.client_number, balance = self.balance, date_created = self.date_created, overdraft_limit = self.overdraft_limit, overdraft_rate = self.overdraft_rate)
 
    def test_init_valid_input(self):
        """
        Testing ChequingAccount with valid inputs. This verifies that all attributes are set correctly.
        """
        account = ChequingAccount(account_number=112233, client_number=889900, balance=500, date_created=date.today(), overdraft_limit=-100, overdraft_rate=0.05)

        self.assertEqual(account.account_number, 112233)
        self.assertEqual(account.client_number, 889900)
        self.assertEqual(account.balance, 500)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_overdraft_limit(self):
        """
        Testing with invalid overdraft limit.
        """
        account = ChequingAccount(account_number=112233, client_number=889900, balance=500, date_created=date.today(), overdraft_limit="invalid", overdraft_rate=0.05)

        self.assertEqual(account._ChequingAccount__overdraft_limit, -100)

    def test_init_invalid_overdraft_rate(self):
        """
        Testing with invalid overdraft rate.
        """
        account = ChequingAccount(account_number = 112233, client_number = 889900, balance = 500, date_created = date.today(), overdraft_limit = -100, overdraft_rate = "invalid")
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_date(self):
        """
        Testing with invalid date.
        """
        with self.assertRaises(ValueError):
            ChequingAccount(account_number = 112233, client_number = 889900, balance = 500, date_created = "invalid date", overdraft_limit = -100, overdraft_rate = 0.05)

    def test_get_service_charges_greater_than_overdraft_limit(self):
        """
        Test service charges when the balance is greater than the overdraft limit.
        """
        account = ChequingAccount(account_number = 112233, client_number = 889900, balance = 0, date_created = date.today(), overdraft_limit = -100, overdraft_rate = 0.05)

        self.assertEqual(account.get_service_charges(), 0.50)

    def test_get_service_charges_balance_less_than_overdraft_limit(self):
        """
        Test service charges when the balance is less than the overdraft limit.
        """
        account = ChequingAccount(account_number = 112233, client_number =889900, balance=-600, date_created=date.today(), overdraft_limit=-100, overdraft_rate=0.05)
       
        expected_service_charge = 0.50 + (-100 - -600) * 0.05
       
        self.assertEqual(account.get_service_charges(), expected_service_charge)

    def test_get_service_charges_balance_equal_to_overdraft_limit(self):
        """
        Test service charges when the balance is equal to the overdraft limit.
        """
        account = ChequingAccount(account_number = 112233, client_number = 889900, balance = -100, date_created = date.today() , overdraft_limit = -100, overdraft_rate = 0.05)

        self.assertEqual(account.get_service_charges(), 0.50)

    def test_str(self):
        """
        Test the string representation of the ChequingAccount.
        Verifies that the __str__ method returns a correctly formatted string.
        """
        account = ChequingAccount(account_number = 112233, client_number = 889900, balance = 1559.49, date_created = date.today(), overdraft_limit = -15.00, overdraft_rate = 0.05)
        expected_str = (
            "Account Number: 112233 Balance: $1,559.49\n"
            "Overdraft Limit: $-15.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()