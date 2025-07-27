from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    A window for searching and managing client details and their bank accounts.
 
    This class extends LookupWindow to enable:
    - Searching for a client by client number.
    - Displaying the client's associated bank accounts in a table.
    - Viewing or modifying details of a selected account.
    """
    def __init__(self):
        """
        Initializes the ClientLookupWindow and sets up the UI components.
 
        Loads the client and account data, connects UI elements to methods,
        and prepares the window for interaction with the user.
        """
        super().__init__()

        # Load client and account data from external source
        self.client_listing, self.accounts = load_data()

        # Connect button and table events to their corresponding handler methods
        self.lookup_button.clicked.connect(self.on_lookup_client)  
        self.account_table.cellClicked.connect(self.__on_select_account)

    def on_lookup_client(self):
        """
        Handles the client lookup process when the user enters a client number.
        
        Validates the input, retrieves the client's details, and displays 
        their bank accounts in a table if the client exists.
        """
        # Get the client number from the input field
        client_number_input = self.client_number_edit.text()

        try:
            # Attempt to convert the client number to an integer
            client_number = int(client_number_input)
        except ValueError:
            # Show an error message if input is not a valid number
            QMessageBox.critical(self, "Input Error", "The client number must be a numeric value.")
            self.reset_display()  # Reset the display if input is invalid
            return

        # Clear the display before updating it with new data
        self.reset_display()

        # Check if the client number exists in the client listing
        if client_number not in self.client_listing:
            QMessageBox.critical(self, "Client Not Found", f"Client number {client_number} not found.")
            self.reset_display()  # Reset the display if client is not found
            return

        # Retrieve the client object from the listing using the client number
        client = self.client_listing[client_number]
        # Display the client's full name
        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        # Add rows to the account table for each bank account of the client
        self.account_table.setRowCount(0)
        for account in self.accounts.values():
            if account.client_number == client_number:
                self.add_account_to_table(account)

    def add_account_to_table(self, account: BankAccount):
        """
        Adds the details of a bank account to the account table.

        The account details displayed include:
        - Account number
        - Balance
        - Date created
        - Account type

        Args:
            account (BankAccount): The bank account whose details will be added to the table.
        """
        # Insert a new row at the end of the table
        row_position = self.account_table.rowCount()
        self.account_table.insertRow(row_position)

        # Create table items for each account detail
        account_number_item = QTableWidgetItem(str(account.account_number))
        balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
        date_created_item = QTableWidgetItem(account.date_created.strftime('%Y-%m-%d'))
        account_type_item = QTableWidgetItem(account.__class__.__name__)

        # Set text alignment for better table presentation
        account_number_item.setTextAlignment(Qt.AlignCenter)
        balance_item.setTextAlignment(Qt.AlignRight)
        date_created_item.setTextAlignment(Qt.AlignCenter)
        account_type_item.setTextAlignment(Qt.AlignCenter)

        # Add the items to their respective columns in the table
        self.account_table.setItem(row_position, 0, account_number_item)
        self.account_table.setItem(row_position, 1, balance_item)
        self.account_table.setItem(row_position, 2, date_created_item)
        self.account_table.setItem(row_position, 3, account_type_item)

        # Resize columns to ensure all content fits properly
        self.account_table.resizeColumnsToContents()

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """
        Handles the event when a bank account is selected from the table.
        
        Opens a new window (AccountDetailsWindow) to view or modify the selected account's details.

        Args:
            row (int): The row index of the selected account.
            column (int): The column index of the selected account (not used here).
        """
        # Get the account number from the selected row
        account_number_item = self.account_table.item(row, 0)

        if not account_number_item:
            QMessageBox.warning(self, "Invalid Selection", "Please select a valid account record.")
            return

        account_number = int(account_number_item.text())

        # Ensure the selected account exists
        if account_number not in self.accounts:
            QMessageBox.warning(self, "No Bank Account", "The selected account does not exist.")
            return

        # Retrieve the selected account and open the account details window
        account = self.accounts[account_number]
        account_details_window = AccountDetailsWindow(account)

        # Connect the account details window's signal to update the account data when modified
        account_details_window.balance_updated.connect(self.update_data)
        account_details_window.exec_()

    def update_data(self, account: BankAccount):
        """
        Updates the bank account data when the balance is changed.

        The account table is updated with the new balance, and the updated account
        data is saved to the accounts dictionary and external data file.

        Args:
            account (BankAccount): The updated bank account to save and reflect in the UI.
        """
        # Loop through the account table and find the row corresponding to the updated account
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)

            if account_number_item and account_number_item.text() == str(account.account_number):
                # Update the balance display for the selected account
                balance_item = self.account_table.item(row, 1)
                balance_item.setText(f"${account.balance:,.2f}")
                break

        # Save the updated account to the accounts dictionary and external data file
        self.accounts[account.account_number] = account
        update_data(account)

    def reset_display(self):
        """
        Resets the UI components: clears the client number input, client info label,
        and the account table.

        This method is called when there is a need to clear the display, such as after
        a failed lookup or when navigating away from the client details.
        """
        # Clear all display fields to reset the window
        self.client_number_edit.clear()
        self.client_info_label.clear()
        self.account_table.clearContents()
        self.account_table.setRowCount(0)
