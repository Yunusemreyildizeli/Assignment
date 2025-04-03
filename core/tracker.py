# tracker.py

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

    def setup_ui(self):
        """
        Creates and places all the input fields, labels, and buttons in the Tkinter window.
        """
        Label(self.root, text="Amount").grid(row=0, column=0)
        self.amount_entry = Entry(self.root)
        self.amount_entry.grid(row=0, column=1)

        Label(self.root, text="Category").grid(row=1, column=0)
        self.category_entry = Entry(self.root)
        self.category_entry.grid(row=1, column=1)

        Label(self.root, text="Description").grid(row=2, column=0)
        self.description_entry = Entry(self.root)
        self.description_entry.grid(row=2, column=1)

        # Radio buttons to choose between expense or income
        self.type_var = StringVar(value="expense")
        Radiobutton(self.root, text="Expense", variable=self.type_var, value="expense").grid(row=3, column=0)
        Radiobutton(self.root, text="Income", variable=self.type_var, value="income").grid(row=3, column=1)

        # Buttons for core functionality
        Button(self.root, text="Add Transaction", command=self.add_transaction).grid(row=4, columnspan=2)
        Button(self.root, text="Show Chart", command=lambda: show_expense_chart(self.transactions)).grid(row=5,
                                                                                                         columnspan=2)
        Button(self.root, text="Save Transactions", command=self.save_transactions).grid(row=6, columnspan=2)

    def add_transaction(self):
        """
        Validates and adds a new transaction to the list.
        Also checks for budget limit warnings and logs the action.
        """
        try:
            # Read and convert input values
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            description = self.description_entry.get()
            trans_type = self.type_var.get()

            # Create a Transaction object and append to the list
            tx = Transaction(trans_type, amount, category, description)
            self.transactions.append(tx.to_dict())
            self.logger.info(f"Transaction added: {tx.to_dict()}")

            # Check if the category has a budget limit and trigger warning if exceeded
            if trans_type=="expense" and category in self.limits:
                spent = sum(t['amount'] for t in self.transactions if t['type']=="expense" and t['category']==category)
                if spent > self.limits[category]:
                    messagebox.showwarning("Limit Exceeded", f"Warning: Spending in '{category}' exceeded the limit!")

            messagebox.showinfo("Success", "Transaction Added")

        except Exception as e:
            self.logger.error(f"Failed to add transaction: {e}")
            messagebox.showerror("Error", f"Failed to add transaction: {e}")

    def save_transactions(self):
        """
        Writes all transactions to the CSV file and confirms success to the user.
        Logs the outcome of the operation.
        """
        try:
            write_transactions("data/transactions.csv", self.transactions)
            messagebox.showinfo("Saved", "Transactions saved successfully.")
        except Exception as e:
            self.logger.error(f"Save failed: {e}")
            messagebox.showerror("Error", "Failed to save transactions.")
