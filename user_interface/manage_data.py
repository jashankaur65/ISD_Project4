import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from typing import Tuple, Dict
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount
from client.client import Client

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************

def load_data() -> Tuple[Dict[int, Client], Dict[int, BankAccount]]:
    """
    Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.
    Returns:
        tuple containing client dictionary and account dictionary.
    """
    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    try:
        with open(clients_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for record in reader:
                try:
                    client_number = int(record['client_number'])
                    first_name = record['first_name']
                    last_name = record['last_name']
                    email_address = record['email_address']
                    
                    # Create Client object and add to client_listing dictionary
                    client = Client(client_number, first_name, last_name, email_address)
                    client_listing[client_number] = client
                except Exception as e:
                    logging.error(f"Unable to create client: {e}")
    except FileNotFoundError:
        logging.error("clients.csv file not found.")
    except Exception as e:
        logging.error(f"Error reading clients.csv: {e}")
        

    # READ ACCOUNT DATA
    try:
        with open(accounts_csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for record in reader:
                try:
                    account_number = int(record['account_number'])
                    client_number = int(record['client_number'])
                    balance = float(record['balance'])
                    date_created = datetime.strptime(record['date_created'], "%Y-%m-%d")
                    account_type = record['account_type']
                    
                    # Create appropriate BankAccount object
                    if account_type == "ChequingAccount":
                        overdraft_limit = float(record['overdraft_limit'])
                        overdraft_rate = float(record['overdraft_rate'])
                        account = ChequingAccount(account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate)
                    elif account_type == "SavingsAccount":
                        minimum_balance = float(record['minimum_balance'])
                        account = SavingsAccount(account_number, client_number, balance, date_created, minimum_balance)
                    elif account_type == "InvestmentAccount":
                        management_fee = float(record['management_fee'])
                        account = InvestmentAccount(account_number, client_number, balance, date_created, management_fee)
                    else:
                        logging.error(f"Not a valid account type: {account_type}")
                        continue
                    
                    # Check if client exists and add the account to the accounts dictionary
                    if client_number in client_listing:
                        accounts[account_number] = account
                    else:
                        logging.error(f"Bank Account: {account_number} contains invalid Client Number: {client_number}")
                except Exception as e:
                    logging.error(f"Unable to create bank account: {e}")
    except FileNotFoundError:
        logging.error("accounts.csv file not found.")
    except Exception as e:
        logging.error(f"Error reading accounts.csv: {e}")

    # RETURN STATEMENT
    return client_listing, accounts


def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:
                # Update the balance column with the new balance from the dictionary
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)


# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")