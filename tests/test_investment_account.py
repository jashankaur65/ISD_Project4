"""
Description: Unit tests for the InvestmentAccount class.
Author: Jashan
Date: 07/26/2025
"""

from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
import unittest

class TestInvestmentAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.account_number = 112233
        self.client_number = 889900
        self.balance = 500.00
        self.management_fee = 15.0
        self.date_created = date.today()

        # Create a valid InvestmentAccount instance
        self.account = InvestmentAccount(
            account_number=self.account_number,
            client_number=self.client_number,
            balance=self.balance,
            management_fee=self.management_fee,
            date_created=self.date_created)
        
    def test_init_valid_values(self):
        """Test initialization with valid values."""
        account = InvestmentAccount(
            account_number=112233,
            client_number=889900,
            balance=500.0,
            management_fee=15.0,
            date_created=date.today()
        )
        self.assertEqual(account.account_number, 112233)
        self.assertEqual(account.client_number, 889900)
        self.assertEqual(account.balance, 500.0)
        self.assertEqual(account._InvestmentAccount__management_fee, 15.0)

    def test_init_invalid_management_fee_type(self):
        """Test initialization with an invalid management fee type."""
        account = InvestmentAccount(
            account_number=112233,
            client_number=889900,
            balance=500.0,
            management_fee="invalid",
            date_created=date.today()
        )
        self.assertEqual(account._InvestmentAccount__management_fee, 2.55)

    def test_get_service_charges_date_older_than_10_years(self):
        """Test get_service_charges with a creation date older than 10 years."""
        today = date.today()
        old_date = today.replace(year=today.year - 15)
        account = InvestmentAccount(
            account_number=112233,
            client_number=889900,
            balance=500.0,
            date_created=old_date,
            management_fee=self.management_fee
        )
        except_service_charges = 5.0
        self.assertEqual(account.get_service_charges(), except_service_charges)

    def test_get_service_charges_date_within_10_years(self):
        """Test get_service_charges with a date created within 10 years."""
        account = InvestmentAccount(
            account_number=self.account_number,
            client_number=self.client_number,
            balance=self.balance,
            management_fee=self.management_fee,
            date_created=self.date_created
        )
        expected_service_charges = BankAccount.BASE_SERVICE_CHARGE + self.management_fee
        self.assertEqual(account.get_service_charges(), expected_service_charges)

    def test_get_service_charges_date_exactly_10_years(self):
        """Test get_service_charges with a date created exactly 10 years ago."""
        old_date = date.today() - timedelta(days=10 * 365.25)
        account = InvestmentAccount(
            account_number=112233,
            client_number=889900,
            balance=500.0,
            date_created=old_date,
            management_fee=self.management_fee
            )
        
        except_service_charge = 5
        self.assertEqual(account.get_service_charges(), except_service_charge)

    def test_str_waived_management_fee(self):
        """Test str method with a waived management fee."""
        old_date = date.today() - timedelta(days = 11 * 365.25)
        account = InvestmentAccount(
            account_number=112233,
            client_number=889900,
            balance=500.0,
            date_created=old_date,
            management_fee=self.management_fee
            )
        
        expected_str = (f"Account Number: {self.account_number}\n"
                        f"Balance: ${self.balance:,.2f}\n"
                        f"Date Created: {old_date}\n"
                        f"Management Fee: Waived\n"
                        f"Account Type: Investment"
                        )
        self.assertEqual(str(account), expected_str)

    def test_str_with_management_fee(self):
        """Test str method with a management fee."""
        expected_str = (f"Account Number: {self.account_number}\n"
                        f"Balance: ${self.balance:,.2f}\n"
                        f"Date Created: {self.date_created}\n"
                        f"Management Fee: ${self.management_fee:,.2f}\n"
                        f"Account Type: Investment"
                        )
        self.assertEqual(str(self.account), expected_str)

if __name__ == '__main__':
    unittest.main()