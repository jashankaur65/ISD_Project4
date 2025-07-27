"""
Description: Unit tests for the SavingAccount class.
Author: Jashan
Date: 07/26/2025
"""
from datetime import date
from bank_account.savings_account import SavingsAccount
import unittest

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        """Set up some initial values for testing"""
        self.account_number = 112233
        self.client_number = 889900
        self.balance = 500.00
        self.date_created = date.today()
        self.minimum_balance = 50.00
    
    def test_init_valid_values(self):
        """Test that attributes are correctly set when initialized with valid parameters."""
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.balance, 
                                self.minimum_balance, 
                                self.date_created
                                )
        self.assertEqual(account.balance, self.balance)
        self.assertEqual(account.minimum_balance, self.minimum_balance)

    def test_init_invalid_minimum_balance(self):
        """Test that minimum balance defaults to 50.00 when an invalid value is provided."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance, "invalid_balance", self.date_created)
        self.assertEqual(account.minimum_balance, SavingsAccount.MINIMUM_BALANCE_DEFAULT)

    def test_get_service_charges_balance_greater_than_minimum(self):
        """Test that service charges are correctly calculated when balance is greater than minimum balance."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance, self.minimum_balance, self.date_created)
        self.assertEqual(account.get_service_charges(), account.BASE_SERVICE_CHARGE)

    def test_get_service_changes_balance_equal_to_minimum(self):
        """Test that service charges are correctly calculated when balance is equal to minimum balance."""
        account = SavingsAccount(self.account_number, self.client_number, 50.00, self.minimum_balance, self.date_created)
        self.assertEqual(account.get_service_charges(), account.BASE_SERVICE_CHARGE)

    def test_get_service_charges_balance_less_than_minimum(self):
        """Test that service charges are correctly calculated when balance is less than minimum balance."""
        account = SavingsAccount(self.account_number, self.client_number, 49.99, self.minimum_balance, self.date_created)
        expected_service_charge = account.BASE_SERVICE_CHARGE * account.SERVICE_CHARGE_PREMIUM
        self.assertEqual(account.get_service_charges(), expected_service_charge)

    def test_str_method(self):
        """Test that the __str__ method returns a string representation of the account."""
        account = SavingsAccount(self.account_number, self.client_number, self.balance, self.minimum_balance, self.date_created)
        expected_str = (f"Account Number: {self.account_number}\n"
                        f"Balance: {account.format_currency(self.balance)}\n"
                        f"Minimum Balance: {account.format_currency(self.minimum_balance)}\n"
                        f"Account Type: Savings")
        self.assertEqual(str(account), expected_str)

if __name__ == '__main__':
    unittest.main()