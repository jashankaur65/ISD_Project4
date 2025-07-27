"""
Description: A class to manage Client.
Author: Jashan
Date: 07/26/2025
"""
from datetime import date
from abc import ABC, abstractmethod

class BankAccount:
    BASE_SERVICE_CHARGE = 5.00
    
    def __init__(self, account_number: int, client_number: int, balance: float = 0.0, date_created: date = None):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self.__account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        self.__balance = self.validate_balance(balance)

        if date_created is None:
            self.__date_created = date.today()
        elif isinstance(date_created, date):
            self.__date_created = date_created
        else:
            raise ValueError("Date created must be an instance of datetime.date")
    
    @abstractmethod
    def validate_integer(value, field_name):
        """Validate if the value is an integer."""
        if not isinstance(value, int):
            raise ValueError(f"{field_name} must be an integer.")
        return value
    
    @staticmethod
    def validate_balance(balance):
        """Ensure the balance is a valid float."""
        try:
            return float(balance)
        except ValueError:
            raise ValueError("Balance must be a numeric value.")

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def client_number(self):
        return self.__client_number
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def date_created(self):
        return self.__date_created
    
    # Update balance
    def update_balance(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be numeric.")
        self.__balance += amount

    # Deposit
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            formatted_amount = "${:,.2f}".format(amount)
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")
        
        self.update_balance(amount)


    # # Withdraw
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            formatted_amount = "${:,.2f}".format(amount)
            raise ValueError(f"Withdraw amount: {formatted_amount} must be positive.")
        
        if amount > self.__balance:
            formatted_amount = "${:,.2f}".format(amount)
            formatted_balance = "${:,.2f}".format(self.__balance)
            raise ValueError(f"Withdraw amount: {formatted_amount} must not exceed the account balance: {formatted_balance}.")
        
        self.update_balance(-amount)

    @staticmethod
    def validate_positive_amount(amount, transaction_type):
        """Validate if the amount is positive"""
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"{transaction_type} amount must be numeric.")
        if amount <= 0:
            raise ValueError(f"{transaction_type} amount must be positive")
        return amount

    @staticmethod
    def format_currency(amount):
        """Format the amount as currency"""
        return "${:,.2f}".format(amount)
    
    def __str__(self):
        return (f"Account Number: {self.__account_number}, "
                f"Client Number: {self.__client_number}, "
                f"Balance: {self.format_currency(self.__balance)}, "
                f"Date Created: {self.format_currency(self.__date_created)}")