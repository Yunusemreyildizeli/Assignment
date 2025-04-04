# transaction.py

from datetime import datetime


class Transaction:
    """
    Represents a financial transaction (either income or expense).

    Stores transaction details including type, amount, category,
    description, and timestamp. Used for data entry, saving, and
    visualization within the Smart Budget Tracker application.
    """

    def __init__(self, trans_type, amount, category, description, date=None):
        """
        Initializes a Transaction object with user-supplied or system-generated data.

        Args:
            trans_type (str): The type of transaction ('income' or 'expense').
            amount (float): The monetary value of the transaction.
            category (str): The category this transaction belongs to.
            description (str): A brief explanation of the transaction.
            date (str, optional): Timestamp of the transaction. If None, current time is used.
        """
        self.trans_type = trans_type
        self.amount = float(amount)
        self.category = category
        self.description = description

        # Use current timestamp if no date is provided
        self.date = date if date else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
