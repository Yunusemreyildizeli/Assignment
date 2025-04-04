# file_handler.py

import csv
import os


def read_transactions(filepath):
    """
    Reads transaction records from a CSV file and returns them as a list of dictionaries.
    Automatically converts the 'amount' field to float for numerical processing.

    Args:
        filepath (str): Path to the transactions CSV file.

    Returns:
        list[dict]: List of transaction dictionaries.
    """
    transactions = []

    # Check if the file exists before attempting to read
    if os.path.exists(filepath):
        with open(filepath, 'r', newline='') as file:
            reader = csv.DictReader(file)

            # Iterate through each row and convert the amount to float
            for row in reader:
                row['amount'] = float(row['amount'])
                transactions.append(row)

    return transactions