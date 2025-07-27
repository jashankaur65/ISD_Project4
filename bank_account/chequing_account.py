"""
Description: A class to manage ChequingAccount.
Author: Jashan
Date: 07/26/2025
"""

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """
    A class representing a chequing account, with additional features such as overdraft limit and overdraft rate.
    """
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number : int, client_number : int, balance: float = 0.0, date_created: date = None, overdraft_limit: float = -100.0, overdraft_rate: float = 0.05):
        super().__init__(account_number, client_number, balance, date_created)

        # Initializing overdraft limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.0

        # Initializing overdraft rate
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            self.__overdraft_rate = 0.05
    
    def __str__(self):
        """
        Returns a string representation of the ChequingAccount object, including account number, balance, overdraft limit, and overdraft rate.
        """
        return (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f} Overdraft Rate: {self.__overdraft_rate * 100:.2f}% Account Type: Chequing")
    
    def get_service_charges(self):
        """
        Calculates the total service charges, including base service charge and an overdraft penalty if applicable.
        """
        if self.balance >= self.__overdraft_limit:
            return ChequingAccount.BASE_SERVICE_CHARGE
        else:
            overdraft_penalty = (self.__overdraft_limit - self.balance) * self.__overdraft_rate
            return ChequingAccount.BASE_SERVICE_CHARGE + overdraft_penalty
        
    def withdraw(self, amount):
        """
        Withdraws an amount, ensuring it doesn't exceed the overdraft limit.
        """

        if self.balance - amount < self.__overdraft_limit:
            raise ValueError("Withdrawal exceeds overdraft limit.")
        super().withdraw(amount)