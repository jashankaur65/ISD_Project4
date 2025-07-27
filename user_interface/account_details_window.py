from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A window that displays details of a bank account and allows transactions
    (deposits and withdrawals) to be performed on the account.
    """

    # Signal to notify when the account balance is updated
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes the AccountDetailsWindow and sets up the UI components.

        Args:
            account (BankAccount): The bank account whose details are to be displayed.
        
        Returns:
            None
        """
        super().__init__()

        # Validate the provided account type
        if not isinstance(account, BankAccount):
            QMessageBox.critical(self, "Error", "Invalid account type provided.")
            self.reject()  # Close the window if the account type is invalid
            return
        
        # Create a copy of the account to avoid modifying the original account object
        self.account = copy.copy(account)

        # Set the account number and balance in the respective labels
        self.account_number_label.setText(str(self.account.account_number))
        self.balance_label.setText(f"${self.account.balance:,.2f}")

        # Connect the buttons to their respective handlers
        self.deposit_button.clicked.connect(self.on_apply_transaction)
        self.withdraw_button.clicked.connect(self.on_apply_transaction)
        self.exit_button.clicked.connect(self.on_exit)

    def on_apply_transaction(self) -> None:
        """
        Handles deposit and withdrawal transactions based on which button was clicked.

        Attempts to parse the transaction amount and apply the appropriate transaction
        (deposit or withdrawal). If successful, the account balance is updated and
        a signal is emitted to notify the balance update. If there is an error, a warning
        or error message is shown.

        Returns:
            None
        """
        try:
            # Parse the transaction amount input as a float
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            # Show an error message if the input is not a valid number
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()  # Focus back to the input field
            return
        
        transaction_type = ""  # To track which type of transaction (Deposit/Withdraw)

        try:
            # Determine the transaction type based on the sender (button clicked)
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)  # Apply deposit
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)  # Apply withdrawal

            # Update the displayed balance after the transaction
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Emit the signal to notify other components of the balance update
            self.balance_updated.emit(self.account)

            # Clear the input field and refocus it for the next transaction
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            # Display an error message if the transaction fails
            QMessageBox.critical(self, f"{transaction_type} Failed", str(e))
            self.transaction_amount_edit.clear()  # Clear the input field after error
            self.transaction_amount_edit.setFocus()  # Refocus the input field

    def on_exit(self) -> None:
        """
        Closes the AccountDetailsWindow.

        This method is triggered when the user clicks the 'Exit' button to close
        the window.

        Returns:
            None
        """
        self.close()
