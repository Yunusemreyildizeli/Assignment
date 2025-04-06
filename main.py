# main.py

from tkinter import Tk
from core.tracker import BudgetApp

# Entry point for the Smart Budget Tracker application.
# Initializes the main Tkinter window and launches the BudgetApp interface.

if __name__ == "__main__":
    # Create the main Tkinter window
    root = Tk()

    # Initialize the BudgetApp with the root window
    app = BudgetApp(root)

    # Start the GUI event loop
    root.mainloop()