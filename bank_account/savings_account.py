"""
Description: A class to manage SavingsAccount.
Author: Jashan
Date: 07/26/2025
"""

from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.00
    MINIMUM_BALANCE_DEFAULT = 50.00

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, 
                 minimum_balance: float = MINIMUM_BALANCE_DEFAULT, date_created=None):
        # Initialize the base BankAccount class
        super().__init__(account_number, client_number, balance, date_created)

        # Validate and set the minimum balance
        self.__minimum_balance = self._validate_float(minimum_balance, SavingsAccount.MINIMUM_BALANCE_DEFAULT)


    def __str__(self):
        """Returns a string representation of the SavingsAccount object,
        including account number, balance, and minimum balance.
        """
        return (f"Account Number: {self.account_number}\n"
                f"Balance: {self.format_currency(self.balance)}\n"
                f"Minimum Balance: {self.format_currency(self.__minimum_balance)}\n"
                f"Account Type: Savings")

    def get_service_charges(self):
        """
        Calculates the total service charges, considering if the balance 
        meets the minimum balance requirement.
        """
        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        else:
            return BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM


    @abstractmethod
    def _validate_float(self, value, default):
        """
        Validates if the given value can be converted to a float, 
        otherwise returns the default value.
        """
        try:
            return float(value)
        except (ValueError, TypeError):
            return default
        
    @property
    def minimum_balance(self):
        return self.__minimum_balance