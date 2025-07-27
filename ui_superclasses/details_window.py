from PySide6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QDialog, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class DetailsWindow(QDialog):
    """
    A Python class which allows users perform bank account 
    transactions. This class is meant to work in conjunction 
    with the BankAccount class such that deposit and withdraw 
    functionality may be used.
    """
    def __init__(self):
        """
        Initializes the Details window by adding 
        various widgets and setting properties. Widgets include: 
        account_number_label, balance_label, transaction_amount_label, 
        deposit_button, withdraw_button and exit_button.
        """
        # Design window.
        super().__init__()
        self.setWindowTitle("Transaction Processor")
        self.resize(200, 200)

        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignTop)  
        layout.setHorizontalSpacing(10)
        layout.setVerticalSpacing(10)

        # Bold font for labels and headers
        bold_font = QFont()
        bold_font.setBold(True)

        # Account details widgets
        self.account_number_prompt_label = QLabel("Account Number:")
        self.account_number_prompt_label.setFont(bold_font)
        self.account_number_label = QLabel()
        self.balance_prompt_label = QLabel("Balance:")
        self.balance_prompt_label.setFont(bold_font)
        self.balance_label = QLabel()
        self.transaction_amount_prompt_label = QLabel("Transaction Amount:")
        self.transaction_amount_prompt_label.setFont(bold_font)
        self.transaction_amount_edit = QLineEdit()
        self.transaction_amount_edit.setFixedWidth(75)
        
        # Right align data.
        self.account_number_label.setAlignment(Qt.AlignRight)
        self.balance_label.setAlignment(Qt.AlignRight)
        self.transaction_amount_edit.setAlignment(Qt.AlignRight)

        # Buttons with QHBoxLayout.
        buttonLayout = QHBoxLayout()
        self.deposit_button = QPushButton("Deposit")
        self.withdraw_button = QPushButton("Withdraw")
        self.exit_button = QPushButton("Exit")

        # Add buttons to the QHBoxLayout object
        buttonLayout.addWidget(self.deposit_button)
        buttonLayout.addWidget(self.withdraw_button)
        buttonLayout.addWidget(self.exit_button)
        buttonLayout.addStretch(1)

        # Adding widgets to the overall layout.
        layout.addWidget(self.account_number_prompt_label, 0, 0)
        layout.addWidget(self.account_number_label, 0, 1)
        layout.addWidget(self.balance_prompt_label, 1, 0)
        layout.addWidget(self.balance_label, 1, 1)
        layout.addWidget(self.transaction_amount_prompt_label, 2, 0)
        layout.addWidget(self.transaction_amount_edit, 2, 1)
        # Adding the button layout to the grid: spanning 2 columns
        layout.addLayout(buttonLayout, 3, 0, 1, 2)  

        # Add stretch to push everything to the top-left
        layout.setColumnStretch(2, 1)  
        layout.setRowStretch(4, 1)  


    


    
