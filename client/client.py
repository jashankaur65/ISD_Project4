"""
Description: A class to manage Client.
Author: Jashan
Date: 07/26/2025
"""

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

class Client(Observer):
    """Implementation of Observer pattern in client class"""
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer")
        self.__client_number = client_number

        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank")
        self.__first_name = first_name
        
        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank")
        self.__last_name = last_name

        try:
            valid = validate_email(email_address)
            self.__email_address = valid.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"
    
    @staticmethod
    def validate_integer(value, field_name):
        """Validate integer value for client number"""
        if not isinstance(value, int):
            raise ValueError(f"{field_name} must be an integer")
        return value
    
    @staticmethod
    def Validate_non_empty_string(value, field_name):
        """Validate non-empty string for first name and last name"""
        if not value.strip():
            raise ValueError(f"{field_name} cannot be blank")
        return value
    
    @staticmethod
    def validate_email(email):
        """Validate email address"""
        try:
            valid = validate_email(email)
            return valid.email
        except EmailNotValidError:
            return "email@pixell-river.com"

    @property
    def client_number(self):
        return self.__client_number
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def email_address(self):
        return self.__email_address
    
    def update(self, subject, message):
        """Update the client with a new message"""
        formatted_message = f"Subject: {subject}\nMessage: {message}\nSent to {self.email_address}"
        simulate_send_email(self.email_address, subject, message)
        print(f"Notification sent to {self.__str__()}: {formatted_message}")

    def __str__(self):
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}"
