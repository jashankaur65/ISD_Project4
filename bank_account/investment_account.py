"""
Description: A class to manage InvestmentAccount.
Author: Jashan
Date: 07/26/2025
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from abc import ABC, abstractmethod

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today() - timedelta(days=10*365.25)

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, 
                 management_fee: float = 2.55, date_created: date = None):
        # Use super() to initialize the base BankAccount class
        super().__init__(account_number, client_number, balance, date_created)

        # Validate and set management fee
        self.__management_fee = self._validate_float(management_fee, 2.55)

    def __str__(self):
        """
        Returns a string representation of the InvestmentAccount object, 
        including account number, balance, and management fee status.
        """
        management_fee_str = "Waived" if self.date_created <= InvestmentAccount.TEN_YEARS_AGO \
            else self.format_currency(self.__management_fee)

        return (f"Account Number: {self.account_number}\n"
                f"Balance: {self.format_currency(self.balance)}\n"
                f"Date Created: {self.date_created}\n"
                f"Management Fee: {management_fee_str}\n"
                f"Account Type: Investment")

    def get_service_charges(self):
        """
        Calculates the total service charges, considering the management fee status.
        """
        if self.date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    @abstractmethod
    def _validate_float(self, value, default_value):
        """
        Validates if the given value can be converted to a float, otherwise returns the default value.
        """
        if isinstance(value, float):
            return value
        return default_value
