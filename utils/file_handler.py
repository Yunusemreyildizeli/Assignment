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


def write_transactions(filepath, transactions):
    """
    Writes a list of transactions to a CSV file. Ensures the directory exists before writing.

    Args:
        filepath (str): Destination path for the CSV file.
        transactions (list[dict]): List of transactions to be saved.
    """
    # Ensure that the directory exists before writing the file
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Open the file and write headers and transaction data
    with open(filepath, 'w', newline='') as file:
        fieldnames = ['type', 'amount', 'category', 'description', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Write column headers
        for tx in transactions:
            writer.writerow(tx)  # Write each transaction row
