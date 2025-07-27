"""
Description: Unit tests for the Client class.
Author: Jashan
Date: 07/26/2025
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):

    def test_client_init_valid(self):
        #Arrange
        Client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email ="tonystark@pixell.com"

        #Act
        Client_instance = Client(Client_number,first_name,last_name,email)

        #Assert
        self.assertEqual(Client_instance.client_number,Client_number)
        self.assertEqual(Client_instance.first_name, first_name)
        self.assertEqual(Client_instance.last_name,last_name)
        self.assertEqual(Client_instance.email_address, email)


    def test_client_invalid_client_number(self):
       #Arrange
       invalid_client_number = "invalid"
       first_name = "Tony"
       last_name = "Stark"
       email = "tonystark@pixell.com"

       #Act and Assert
       with self.assertRaises(ValueError):
           Client(invalid_client_number,first_name,last_name,email)

    def test_client_blank_first_name(self):
        # Arrange
        client_number = 1010
        first_name = " "
        last_name = "Stark"
        email = "tonystark@pixell.com"

        #Act and Assert
        with self.assertRaises(ValueError):
            Client(client_number,first_name,last_name,email)

    def test_client_blank_last_name(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        blank_last_name = " "
        email = "tonystark@pixell.com"

        #Act and Assert
        with self.assertRaises(ValueError):
            Client(client_number,first_name,blank_last_name,email)

    def test_client_invalid_email(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        invalid_email = "invalid-email"
        default_email = "email@pixell-river.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,invalid_email)

        #Assert
        self.assertEqual(client_instance.email_address,default_email)

    def test_return_client_number(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email = "tonystark@pixell.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,email)

        #Assert
        self.assertEqual(client_instance.client_number,client_number)

    def test_return_first_name(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email = "tonystark@pixell.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,email)

        #Assert
        self.assertEqual(client_instance.first_name,first_name)

    def test_return_last_name(self):
        #Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email = "tonystark@pixell.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,email)

        #Assert
        self.assertEqual(client_instance.last_name, last_name)

    def test_return_email_address(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email = "tonystark@pixell.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,email)

        #Assert
        self.assertEqual(client_instance.email_address, email)

    def test_str_method(self):
        # Arrange
        client_number = 1010
        first_name = "Tony"
        last_name = "Stark"
        email = "tonystark@pixell.com"
        expected_str = "Stark, Tony [1010] - tonystark@pixell.com"

        #Act
        client_instance = Client(client_number,first_name,last_name,email)
        
        #Assert
        self.assertEqual(str(client_instance),expected_str)

if __name__ == "__main__":
    unittest.main()
