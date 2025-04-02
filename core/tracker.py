from tkinter import *
from tkinter import messagebox
from core.transaction import Transaction
from utils.file_handler import read_transactions, write_transactions
from utils.visualizer import show_expense_chart
from core.logger import setup_logger
from core.settings import load_limits


class BudgetApp:
    """
    Main application class for the Smart Budget Tracker.

    Handles the GUI interface using Tkinter, processes user input,
    manages transactions, and triggers visualizations.
    """

    def __init__(self, root):
        """
        Initializes the GUI window, loads existing data, and sets up the logger and budget limits.

        Args:
            root (Tk): The main Tkinter window object.
        """
        self.root = root
        self.root.title("Smart Budget Tracker")

        # Load existing transactions from file
        self.transactions = read_transactions("data/transactions.csv")

        # Set up application logger
        self.logger = setup_logger()

        # Load category-wise spending limits
        self.limits = load_limits()

        # Build the GUI elements
        self.setup_ui()